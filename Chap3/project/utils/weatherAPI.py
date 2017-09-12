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
import sys
import time
import requests
import json
import const_value

# from .const_value import API_OWM, API_Yahoo
from helper import json2list

class WeatherAPI(object):
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    __formatWeather = ["天气：","温度：","最后更新时间："]
    def __init__(self):
        self.result = {} # 存放有意义的结果
        self.cityEnName = [] # 初始化字典
        self.loadCityList('cityEnName.txt')

    def getWeather(self,location):
        self.fetch_XZ_weather(location)
        self.fetch_OWM_weather(location)
        self.fetch_Yahoo_weather(location)


    def loadCityList(self,input_file_path=''):
        """从文件中读取字符串 进行分割 存入list 中并返回
        """
        try:
            with open(input_file_path, encoding='utf-8') as f:
                for line in f:
                    self.cityEnName.append(line.strip('\n').lower())
        except FileNotFoundError:
            print("文件无法找到，请确认路径和文件名正确.......")

        # print(cityCnName, cityEnName)
        # return cityEnName

    def fetch_XZ_weather(self,location):
        r = requests.get(API_XZ, params={
                                            'key': KEY_XZ,
                                            'location': location,
                                            'language': LANGUAGE_XZ,
                                            'unit': UNIT_XZ
                                        }, timeout=10)
        d ={}
        json2list(d,json.loads(r.text),str_key="XZ")
        temp = str(d['XZ_results_now_temperature']) + " C"
        self.result["XZ"] =  dict(zip(self.__formatWeather,
            [d['XZ_results_now_text'], temp,
                                       d['XZ_results_last_update']]
                                      )
                                 )
        # print(self.result)

    def fetch_OWM_weather(self,location):

        r = requests.get(API_OWM, params={
                                            'appid': APPID_OWM,
                                            'q': location,
                                            'units':UNIT_OWM
                                          }, timeout=10)
        d ={}
        json2list(d,json.loads(r.text),str_key="OWP")
        # print(d)
        temp = str(d['OWP_main_temp']) + " C"
        self.result["OWP"] = dict(zip(self.__formatWeather,[d['OWP_weather_main'], temp, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())]))
        # print(self.result)

    def fetch_Yahoo_weather(self,location):
        ysl = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='" + location + "')"
        r = requests.get(API_Yahoo, params={
                                            'format':'json',
                                            'q': ysl,
                                          }, timeout=10)
        # print(result.text)
        d ={}
        json2list(d,json.loads(r.text),str_key="Yahoo")
        # print(d)
        temp =  str(float('%.2f' %((int(d['Yahoo_query_results_channel_item_condition_temp'])-32)*5/9))) + ' C' # 华摄度转换为摄氏度
        self.result["Yahoo"] = dict(zip(self.__formatWeather,
                                        [d['Yahoo_query_results_channel_item_condition_text'],
                                        temp, d['Yahoo_query_results_channel_item_condition_date']]))
        # print(self.result)

if __name__ == '__main__':
    w = WeatherAPI()
    w.getWeather('beijing')
    print(w.result)
