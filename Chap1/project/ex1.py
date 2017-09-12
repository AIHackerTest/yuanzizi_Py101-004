#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Program name: Bulls And Cows Advanced Edition
Author: Yuanzizi
Github: https://github.com/Yuanzizi/
Edition：v x.x
Edit date: 2017.08.xx
Descrition:
    ------------------------------------------------
    输入城市名，返回该城市的天气数据；
    输入指令，打印帮助文档（一般使用 h 或 help）；
    输入指令，退出程序的交互（一般使用 quit 或 exit）；
    在退出程序之前，打印查询过的所有城市。

    PS: 所用天气数据见 weather_info.txt 文件
    -------------------------------------------------
"""

def initial_dict(input_file_path='', str_split=' '):
    """从文件中读取key：value 到 db 字典中并返回

    Args:
        input_file_path: 文件的路径, 文件是按照key：values 定义的文本文件
        str_split: key:values  的分割字符，缺省是空格.

    Returns:
        返回一个dict 类型，比如
            {'北京':'晴天','天津':'多云'}

    Raises:
        FileNotFoundError: 文件没找到，给出提示
    """

    db = {} # 初始化字典
    try:
        with open(input_file_path, encoding='utf-8') as f:
            for line in f:
                db[line.split(str_split)[0]] = line.split(str_split)[1].strip('\n')
    except FileNotFoundError:
        print("文件无法找到，请确认路径和文件名正确.......")

    return db

def retrieve_weather_info(input_file_path):
    """
    用更简洁的代码实现 从文件中读取key：value 到 db 字典中并返回
    """
    weather_info = {}
    with open(input_file_path,"r",624,'utf-8') as file:
        lis = [list(x.split(",")) for x in list(file)]
        weather_info = dict(lis)
    return weather_info

def search_city_weather(db):
    """在 db 字典中查找城市对应的天气

    Args:
        db: 包含 city：weather 定义的字典

    """
    history = [] # 存放查找记录
    help =  """
            输入城市名，返回该城市的天气数据；
            输入指令，打印帮助文档（一般使用 h 或 help）；
            输入指令，退出程序的交互（一般使用 quit 或 exit）；
            在退出程序之前，打印查询过的所有城市。
            """

    while len(db) > 0 :
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

        elif str_input in db:
            print (db.get(str_input))
            history.append(str_input + ":"+ db.get(str_input))

        else:
            print("找不到你查找的城市。。。。")
            history.append(str_input + ": 找不到")


def main():
    db = {} # 存放城市和天气的字典
    db = initial_dict('weather_info.txt',',')
    search_city_weather(db)

if __name__ == '__main__':
    main()
