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
    Log:
        V1.1 2017-9-1
        + 增加图片 ok
        + 优化帮助函数 ok
        + 优化历史函数 ok
        + 优化index 页面布局 ok
        V1.2 2017-9-2
        + 调整文件目录 ok
        + 抽象weather 类里面的函数 ok
        + 使用bootstrap 模板美化index 页面

"""

from flask import Flask
from flask import request
from flask import render_template  # Jinja2 模板
from utils.helper import WeatherAPI
from utils.pinyin import PinYin
# history = []
app = Flask(__name__)
w = WeatherAPI('../resource/cityEnName.txt')
cityEnName = PinYin("../resource/word.data")
cityEnName.load_word()

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        str_input = request.form['cityname']
        location = cityEnName.hanzi2pinyin(string=str_input)
        order = request.form.get('order')
        if order == 'quit':
            return render_template('quit.html', his=w.history)
        elif order == 'history':
            return render_template('index.html', his=w.history)
        elif order == 'help':
            return render_template('index.html', help=True)
        elif order == 'search' and location in w.cityEnName:
            w.getWeather(location)
            return  render_template('index.html', location=location,
                result=w.result)
        else:
            msg = "Your Input: %s is error." % location
            return render_template('index.html', message=msg)
    else:
        return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
