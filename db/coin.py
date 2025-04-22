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


class Coin:
    def __init__(self):
        self.modelArray = [
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-0301",
            "gpt-3.5-turbo-0613",
            "gpt-3.5-turbo-16k",
            "gpt-3.5-turbo-16k-0613",
            "gpt-4",
            "embedding-2",
            "deepseek-V3"
        ]
        self.priceArray = [
            12.5,
            12.4,
            12.3,
            12.2,
            12.1,
            12.0,
            11.9,
            11.8
        ]


    # 根据模型价格和token数，计算token消耗的积分数
    def get_model_price(self, response_data) :
        logger.info(f"In coin.py responseData.responseData={response_data.get('responseData')}")

        # 先获取所有本次响应里所有的model
        model_array = []
        for res in response_data.get('responseData'):
            model_name = res.get('model')
            logger.info(f"model_name={model_name}")
            if model_name is None or model_name == '':
                continue
            else:
                model_array.append(model_name.lower())

        # logger.info(f"in responseData contain models={model_array}")

        # 按价格从高到低检查响应里是否用到了，如果有则使用该价格
        for i,model_name in enumerate(self.modelArray):
            if model_name in model_array:
                price = self.priceArray[i]
                # logger.info(f"Finally we choose model_name={model_name} price={price} tokens={tokens}")
                return model_name, price

        # logger.info(f"At last we choose the 1st(default) price={self.priceArray[0]} tokens={tokens}")
        # return self.compute_price(self.priceArray[0], tokens)
        return self.modelArray[0], self.priceArray[0]

    # 根据价格和tokens计算积分数
    def compute_price(self, price, tokens):
        price_round = float(tokens) * 1000000 / float(price)
        return round(price_round / 1000000, 6)

    # 精简小数
    def subtraction(self, n1:float, n2:float):
        number1 = n1*1000000
        number2 = n2*1000000
        return floor(number1-number2)/1000000