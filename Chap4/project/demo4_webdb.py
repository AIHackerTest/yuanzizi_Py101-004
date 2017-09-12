#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Program name: Get the Weather from API & Store in db
    Author: Yuanzizi
    Github: https://github.com/Yuanzizi/
    Edition：v 0.2
    Edit date: 2017.09.07
    Descrition:
        ------------------------------------------------
        基础任务：完成一个网页版天气查询程序，实现以下功能：
            基本功能
                输入城市名，获取该城市最新天气情况
                点击「帮助」，获取帮助信息
                点击「历史」，获取历史查询信息
            扩展功能
                使用 SQLite 存储天气数据
                用户可通过 Web 页面的用户更正按钮，更正天气数据到数据库
                如果在5分钟以内查询相同的数据, 不用通过 API 访问远程数据源（较难，选做）
                可记录多个用户不同的查询历史（较难，选做）
        进阶任务：使用 Flask 的扩展 Flask-SQLAlchemy 来替代 sqlite3 模块，和 Flask 更好地结合。

        PS: 天气数据来自网络API,    部署在命令行界面
        -------------------------------------------------
    Log:
        V0.1 2017-9-7
        + 调试复用 chap3 的函数是否可用 ok
        + 引入 sqlite3 OK
        + 定时爬取心知天气存在数据库中
        + 调整查询接口
        + 增加用户注册登录
        + 增加处理不同用户的查询历史功能


"""

from flask import Flask
from flask import request
from flask import render_template  # Jinja2 模板
from utils.helper import WeatherAPI
from utils.pinyin import PinYin
import sqlite3

app = Flask(__name__)
w = WeatherAPI('../resource/cityEnName.txt')
cityEnName = PinYin("../resource/word.data")
cityEnName.load_word()
conn = sqlite3.connect('weather.db')



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
            result = w.getWeather(location)
            return  render_template('index.html', location=location,
                result=result)
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
