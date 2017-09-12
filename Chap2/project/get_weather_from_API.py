#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Program name: Get the Weather from API
Author: Yuanzizi
Github: https://github.com/Yuanzizi/
Edition：v 0.2
Edit date: 2017.08.21
Descrition:
    ------------------------------------------------
    输入城市名，返回该城市的天气数据；
    输入指令，打印帮助文档（一般使用 h 或 help）；
    输入指令，退出程序的交互（一般使用 quit 或 exit）；
    在退出程序之前，打印查询过的所有城市。

    PS: 天气数据来自网络API
    -------------------------------------------------
"""


import requests
import json
import utils.const_value
# from utils.helper import fetch_XZ_weather,fetch_OWM_weather
# from utils.helper import fetch_Yahoo_weather, getLocation
# # from utils.const_value import API_Yahoo
from utils.helper import loadCityList, search_city_weather


if __name__ == '__main__':
    cityCnName, cityEnName = loadCityList("../resource/cityname.txt",str_split="\t")
    search_city_weather(cityCnName, cityEnName)
