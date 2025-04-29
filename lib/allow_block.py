import json
from common.log import logger

def check_allow_or_block_list(context, wxinfo):
    block_list = wxinfo.get('block_list')
    if block_list is None:
        block_list = '[]'
    block_list = json.loads(block_list)

    allow_list = wxinfo.get('allow_list')
    if allow_list is None:
        allow_list = '[]'
    allow_list = json.loads(allow_list)
    # 是否禁用所有群
    if context['isgroup']:
        group_block_list = wxinfo.get('group_block_list')
        if group_block_list is None:
            group_block_list = '[]'
        group_block_list = json.loads(group_block_list)
        logger.info(f"[check_allow_or_block_list]isgroup={context['isgroup']}, group_block_list={group_block_list}")
        logger.info(f"[check_allow_or_block_list]all_in_block_list={'ALL' in group_block_list}, group_in_block_list={str(context['receiver']) in group_block_list}")
        if group_block_list and ("ALL" in group_block_list or str(context['receiver']) in group_block_list):
            logger.debug(
                f"[CHATGPT] --------------------已禁用改群或所有群-----------------")
            return False
    # 是否禁用所有用户
    elif block_list and ("ALL" in block_list or str(context['session_id']) in block_list):
        logger.debug(
            f"[CHATGPT] --------------------已禁用当前用户或所有用户-----------------")
        return False
    # 当没有允许所有群时
    if context['isgroup']:
        group_allow_list = wxinfo.get('group_allow_list')
        if group_allow_list is None:
            group_allow_list = '[]'
        group_allow_list = json.loads(group_allow_list)
        if group_allow_list and len(group_allow_list) > 0:
            # 是否允许当前群
            if "ALL" not in group_allow_list and context['receiver'] not in group_allow_list:
                logger.debug(
                    f"[CHATGPT] --------------------群不在白名单-----------------")
                return False
    # 当没有允许所有用户时
    elif allow_list and len(allow_list) > 0:
        # 是否允许当前用户
        if "ALL" not in allow_list and str(context['session_id']) not in allow_list:
            logger.debug(
                f"[CHATGPT] --------------------用户不在白名单-----------------")
            return False

    return True