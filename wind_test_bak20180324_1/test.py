#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 21:16
# @Author  : XMM
# @Site    : 
# @File    : test.py
# @Software: PyCharm

import datetime
import pandas as pd
import sqlite3 as lite
from pandas.io import sql

#dt=datetime.now()
#delta = dt.strftime('%Y%m%d')


def get_lastday(n=-2):
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=n)
    n_days = now + delta
    day = n_days.strftime('%Y%m%d')
    return day

#读取固收部门的数据
def return_gs_data():
    gs_file = 'D:/fixed_income/' + get_lastday() + '/' + u'固收部数据报送' + get_lastday() + '.xlsx'
    gs_data = pd.read_excel(gs_file,header=3)
    gs_filter_data = gs_data[[u'证券名称',u'证券代码',u'证券类别',u'市场',u'求和项:持仓数量',u'求和项:净价成本',\
                              u'求和项:公允价值（净价）',u'求和项:浮动盈亏（净价）',u'求和项:资本利得',\
                              u'求和项:利息收入',u'求和项:总体盈亏',u'证券面值',u'证券总面值',u'万得证券分类', \
                              u'全价总市值']]
    gs_filter_data.columns = [u'证券名称',u'证券代码',u'证券类别',u'市场',u'持仓数量',u'净价成本',u'公允价值',u'浮动盈亏',\
                              u'资本利得',u'利息收入',u'总体盈亏',u'证券面值',u'证券总面值',u'万得证券分类', \
                              u'全价总市值']
    gs_filter_data['日期'] = get_lastday()
    gs_filter_data[u'证券类别'] = gs_filter_data[u'证券类别'].fillna(method='pad')
    gs_filter_data[u'市场'] = gs_filter_data[u'市场'].fillna(method='pad')
    return gs_filter_data

def write_data_to_db(from_data= pd.DataFrame(),table_name = 'temptable'):
    cnx = lite.connect('data.db')
    sql.to_sql(from_data, name=table_name, con=cnx,if_exists='replace',index=False)

df = return_gs_data()

def juage_suffix(df):
    if df[u'市场'] == '上交所':
        return '.SH'
    if df[u'市场'] == '深交所':
        return '.SZ'
    else:
        return '.IB'

df[u'证券后缀'] = df.apply(lambda r:juage_suffix(r),axis=1)

df['code']  = df['证券代码'].astype(str)  + df.apply(lambda r:juage_suffix(r),axis=1)

#print(df.dtypes)

#print(df.head(3))


from WindPy import w
w.start();
df_tmp = pd.DataFrame()
for code in df['code']:
    #债券最新面值
    latest_par = w.wsd(code, "latestpar", "ED-0D", get_lastday(), "")
    df_code = latest_par.Codes[0]
    code_latest_par = latest_par.Data[0][0]
    #wind债券一级分类
    windl1_type = w.wss(code, "windl1type")
    code_windl1_type = windl1_type.Data[0][0]
    #交易场所
    exch_city = w.wss(code, "exch_city")
    code_exch_city = exch_city.Data[0][0]
    #估价全价（中债）
    dirty_cnbd = w.wsd(code, "dirty_cnbd", "ED0D", get_lastday(), "credibility=1")
    code_dirty_cnbd = dirty_cnbd.Data[0][0]
    #收盘价（全价）
    dirty_price = w.wsd(code, "dirtyprice", "ED0D", get_lastday(), "")
    code_dirty_price = dirty_price.Data[0][0]

    s2 = pd.Series([df_code, code_latest_par,code_windl1_type,code_exch_city,code_dirty_cnbd,code_dirty_price],\
                   index=['code', 'code_latest_par','code_windl1_type','code_exch_city','code_dirty_cnbd',\
                          'code_dirty_price'])
    df_tmp = df_tmp.append(s2,ignore_index=True)
print(df_tmp.head(3))