#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sqlite3
import datetime

conn = sqlite3.connect('weather.db')
c = conn.cursor()
sql_create_table_weather = """
    create table if not exists T_Weather_LOG(
        id integer primary key autoincrement unique not null, location text, text text, temp float, updatetime datetime
        );
        """
sql_create_table_search = """
    create table if not exists T_Search_LOG(
        id integer primary key autoincrement unique not null, username varchar(20), resultkey integer, searchtime datetime
        );
        """
sql_create_table_user = """
    create table if not exists T_User(
        id integer primary key autoincrement unique not null, username varchar(20), password varchar(20), regtime datetime
        );
        """
c.execute(sql_create_table_weather)
c.execute(sql_create_table_search)
c.execute(sql_create_table_user)
sql_insert = "insert into T_WEATHER_LOG(location,text,temp) values (?,?,?)"
c.execute(sql_insert,('shantou','多云','30'))
sql_insert = "insert into T_Search_LOG(username,resultkey,searchtime) values (?,?,?)"
c.execute(sql_insert,('yuanrzi',99,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  ))
sql_insert = "insert into T_User (username, password, regtime) values (?,?,?)"
c.execute(sql_insert, ('zhangsan','123',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
conn.commit()

location = ('shantou',)
print (c.execute("Select * from T_WEATHER_LOG where location=?", location))
print(c.rowcount)
print(c.fetchall())
conn.close()
