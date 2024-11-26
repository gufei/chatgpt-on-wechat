from app import db_storage
from common.log import logger


def usage_storage(bot_type: int, bot_id: str, receiver_id: str, app: int, session_id: int, request: dict, response: dict, organization_id: int):
    total_tokens = 0
    prompt_tokens = 0
    completion_tokens = 0
    detail = response.get("responseData")
    if detail:
        for item in detail:
            logger.info("[ChatGPT] item={}".format(item))
            token = item.get("tokens")
            if token:
                total_tokens += token

        if total_tokens:
            db_storage.add_usage(bot_type, bot_id, receiver_id, app, session_id, detail, response["choices"][0]["message"]["content"], total_tokens, prompt_tokens, total_tokens, organization_id)
    else:
        usage = response.get("usage")
        if usage:
            total_tokens = usage.get("total_tokens")
            prompt_tokens = usage.get("prompt_tokens")
            completion_tokens = usage.get("completion_tokens")
            db_storage.add_usage(bot_type, bot_id, receiver_id, app, session_id, request, response["choices"][0]["message"]["content"], total_tokens, prompt_tokens,completion_tokens, organization_id)


