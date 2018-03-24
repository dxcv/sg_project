#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 20:55
# @Author  : XMM
# @Site    : 
# @File    : merge_data.py
# @Software: PyCharm

import pandas as pd
import os
cur_path = os.path.dirname(os.getcwd()) + '\\excel_dir\\'
excel_file_gs = cur_path + '固收部数据报送20180228.xlsx'
excel_file_o32 = cur_path + '综合信息查询_组合证券.xlsx'

df_gs = pd.read_excel(excel_file_gs,header=3)
df_gs[u'证券类别'] = df_gs[u'证券类别'].fillna(method='pad')
df_gs[u'市场'] = df_gs[u'市场'].fillna(method='pad')
df_gs = df_gs[['证券类别','证券名称','证券代码','求和项:净价成本']]
df_gs.rename(columns={'证券类别':'证券类别gs', '证券代码':'证券代码gs','求和项:净价成本':'净价成本'}, inplace = True)
df_o32 = pd.read_excel(excel_file_o32)
df_o32 =df_o32[['日期','基金名称','组合名称','证券代码','证券名称','证券类别','本币净价成本','本币全价成本','含费用成本']]

df_merge = pd.merge(df_o32,df_gs,on = u'证券名称' , how='inner')

df_merge.to_excel(cur_path+'/merge_result.xls', encoding='gb2312')

'''
grouped = df_merge.groupby(df_merge['证券类别'])
grouped.agg(['sum','mean']).to_excel(cur_path+'/grouped_result.xls', encoding='gb2312')
'''

'''
grouped = df_merge.groupby(df_merge['证券类别'])['净价成本'].sum()
#grouped = grouped.to_frame()
print(grouped)
grouped.to_excel(cur_path+'/grouped_result_sigle.xls', encoding='gb2312')
'''
#对指定的多个列求和
print(df_merge.dtypes)
df_merge[["净价成本"]] = df_merge[["净价成本"]].astype(float)
grouped = df_merge[['本币全价成本','本币净价成本','净价成本']].groupby(df_merge['证券类别']).sum()
#grouped = grouped.to_frame()
print(grouped)
grouped.to_excel(cur_path+'/grouped_result_m.xls', encoding='gb2312')