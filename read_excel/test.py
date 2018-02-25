# -*- coding: utf-8 -*-
__author__ = 'XMM'

import sqlite3 as lite
from pandas.io import sql

cnx = lite.connect('data.db')

#if_exists 預設為 failed 新建一個 Daily_Record table 並寫入 sql_df資料
sql.write_frame(sql_df, name='Daily_Record', con=cnx)

#if_exists 選擇 replace 是Daily_Record 這個 table 已存在資料庫
#將Daily_Record 表刪除並重新創建 寫入 sql_df 的資料
sql.write_frame(sql_df, name='Daily_Record', con=cnx, if_exists='replace')

'''
import datetime
now = datetime.datetime.now()
delta = datetime.timedelta(days=-1)
n_days = now + delta
print n_days.strftime('%Y%m%d')[4:]
'''


'''
#coding:UTF-8
import time

#获取当前时间
time_now = int(time.time())
#转换成localtime
time_local = time.localtime(time_now)
#转换成新的时间格式(2016-05-09 18:59:20)
dt = time.strftime("%m%d",time_local)

print dt
'''