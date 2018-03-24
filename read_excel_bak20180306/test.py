# -*- coding: utf-8 -*-
__author__ = 'XMM'

import pandas as pd
import datetime
import sqlite3 as lite
from pandas.io import sql

def return_o32_data():
    o32_file = 'D:/fixed_income/综合信息查询_组合证券gs0214.xls'
    o32_data = pd.read_excel(o32_file)
    o32_filter_data = o32_data[[u'组合名称',u'证券代码',u'证券名称',u'交易市场',u'投资类型',u'证券类别']]
    return o32_filter_data

def write_data_to_db(from_data= pd.DataFrame(),table_name = 'temptable'):
    cnx = lite.connect('data.db')
    #if_exists 預設為 failed 新建一個 Daily_Record table 並寫入 sql_df資料
    #sql(from_data, name=table_name, con=cnx)
    sql.to_sql(from_data, name=table_name, con=cnx,if_exists='replace',index=False)

if __name__ == '__main__':
    o32_result = return_o32_data()
    #print (o32_result)
    write_data_to_db(o32_result,'o32_result')
    print (sql.read_sql('select * from o32_result', con=lite.connect('data.db'), index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None,
                   chunksize=None))

'''
cnx = lite.connect('data.db')

#if_exists 預設為 failed 新建一個 Daily_Record table 並寫入 sql_df資料
sql.write_frame(sql_df, name='Daily_Record', con=cnx)

#if_exists 選擇 replace 是Daily_Record 這個 table 已存在資料庫
#將Daily_Record 表刪除並重新創建 寫入 sql_df 的資料
sql.write_frame(sql_df, name='Daily_Record', con=cnx, if_exists='replace')
'''


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