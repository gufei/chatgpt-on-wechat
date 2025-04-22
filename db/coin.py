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
        ]
        self.priceArray = [
            12.1,
            12.5,
            12.5,
            12.5,
            12.5,
            12.5,
        ]

    # 根据模型名获取模型价格
    def get_model_price(self, model_name:str):
        for i in range(len(self.modelArray)):
            if self.modelArray[i] == model_name:
                return self.priceArray[i]

        return 12.5

    # 根据模型价格和token数，计算token消耗的积分数
    def transfer(self, model_name:str, tokens) :
        price = self.get_model_price(model_name)
        price_round = float(tokens) * 1000000 / float(price)
        return round(price_round / 1000000, 6)
