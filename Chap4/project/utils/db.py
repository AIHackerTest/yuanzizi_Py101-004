#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sqlite3
import datetime

conn = sqlite3.connect('weather.db')
c = conn.cursor()
sql_create_db = """
    create table if not exists T_Weather_LOG(
        id integer primary key autoincrement unique not null, locationtext, text text, temp float, updatetime datetime
        );
    create table if not exists T_Search_LOG(
        id integer primary key autoincrement unique not null, username varchar(20), resultkey integer, searchtime datetime
        );
    create table if not exists T_User(
        id integer primary key autoincrement unique not null, username varchar(20), password varchar(20), regtime datetime
        );
    """
c.executescript( sql_create_db)
conn.close()
