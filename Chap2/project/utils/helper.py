import sys
import time
import requests
import json
from .const_value import *
from .const_value import API_OWM, API_Yahoo

def printMap(obj,i=-1):
    """输出 Map 格式
    Arug:
        obj:
            递归对象，可以是dict，list，str
        i：
            格式计数器，为了输出缩进
    """
    i += 1
    if isinstance(obj,dict) : #使用isinstance检测数据类型
        for k,v in obj.items():
            print('\t'*i,"%s : " %(k))
            printMap(v,i) #自我调用实现无限遍历
    elif isinstance(obj,list):
        for item in obj:
            printMap(item,i)
    else:
        print('\t'*i,obj)

def json2list(d,obj,i=-1,str_key=""):
    """格式化 JSON 包为 1唯 的列表list
    Arug:
        d:
            将JSON 存储为 没有嵌套 的dict
        obj:
            递归对象，可以是dict，list，str
        i：
            格式计数器，为了输出缩进
        str_key：
            存储键名的字符串
    """
    i += 1
    if isinstance(obj,dict) : #使用isinstance检测数据类型
        for k,v in obj.items():
            # print('\t'*i,"%s : " %(k))
            str_key1 = str_key +"_" + k
            json2list(d,v,i,str_key1) #自我调用实现无限遍历
    elif isinstance(obj,list):
        for item in obj:
            json2list(d,item,i,str_key)
    else:
        # print('\t'*i,obj)
        # print(str_key)
        d[str_key] = obj

def loadCityList(input_file_path='', str_split=' '):
    """从文件中读取key：value 到 db 字典中并返回

    Args:
        input_file_path: 文件的路径, 文件是按照key：values 定义的文本文件
        str_split: key:values  的分割字符，缺省是空格.

    Returns:
        返回 2 个 list 类型，比如
            ['北京','天津'] , ['beijing','tiajin']

    Raises:
        FileNotFoundError: 文件没找到，给出提示
    """

    cityCnName = []
    cityEnName = [] # 初始化字典
    try:
        with open(input_file_path, encoding='utf-8') as f:
            for line in f:
                cityCnName.append(line.split(str_split)[0])
                cityEnName.append(line.split(str_split)[1].strip('\n').lower())
    except FileNotFoundError:
        print("文件无法找到，请确认路径和文件名正确.......")

    # print(cityCnName, cityEnName)
    return cityCnName, cityEnName


def search_city_weather(cityCnName, cityEnName):
    """查找天气的主函数

        Args:
            cityCnName, cityEnName: 包含 city name 定义的字典
    """
    history = [] # 存放查找记录
    help =  """
            输入城市名，返回该城市的天气数据；
            输入指令，打印帮助文档（一般使用 h 或 help）；
            输入指令，退出程序的交互（一般使用 quit 或 exit）；
            在退出程序之前，打印查询过的所有城市。
            """

    while len(cityEnName) > 0 :
        str_input = input("请输入你要查询的城市：")
        if str_input in ["exit",'quit','q']:
            print ("----你的查询记录是：----\n ")
            for x in history:
                print (x)
            print ("\n---------------------- ")
            break

        elif str_input in ['help','h','?']:
            print(help)

        elif str_input in ["history",'his']:
            print ("----你的查询记录是：----\n ")
            for x in history:
                print (x)
            print ("\n----------------------- ")

        elif str_input in cityCnName or str_input in cityEnName:
            w = GetWeatherInfo(str_input)
            printMap(w.result)
            history.append(str_input + " >>>>>>\n\t "+ str(w.result))

        else:
            print("找不到你查找的城市。。。。")
            history.append(str_input + ": 找不到")




class GetWeatherInfo(object):
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """
    result = {} # 存放有意义的结果
    __formatWeather = ["天气：","温度：","最后更新时间："]
    def __init__(self,location):
        self.result.clear()
        self.fetch_XZ_weather(location)
        self.fetch_OWM_weather(location)
        self.fetch_Yahoo_weather(location)
        # print(self.reslut)

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
                                      [d['XZ_results_now_text'],
                                       temp,
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
