import requests
import json
import datetime
from .const_value import initialApiParams

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

class WeatherAPI(object):
    """通过API查询天气的类.
    """

    __formatWeather = ["天气：","温度：","最后更新时间："]  #输出格式
    def __init__(self,cityEnNameFile):
        self.result = {} # 存放有意义的结果
        self.cityEnName = [] # 初始化城市英文名字典
        self.loadCityList(cityEnNameFile)
        self.history = []

    def getWeather(self,location):
        APIParamsDict = initialApiParams(location)
        for k,v in APIParamsDict.items():
            r = requests.get(v['API'], params=v['params'], timeout=10)
            d ={}
            json2list(d,json.loads(r.text),str_key=k)
            temp = str(d.get(v['strTemp'])) + " C"  #??? 华摄度怎么办？？？
            default_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.result[k] =  dict(zip(self.__formatWeather,
                [d.get(v['text']), temp, d.get(v['time'], default_time)]))
        self.history.append(location)
        self.history.append(self.result)

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

if __name__ == '__main__':
    w = WeatherAPI('cityEnName.txt')
    w.getWeather('beijing')
    print(w.result)
