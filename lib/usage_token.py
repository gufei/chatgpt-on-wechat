from app import db_storage
from common.log import logger


def usage_storage(bot_type: int, bot_id: str, receiver_id: str, app: int, session_id: int, request_data: dict, response_data: dict, organization_id: int):
    total_tokens = 0
    prompt_tokens = 0
    # completion_tokens = 0
    detail = response_data.get("responseData")
    request = request_data["messages"][-1]["content"]
    response = response_data["choices"][0]["message"]["content"]
    original_data = {
        "request_data": request_data,
        "response_data": response_data
    }
    if detail:
        for item in detail:
            logger.info("[ChatGPT] item={}".format(item))
            token = item.get("tokens")
            if token:
                total_tokens += token

        if total_tokens:
            db_storage.add_usage(bot_type, bot_id, receiver_id, app, session_id, request, response, original_data, total_tokens, prompt_tokens, total_tokens, organization_id)
    else:
        usage = response_data.get("usage")
        if usage:
            total_tokens = usage.get("total_tokens")
            prompt_tokens = usage.get("prompt_tokens")
            completion_tokens = usage.get("completion_tokens")
            db_storage.add_usage(bot_type, bot_id, receiver_id, app, session_id, request, response, original_data, total_tokens, prompt_tokens,completion_tokens, organization_id)


