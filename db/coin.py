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

from common.log import logger
from config import conf

#gpt-4o-mini-2024-07-18
class Coin:
    def __init__(self):
        self.modelArray = [
            "o1",
            "gpt-4o",
            "gpt-4.1",
            "o3-mini",
            "moonshot-v1-32k",
            "deepseek-r1",
            "moonshot-v1-8k",
            "gpt-4.1-mini",
            "gpt-3.5-turbo",
            "qwen-max",
            "doubao1.5-pro-256k",
            "deepseek-v3",
            "qwq-32b-preview",
            "gpt-4o-mini",
            "qwen2.5-14b-instruct-1m",
            "gpt-4.1-nano",
            "doubao1.5-pro",
            "doubao1.5-pro-32k",
            "chatglm3",
            "qwen-turbo",
            "doubao1.5-lite-32k",
        ]
        self.priceArray = [
            0.0001,
            0.00001667,
            0.00001333,
            0.00000733,
            0.00000548,
            0.00000365,
            0.00000274,
            0.00000267,
            0.0000025,
            0.00000219,
            0.00000205,
            0.00000183,
            0.00000137,
            0.000001,
            0.00000068,
            0.00000067,
            0.00000046,
            0.00000046,
            0.00000023,
            0.00000014,
            0.00000014,
        ]


    # 根据模型价格和token数，计算token消耗的积分数
    def get_model_price(self, response_data):
        responseData = response_data.get('responseData')
        logger.info(f"In coin.py responseData={responseData}")

        # 先获取所有本次响应里所有的model
        model_array = []
        model = response_data.get('model')
        if model is not None and model != '':
            model_array.append(model.lower())

        if responseData is not None:
            for res in responseData:
                model_name = res.get('model')
                logger.info(f"model_name={model_name}")
                if model_name is None or model_name == '':
                    continue
                else:
                    model_array.append(model_name.lower())

        # logger.info(f"In coin.py model_array={model_array} len={len(model_array)}")


        # 按价格从高到低检查响应里是否用到了，如果有则使用该价格
        if len(model_array) > 0:
            for i,model_name in enumerate(self.modelArray):
                if model_name in model_array:
                    return model_name, self.priceArray[i]


        # 如果模型里带日期，这时候要在筛选一次，比如 gpt-4.1-mini-2024-07-18 其实应该匹配到 gpt-4.1-mini
        # 对模型名数组按名字长度排序，然后按长到短匹配
        sorted_modelArray = sorted(self.modelArray, key=len, reverse=True)
        # logger.info(f"sorted_modelArray={sorted_modelArray}")
        for model in sorted_modelArray:
            for model_name in model_array:
                match = re.search(re.escape(model), model_name, flags=re.IGNORECASE)
                if match:
                    logger.info(f"In coin.py the given model_name: {model_name} match: {match.group()}")
                    return model, self.getPriceByModel(model)

        # 最后返回最高的价格
        return self.modelArray[0], self.priceArray[0]


    # 根据价格和tokens计算积分数
    def compute_price(self, price, tokens):
        result = price * tokens * 1000000

        return round(result / 1000000, 6)


    # 精简小数
    def subtraction(self, n1:float, n2:float):
        number1 = n1*1000000
        number2 = n2*1000000
        return floor(number1-number2)/1000000


    # 根据模型名称获取价格
    def getPriceByModel(self, model):
        for i, model_name in enumerate(self.modelArray):
            if model_name == model:
                return self.priceArray[i]