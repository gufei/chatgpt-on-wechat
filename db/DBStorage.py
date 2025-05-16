import copy
import json
import os
import re
from datetime import datetime, timezone
from math import floor
from typing import Optional

import mysql.connector
import redis
from mysql.connector import Error, errorcode
from DBUtils.PooledDB import PooledDB
from db.coin import Coin

from common.log import logger
from config import conf


class DBStorage:
    def __init__(self):
        curdir = os.path.dirname(__file__)
        config_path = os.path.join(curdir, "config.json")
        conf = None
        if not os.path.exists(config_path):
            logger.debug(f"[wxsop]不存在配置文件{config_path}")
        else:
            logger.debug(f"[wxsop]加载配置文件{config_path}")
            with open(config_path, "r", encoding="utf-8") as f:
                conf = json.load(f)
        self._mysql = PooledDB(
            creator=mysql.connector,  # 使用链接数据库的模块
            maxconnections=10,  # 连接池允许的最大连接数，0和None表示不限制连接数
            mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
            maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
            maxshared=3,
            # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的
            # threadsafety都为1，所有值无论设置为多少，maxcached永远为0，所以永远是所有链接都共享。
            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
            setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
            ping=0,
            # ping MySQL服务端，检查是否服务可用。如：0 = None = never, 1 = default = whenever it is requested,
            # 2 = when a cursor is created, 4 = when a query is executed, 7 = always
            host=conf["mysql_host"],
            port=conf["mysql_port"],
            user=conf["mysql_user"],
            password=conf["mysql_password"],
            database=conf["mysql_database"],
            charset='utf8'
        )
        self._redis = redis.Redis(
            host=conf["redis_host"],
            port=conf["redis_port"],
            db=0,
            decode_responses=True)

    def get_redis_conn(self):
        return self._redis

    def get_server_by_id(self,id: int):
        server_info = self._redis.hget('server_info', str(id))
        if server_info:
            logger.debug(
                f"[CHATGPT] --------------------server_info-----------------, msg={server_info}")
            return json.loads(server_info)

        conn = self._mysql.connection()
        try:
            sql_query = "SELECT id, status, name, public_ip, private_ip, admin_port FROM server WHERE id = %s LIMIT 1"
            record_tuple = (id, )
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_query, record_tuple)
                server_record = cursor.fetchone()
            if server_record:
                self._redis.hset('server_info', str(id), json.dumps(server_record))
                return server_record
            else:
                return None
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()
    
    # 查询微信账号信息
    def get_info_by_wxid(self, wxid: str):
        wx_info = self._redis.hget('wx_info', wxid)
        if wx_info:
            return json.loads(wx_info)
        conn = self._mysql.connection()
        try:
            sql_query = "SELECT id, status, port, process_id, callback, wxid, account, nickname, server_id, organization_id, agent_id, api_base, api_key, allow_list, group_allow_list, block_list, group_block_list, server_id, ctype FROM wx WHERE wxid = %s ORDER BY id DESC LIMIT 1"
            record_tuple = (wxid, )
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_query, record_tuple)
                wx_record = cursor.fetchone()
            if wx_record:
                self._redis.hset('wx_info', wxid, json.dumps(wx_record))
                return wx_record
            else:
                return None
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    def get_wainfo_by_phone(self, phone: str):
        wa_info = self._redis.hget('wa_info', phone)
        if wa_info:
            return json.loads(wa_info)
        conn = self._mysql.connection()
        try:
            sql_query = "SELECT wa_id, agent_id, cc_phone, phone_name, api_base, api_key, allow_list, group_allow_list, block_list, group_block_list FROM whatsapp WHERE cc_phone = %s LIMIT 1"
            record_tuple = (phone, )
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_query, record_tuple)
                wa_record = cursor.fetchone()
                logger.debug(f"[wx_hook] wa_record: {wa_record}")
            if wa_record:
                sql_query = "SELECT * FROM whatsapp_channel WHERE deleted_at IS NULL AND wa_id = %s AND status = 1"
                sop_node_tuple = (wa_record['wa_id'], )

                with conn.cursor(dictionary=True) as cursor:
                    cursor.execute(sql_query, sop_node_tuple)
                    channel_info = cursor.fetchone()
                    logger.debug("[wxagent] channel_info: %s" % channel_info)
            if wa_record and channel_info:
                wa_record["ak"] = channel_info["ak"]
                wa_record["sk"] = channel_info["sk"]
                wa_record["organization_id"] = channel_info["organization_id"]
                self._redis.hset('wa_info', phone, json.dumps(wa_record))
                return wa_record
            else:
                return None
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    def get_contact_by_wxid(self, wxid: str, bot_wxid: str = None):
        conn = self._mysql.connection()
        try:
            if bot_wxid:
                sql_query = "SELECT * FROM contact WHERE wxid = %s AND wx_wxid = %s ORDER BY id DESC LIMIT 1"
                record_tuple = (wxid, bot_wxid)
            else:
                sql_query = "SELECT * FROM contact WHERE wxid = %s ORDER BY id DESC LIMIT 1"
                record_tuple = (wxid, )
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_query, record_tuple)
                wx_record = cursor.fetchone()
            if wx_record:
                return wx_record
            else:
                return None
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    # 根据wx_wxid和wxid获取联系人信息
    def get_contact_by_wxwxid_wxid(self, wx_wxid: str, wxid: str = None):
        conn = self._mysql.connection()
        try:
            sql_query = "SELECT id,wx_wxid,wxid,nickname,markname,account FROM contact WHERE wx_wxid=%s AND wxid = %s LIMIT 1"
            record_tuple = (wx_wxid, wxid)
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_query, record_tuple)
                wx_record = cursor.fetchone()
            if wx_record:
                return wx_record
            else:
                return None
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()


    def get_label_tagging_by_orgid(self, orgid: int):
        label_tagging_info = self._redis.hget('label_tagging_info', str(orgid))
        if label_tagging_info:
            return json.loads(label_tagging_info)
        conn = self._mysql.connection()
        try:
            sql_query = "SELECT id, organization_id, type, conditions, action_label_add, action_label_del FROM label_tagging WHERE organization_id = %s AND deleted_at IS NULL"
            record_tuple = (orgid, )
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_query, record_tuple)
                label_tagging_record = cursor.fetchall()

            if label_tagging_record:
                new_records = []
                for record in label_tagging_record:
                    keywords = record.get('conditions')
                    if keywords:
                        standard_keywords = re.sub(r'[,、，｜\s]+', '|', keywords)
                        # 将竖线 `|` 分隔的关键词列表
                        split_keywords = standard_keywords.split('|')
                        # 转义每个关键词中的特殊字符
                        escaped_keywords = [re.escape(keyword) for keyword in split_keywords]
                        # 组合成正则表达式
                        record["conditions"] = '|'.join(escaped_keywords)
                        new_records.append(record)
                if new_records:
                    self._redis.hset('label_tagging_info', str(orgid), json.dumps(label_tagging_record))
                return new_records
            else:
                return None
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()


    # 查询接下来带匹配的回答
    def get_next_answers(self, bot_wxid: str, contact_wxid: str, contact_type: int, organization_id: int):
        conn = self._mysql.connection()
        try:
            # 在message_records表中，查询bot_wxid == selfwxid and contact_wxid == fromid contact_type == 1 source_type == 3 status == 1 的最新一条记录，按created_at字段排序
            sql_query = "SELECT * FROM message_records WHERE bot_wxid = %s AND contact_wxid = %s AND contact_type = %s AND content_type = 1 AND (source_type = 3 OR source_type = 4) AND status = 3 ORDER BY id DESC LIMIT 1"
            record_tuple = (bot_wxid, contact_wxid, contact_type)

            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_query, record_tuple)
                message_record = cursor.fetchone()
            if message_record:
                # 在sop_node表中，查询 id == message_record['sub_source_id'] stage_id == message_record['source_id'] 的记录
                if message_record['source_type'] == 3:
                    # 在message_records表中，查询bot_wxid == selfwxid and contact_wxid == fromid contact_type == 1 source_type == 3 status == 1 的最新一条记录，按created_at字段排序
                    stage_query = "SELECT * FROM sop_stage WHERE id = %s LIMIT 1"
                    with conn.cursor(dictionary=True) as cursor:
                        cursor.execute(stage_query, (message_record['source_id'], ))
                        stage_record = cursor.fetchone()
                    if stage_record:
                        task_query = "SELECT * FROM sop_task WHERE id = %s AND status = 3 AND organization_id = %s LIMIT 1"
                        with conn.cursor(dictionary=True) as cursor:
                            cursor.execute(task_query, (stage_record['task_id'], organization_id))
                            task_record = cursor.fetchone()
                        if task_record:
                            sql_query = "SELECT * FROM sop_node WHERE deleted_at IS NULL AND parent_id = %s AND stage_id = %s"
                            sop_node_tuple = (0, message_record['source_id'])
                            with conn.cursor(dictionary=True) as cursor:
                                cursor.execute(sql_query, sop_node_tuple)
                                sop_nodes = cursor.fetchall()
                                return message_record, sop_nodes, message_record['source_type'], message_record[
                                    'source_id']
                else:
                    node_query = "SELECT * FROM sop_node WHERE id = %s LIMIT 1"
                    with conn.cursor(dictionary=True) as cursor:
                        cursor.execute(node_query, (message_record['source_id'],))
                        node_record = cursor.fetchone()
                    if node_record:
                        stage_query = "SELECT * FROM sop_stage WHERE id = %s LIMIT 1"
                        with conn.cursor(dictionary=True) as cursor:
                            cursor.execute(stage_query, (node_record['stage_id'],))
                            stage_record = cursor.fetchone()
                        if stage_record:
                            task_query = "SELECT * FROM sop_task WHERE id = %s AND status = 3 AND organization_id = %s LIMIT 1"
                            with conn.cursor(dictionary=True) as cursor:
                                cursor.execute(task_query, (stage_record['task_id'], organization_id))
                                task_record = cursor.fetchone()
                            if task_record:
                                sql_query = "SELECT * FROM sop_node WHERE deleted_at IS NULL AND parent_id = %s"
                                sop_node_tuple = (message_record['source_id'],)

                                with conn.cursor(dictionary=True) as cursor:
                                    cursor.execute(sql_query, sop_node_tuple)
                                    sop_nodes = cursor.fetchall()
                                    return message_record, sop_nodes, message_record['source_type'], message_record['source_id']

            return None, None, None, None
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    # 创建一条消息记录
    def create_message_record(self, status: int, bot_wxid: str, contact_id: int, contact_type: int, contact_wxid: str, content_type: int, content: str, meta: dict, source_type: int, source_id: int, sub_source_id: int, organization_id: int) -> Optional[int]:
        conn = self._mysql.connection()
        try:
            current_utc_time = datetime.now(timezone.utc)
            formatted_time = current_utc_time.strftime('%Y-%m-%d %H:%M:%S')
            meta_str = json.dumps(meta) if isinstance(meta, dict) else meta
            sql_insert = "INSERT INTO message_records (status, bot_wxid, contact_id, contact_type, contact_wxid, content_type, content, meta, source_type, source_id, sub_source_id, organization_id, send_time, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            record_tuple = (status, bot_wxid, contact_id, contact_type, contact_wxid, content_type, content, meta_str, source_type, source_id, sub_source_id, organization_id, formatted_time, formatted_time, formatted_time)

            with conn.cursor() as cursor:
                cursor.execute(sql_insert, record_tuple)
                conn.commit()
                return cursor.lastrowid
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    # 更新消息记录
    def update_message_record(self, id: int, status: int, error_detail: str = None):
        conn = self._mysql.connection()
        try:
            current_utc_time = datetime.now(timezone.utc)
            formatted_time = current_utc_time.strftime('%Y-%m-%d %H:%M:%S')
            if status == 3:
                sql_update = "UPDATE message_records SET status = %s, send_time = %s WHERE id = %s"
                record_tuple = (status, formatted_time, id)
            elif status == 4:
                sql_update = "UPDATE message_records SET status = %s, error_detail = %s, send_time = %s WHERE id = %s"
                record_tuple = (status, error_detail, formatted_time, id)
            else:
                sql_update = "UPDATE message_records SET status = %s WHERE id = %s"
                record_tuple = (status, id)

            with conn.cursor() as cursor:
                cursor.execute(sql_update, record_tuple)
                conn.commit()
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    # 追加联系人标签
    def add_contact_label(self, contact_id: int, action_label_add: list[int], action_label_del: list[int], organization_id: int):
        conn = self._mysql.connection()
        try:
            # 从 label_relationship 表中查询 contact_id == contact_id 的记录
            sql_query = "SELECT * FROM label_relationship WHERE deleted_at IS NULL AND contact_id = %s"
            record_tuple = (contact_id,)

            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_query, record_tuple)
                label_relationships = cursor.fetchall()
                logger.debug("[wxsop] label_relationships: %s" % label_relationships)
                add_label_ids = []
                rem_label_ids = []
                contact_label_ids = []
                final_label_ids = []
                if label_relationships:
                    contact_label_ids = [label_relationship['label_id'] for label_relationship in label_relationships]
                    for add_label_id in action_label_add:
                        if add_label_id not in contact_label_ids and add_label_id not in action_label_del:
                            add_label_ids.append(add_label_id)
                            contact_label_ids.append(add_label_id)
                    # if add_label_ids:
                    #     return contact_label_ids
                else:
                    add_label_ids = copy.copy(action_label_add)
                    for add_label_id in action_label_add:
                        if add_label_id not in action_label_del:
                            add_label_ids.append(add_label_id)
                            contact_label_ids.append(add_label_id)

                for contact_label_id in contact_label_ids:
                    if contact_label_id not in action_label_del:
                        final_label_ids.append(contact_label_id)
                    else:
                        rem_label_ids.append(contact_label_id)

                logger.debug("[wxsop] final_label_ids: %s" % final_label_ids)
                for label_id in add_label_ids:
                    current_utc_time = datetime.now(timezone.utc)
                    formatted_time = current_utc_time.strftime('%Y-%m-%d %H:%M:%S')
                    try:
                        sql_insert = "INSERT INTO label_relationship (status, contact_id, label_id, organization_id, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)"
                        record_tuple = (1, contact_id, label_id, organization_id, formatted_time, formatted_time)
                        cursor.execute(sql_insert, record_tuple)
                    except mysql.connector.Error as err:
                        if err.errno == errorcode.ER_DUP_ENTRY:
                            print(f"Duplicate entry found: {err}")
                            # 这里可以选择记录日志或者执行其他操作，但不抛出异常
                        else:
                            raise err  # 如果是其他错误，重新抛出异常

                for label_id in rem_label_ids:
                    sql_delete = "DELETE FROM label_relationship WHERE contact_id = %s AND label_id = %s AND organization_id = %s"
                    record_tuple = (contact_id, label_id, organization_id)
                    cursor.execute(sql_delete, record_tuple)

                conn.commit()

                return final_label_ids
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    # 获取阶段记录
    def get_stage(self, organization_id: int):
        conn = self._mysql.connection()
        try:
            task_query = "SELECT * FROM sop_task WHERE deleted_at IS NULL AND status = 3 AND organization_id = %s"
            task_tuple = (organization_id,)
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(task_query, task_tuple)
                tasks = cursor.fetchall()

            # 遍历tasks，查询每个task下的stage
            stages = []
            for task in tasks:
                sql_query = "SELECT * FROM sop_stage WHERE task_id = %s AND deleted_at IS NULL AND status = 1"
                stage_tuple = (task['id'],)

                with conn.cursor(dictionary=True) as cursor:
                    cursor.execute(sql_query, stage_tuple)
                    stages += cursor.fetchall()

            return stages
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    # 判断发送记录是否已存在
    def check_message_record(self, contact_wxid: str, source_type: int, source_id: int, sub_source_id: int) -> bool:
        conn = self._mysql.connection()
        try:
            sql_query = "SELECT * FROM message_records WHERE contact_wxid = %s AND source_type = %s AND source_id = %s AND sub_source_id = %s"
            record_tuple = (contact_wxid, source_type, source_id, sub_source_id)

            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_query, record_tuple)
                message_record = cursor.fetchone()

            return True if message_record else False
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    def get_agent_info(self, bot_wxid: str, channel_type):
        logger.debug(f"[wx_hook] --------------------bot_wxid-----------------, msg={bot_wxid}")
        logger.debug(f"[wx_hook] --------------------channel_type-----------------, msg={channel_type}")
        conn = self._mysql.connection()
        try:
            if channel_type == "whatsapp":
                # 在message_records表中，查询bot_wxid == selfwxid and contact_wxid == fromid contact_type == 1 source_type == 3 status == 1 的最新一条记录，按created_at字段排序
                sql_query = "SELECT * FROM whatsapp WHERE deleted_at IS NULL AND cc_phone = %s ORDER BY created_at DESC LIMIT 1"
            elif channel_type == "wework_hook":
                sql_query = "SELECT * FROM xunji_service WHERE deleted_at IS NULL AND wxid = %s ORDER BY created_at DESC LIMIT 1"
            else:
                sql_query = "SELECT * FROM wx WHERE deleted_at IS NULL AND wxid = %s ORDER BY created_at DESC LIMIT 1"
            record_tuple = (bot_wxid,)

            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_query, record_tuple)
                wx_info = cursor.fetchone()
                logger.debug("[wxagent] wx_info: %s" % wx_info)
            if wx_info and wx_info['agent_id'] != 0:
                sql_query = "SELECT * FROM agent WHERE deleted_at IS NULL AND id = %s AND status = 1"
                sop_node_tuple = (wx_info['agent_id'], )

                with conn.cursor(dictionary=True) as cursor:
                    cursor.execute(sql_query, sop_node_tuple)
                    agent_info = cursor.fetchone()
                    logger.debug("[wxagent] agent_info: %s" % agent_info)
                    return agent_info
            else:
                return None
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    def add_usage(self, bot_type: int, bot_id: str, receiver_id: str, app: int, session_id: int, request: str, response: str, original_data: dict, total_tokens: int, prompt_tokens: int, completion_tokens: int, organization_id: int):
        conn = self._mysql.connection()
        try:
            current_utc_time = datetime.now(timezone.utc)
            formatted_time = current_utc_time.strftime('%Y-%m-%d %H:%M:%S')
            original_data_str = json.dumps(original_data)

            # 获取计费使用的模型和价格
            coin_util = Coin()
            response_data = original_data.get('response_data')
            model_name, price = coin_util.get_model_price(response_data)
            credits = coin_util.compute_price(price, total_tokens)
            logger.info(f"currently use model={model_name}, price={price} total_tokens={total_tokens} credits={credits}")

            sql_insert_detail = "INSERT INTO usage_detail (type, bot_id, receiver_id, app, session_id, request, response, original_data, total_tokens, prompt_tokens, completion_tokens, organization_id, model, credits, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            detail_record_tuple = (bot_type, bot_id, receiver_id, app, session_id, request, response, original_data_str, total_tokens, prompt_tokens, completion_tokens, organization_id, model_name, credits, formatted_time, formatted_time)

            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_insert_detail, detail_record_tuple)
                detail_record_id = cursor.lastrowid

                sql_query_total = "SELECT id, total_tokens FROM usage_total WHERE bot_id = %s"
                record_tuple = (bot_id,)
                cursor.execute(sql_query_total, record_tuple)
                existing_record = cursor.fetchone()

                if existing_record:
                    # 如果存在记录，则更新记录
                    sql_update_total = """UPDATE usage_total SET total_tokens = %s, end_index = %s, updated_at = %s WHERE id = %s"""
                    record_tuple = (existing_record['total_tokens'] + total_tokens, detail_record_id, formatted_time, existing_record['id'])
                    cursor.execute(sql_update_total, record_tuple)
                else:
                    # 如果不存在记录，则插入新记录
                    sql_insert_total = """INSERT INTO usage_total (type, bot_id, total_tokens, start_index, end_index, organization_id, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                    record_tuple = (bot_type, bot_id, total_tokens, 0, detail_record_id, organization_id, formatted_time, formatted_time)
                    cursor.execute(sql_insert_total, record_tuple)
            conn.commit()


            self.add_credit_usage(detail_record_id, total_tokens, organization_id, credits)
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()


    """ 这里记录积分消耗数到积分明细表里，同时在余额里扣减积分 """
    def add_credit_usage(self, nid: int, tokens: int, organization_id: int, credits):
        conn = self._mysql.connection()

        coin_util = Coin()
        try:
            current_utc_time = datetime.now(timezone.utc)
            formatted_time = current_utc_time.strftime('%Y-%m-%d %H:%M:%S')

            # 先获取之前的积分余额
            conn = self._mysql.connection()
            sql_query = "SELECT id, balance,organization_id FROM credit_balance WHERE organization_id = %s AND deleted_at IS NULL ORDER BY created_at DESC LIMIT 1"
            record_tuple = (organization_id,)
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_query, record_tuple)
                existing_record = cursor.fetchone()

            if existing_record:
                before_number = existing_record['balance']
                after_number = coin_util.subtraction(float(before_number), credits)
            else:
                before_number = 0
                after_number = 0 - credits

            sql_insert_detail = "INSERT INTO credit_usage (number, before_number, after_number, ntype, nid, `table`, organization_id, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, 'usage_detail', %s, %s, %s)"
            sql_insert_tuple = (
            credits, 0, 0, 1, nid, organization_id, formatted_time, formatted_time)

            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_insert_detail, sql_insert_tuple)

                if existing_record:
                    sql_update_total = "UPDATE `credit_balance` SET balance = %s, updated_at = %s WHERE organization_id = %s AND deleted_at IS NULL"
                    record_tuple = (after_number, formatted_time, organization_id)
                    cursor.execute(sql_update_total, record_tuple)
                else:
                    sql_update_total = "INSERT INTO `credit_balance` (balance, organization_id, created_at, updated_at) VALUES (%s, %s, %s, %s)"
                    record_tuple = (after_number, organization_id, formatted_time, formatted_time)
                    cursor.execute(sql_update_total, record_tuple)

            conn.commit()
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()



    def add_wp_chatroom(self, wx_wxid: str, chat_rooms: list[tuple]):
        conn = self._mysql.connection()
        try:
            task_query = "DELETE FROM wp_chatroom WHERE wx_wxid = %s"
            task_tuple = (wx_wxid,)
            sql_insert_detail = "INSERT INTO wp_chatroom (wx_wxid, chatroom_id, nickname, owner, avatar, member_list, show_name_list) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(task_query, task_tuple)
                cursor.executemany(sql_insert_detail, chat_rooms)
            conn.commit()
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    def add_wp_chatroom_member(self, wx_wxid: str, members: list[tuple]):
        conn = self._mysql.connection()
        try:
            task_query = "DELETE FROM wp_chatroom_member WHERE wx_wxid = %s"
            task_tuple = (wx_wxid,)
            sql_insert_detail = "INSERT INTO wp_chatroom_member (wx_wxid, wxid, nickname, avatar) VALUES (%s, %s, %s, %s)"
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(task_query, task_tuple)
                cursor.executemany(sql_insert_detail, members)
            conn.commit()
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    def create_wx_record(self, port: str, process_id: str, wxid: str, account: str, nickname: str, tel: str, head_big: str, type: int):
        conn = self._mysql.connection()
        try:
            # current_utc_time = datetime.now(timezone.utc)
            # formatted_time = current_utc_time.strftime('%Y-%m-%d %H:%M:%S')
            sql_insert = "INSERT INTO wx (`port`, `process_id`, `wxid`, `account`, `nickname`, `tel`, `head_big`, `ctype`, `allow_list`, `group_allow_list`, `block_list`, `group_block_list`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            record_tuple = (port, process_id, wxid, account, nickname, tel, head_big, type, '[]', '[]', '[]', '[]')

            with conn.cursor() as cursor:
                cursor.execute(sql_insert, record_tuple)
                conn.commit()
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    def update_wx_record(self, wxid: str, port: str, process_id: str, account: str, nickname: str, tel: str, head_big: str):
        conn = self._mysql.connection()
        try:
            # current_utc_time = datetime.now(timezone.utc)
            # formatted_time = current_utc_time.strftime('%Y-%m-%d %H:%M:%S')
            sql_update = "UPDATE wx SET `port` = %s, `process_id` = %s, `account` = %s, `nickname` = %s, `tel` = %s, `head_big` = %s WHERE `wxid` = %s"
            record_tuple = (port, process_id, account, nickname, tel, head_big, wxid)

            with conn.cursor() as cursor:
                cursor.execute(sql_update, record_tuple)
                conn.commit()
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    def create_contact_record(self, wx_wxid: str, type: int, wxid: str, account: str, nickname: str, markname: str, headimg: str, lag: str, gid: str, gname: str, organization_id: int, ctype: int, phone: str):
        conn = self._mysql.connection()
        try:
            sql_insert = "INSERT INTO contact (`wx_wxid`, `type`, `wxid`, `account`, `nickname`, `markname`, `headimg`, `lag`, `gid`, `gname`, `organization_id`, `ctype`, `phone`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            record_tuple = (wx_wxid, type, wxid, account, nickname, markname, headimg, lag, gid, gname, organization_id, ctype, phone)

            with conn.cursor() as cursor:
                cursor.execute(sql_insert, record_tuple)
                conn.commit()
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    def update_contact_record(self, wx_wxid: str, wxid: str, account: str, nickname: str, markname: str, headimg: str, lag: str, gid: str, gname: str, organization_id: int, phone: str):
        conn = self._mysql.connection()
        try:
            sql_update = "UPDATE contact SET `account` = %s, `nickname` = %s, `markname` = %s, `headimg` = %s, `lag` = %s, `gid` = %s, `gname` = %s, `organization_id` = %s, `phone` = %s WHERE `wx_wxid` = %s AND `wxid` = %s"
            record_tuple = (account, nickname, markname, headimg, lag, gid, gname, organization_id, phone, wx_wxid, wxid)

            with conn.cursor() as cursor:
                cursor.execute(sql_update, record_tuple)
                conn.commit()
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    # 获取用户的圈量配置信息
    def get_xunji_token(self, app_key: str, token: str):
        conn = self._mysql.connection()
        try:
            sql_query = "SELECT app_key, token, encoding_key, organization_id FROM xunji WHERE app_key = %s AND token=%s AND status=1 LIMIT 1"
            record_tuple = (app_key, token)
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_query, record_tuple)
                xunji_token = cursor.fetchone()
                if xunji_token:
                    return xunji_token
                else:
                    return None
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    def set_msg_id_friend_id(self, msg_id: str, friend_id: str):
        self._redis.set(f'MsgId_FriendId:{msg_id}', friend_id, ex=600)
