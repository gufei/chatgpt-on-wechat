from typing import Optional

import mysql.connector
from mysql.connector import Error
from DBUtils.PooledDB import PooledDB
from config import conf


class DBStorage:
    def __init__(self,
                 host: str,
                 port: int,
                 user: str,
                 password: str,
                 database: str):
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
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset='utf8'
        )

    # 查询接下来带匹配的回答
    def get_next_answers(self, bot_wxid: str, contact_wxid: str, contact_type: int):
        conn = self._mysql.connection()
        try:
            # 在message_records表中，查询bot_wxid == selfwxid and contact_wxid == fromid contact_type == 1 source_type == 3 status == 1 的最新一条记录，按created_at字段排序
            sql_query = "SELECT * FROM message_records WHERE bot_wxid = %s AND contact_wxid = %s AND contact_type = %s AND source_type = 3 AND status = 3 ORDER BY created_at DESC LIMIT 1"
            record_tuple = (bot_wxid, contact_wxid, contact_type)

            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_query, record_tuple)
                message_record = cursor.fetchone()

            if message_record:
                # 在sop_node表中，查询 id == message_record['sub_source_id'] stage_id == message_record['source_id'] 的记录
                sql_query = "SELECT * FROM sop_node WHERE parent_id = %s AND stage_id = %s"
                sop_node_tuple = (message_record['sub_source_id'], message_record['source_id'])

                with conn.cursor(dictionary=True) as cursor:
                    cursor.execute(sql_query, sop_node_tuple)
                    sop_nodes = cursor.fetchall()
                    return message_record, sop_nodes

            return None, None
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    # 创建一条消息记录
    def create_message_record(self, status: int, bot_wxid: str, contact_id: int, contact_type: int, contact_wxid: str, content_type: int, content: str, source_type: int, source_id: int, sub_source_id: int) -> Optional[int]:
        conn = self._mysql.connection()
        try:
            sql_insert = "INSERT INTO message_records (status, bot_wxid, contact_id, contact_type, contact_wxid, content_type, content, source_type, source_id, sub_source_id, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), NOW())"
            record_tuple = (status, bot_wxid, contact_id, contact_type, contact_wxid, content_type, content, source_type, source_id, sub_source_id)

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
            if status == 3:
                sql_update = "UPDATE message_records SET status = %s, send_time = NOW() WHERE id = %s"
                record_tuple = (status, id)
            elif status == 4:
                sql_update = "UPDATE message_records SET status = %s, error_detail = %s, send_time = NOW() WHERE id = %s"
                record_tuple = (status, error_detail, id)
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
    def add_contact_label(self, contact_id: int, label_ids: list[int]):
        conn = self._mysql.connection()
        try:
            # 从 label_relationship 表中查询 contact_id == contact_id 的记录
            sql_query = "SELECT * FROM label_relationship WHERE contact_id = %s"
            record_tuple = (contact_id,)

            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_query, record_tuple)
                label_relationships = cursor.fetchall()

                if label_relationships:
                    contact_label_ids = [label_relationship['label_id'] for label_relationship in label_relationships]
                    add_label_ids = []
                    for label_id in label_ids:
                        if label_id not in contact_label_ids:
                            add_label_ids.append(label_id)
                    if add_label_ids:
                        return contact_label_ids
                else:
                    add_label_ids = label_ids
                    contact_label_ids = []

                for label_id in add_label_ids:
                    sql_insert = "INSERT INTO label_relationship (status, contact_id, label_id, created_at, updated_at) VALUES (%s, %s, %s, NOW(), NOW())"
                    record_tuple = (1, contact_id, label_id)
                    cursor.execute(sql_insert, record_tuple)
                    contact_label_ids.append(label_id)
                conn.commit()

                return contact_label_ids
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    # 获取阶段记录
    def get_stage(self):
        conn = self._mysql.connection()
        try:
            sql_query = "SELECT * FROM sop_stage WHERE deleted_at IS NULL AND status = 1"

            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_query)
                stages = cursor.fetchall()

            return stages
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            conn.rollback()
        finally:
            conn.close()

    # 判断发送记录是否已存在
    def check_message_record(self, contact_wxid: str, source_type: int, source_id: str, sub_source_id: str) -> bool:
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