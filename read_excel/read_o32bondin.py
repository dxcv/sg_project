# -*- coding: utf-8 -*-
__author__ = 'XMM'

import pandas as pd
import datetime
import sqlite3 as lite
from pandas.io import sql
import sys
reload(sys)
sys.setdefaultencoding('utf8')


#获取前一自然日格式,每周一或者节假日后记得修改n
def get_lastday(n=-1):
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=n)
    n_days = now + delta
    day = n_days.strftime('%Y%m%d')
    return day

#读取o32综合信息查询的证券组合
def return_o32_data():
    o32_file = 'D:/fixed_income/'+ u'综合信息查询_组合证券gs' + get_lastday()[4:] + '.xls'
    o32_data = pd.read_excel(o32_file)
    o32_filter_data = o32_data[[u'组合名称',u'证券代码',u'证券名称',u'交易市场',u'投资类型',u'证券类别']]
    return o32_filter_data

#读取固收部门的数据
def return_gs_data():
    gs_file = 'D:/fixed_income/' + u'固收部数据报送' + get_lastday() + '.xlsx'
    gs_data = pd.read_excel(gs_file,header=3)
    gs_filter_data = gs_data[[u'证券名称',u'证券代码',u'证券类别',u'市场',u'求和项:净价成本']]
    gs_filter_data[u'证券类别'] = gs_filter_data[u'证券类别'].fillna(method='pad')
    gs_filter_data[u'市场'] = gs_filter_data[u'市场'].fillna(method='pad')
    return gs_filter_data

#连接sqlite数据库并将dataframe里面的数据写入数据库表中
def write_data_to_db(from_data= pd.DataFrame(),table_name = 'temptable'):
    cnx = lite.connect('data.db')
    #if_exists 預設為 failed 新建一個 Daily_Record table 並寫入 sql_df資料
    #sql(from_data, name=table_name, con=cnx)
    sql.to_sql(from_data, name=table_name, con=cnx,if_exists='replace',index=False)

#比较两个表的结果并返回
def compare_data(db_path,exectCmd):

    conn = lite.connect(db_path)  # 该 API 打开一个到 SQLite 数据库文件 database 的链接，如果数据库成功打开，则返回一个连接对象
    '''
    cursor = conn.cursor()  # 该例程创建一个 cursor，将在 Python 数据库编程中用到。
    conn.row_factory = lite.Row  # 可访问列信息
    cursor.execute(exectCmd)  # 该例程执行一个 SQL 语句
    rows = cursor.fetchall()  # 该例程获取查询结果集中所有（剩余）的行，返回一个列表。当没有可用的行时，则返回一个空的列表。
    return rows
    # print(rows[0][2]) # 选择某一列数据
    '''
    df = pd.read_sql_query(exectCmd, con=conn)
    return df

def read_file(file_path):
    script_file = open(file_path,'r')
    script_text = script_file.read()
    script_file.close()
    return script_text

#excel文件发送给自己
def excel_to_email():
    pass

def fill_valuse(data=pd.DataFrame(),*args,**kwargs):
    '''
    #测试一下 *args,**kwargs
    for value in args:
        print "another arg:", value
    for key in kwargs:
        print "another keyword arg: %s: %s" % (key, kwargs[key])
    '''


    # 方法一 ：单独列操作, 通过标签索引数据
    data[u'证券类别'] = data[u'证券类别'] .fillna(method='pad')
    data[u'市场'] = data[u'市场'].fillna(method='pad')


    '''
    # 方法二：两列同时操作 ,loc—通过标签索引数据 
    # print data.loc[: ,[u'证券类别',u'市场']]
    data.loc[: ,[u'证券类别',u'市场']]= data.loc[: ,[u'证券类别',u'市场']].fillna(method='pad')
    '''

    '''
    # 方法三：两列同时操作,  通过传递数值进行位置选择
    print data.iloc[:, 2:4].head(3)
    data.iloc[:, 2:4] = data.iloc[:, 2:4].fillna(method='pad')
    '''
    '''
    # 方法四：两列同时操作,  ix - 结合前两种的混合索引，既可以通过标签也可以通过位置选择
    print data.ix[:, 2:4].head(3)
    data.ix[:, 2:4] = data.ix[:, 2:4].fillna(method='pad')
    '''
    return data
#调试
if __name__ == '__main__':

    data = return_gs_data()
    #re_data = fill_valuse(data)
    #print data.head(50)

    o32_result = return_o32_data()
    gs_result = return_gs_data()
    write_data_to_db(o32_result,'o32_result')
    write_data_to_db(gs_result,'gs_result')

    sql_text = read_file('compare.sql')
    #print sql_text

    db_path = 'data.db'
    rows = compare_data(db_path, sql_text)
    #print pd.DataFrame(rows[:,1:2], dtype='object')  # 示例1

    print rows.head(50)
    print rows.dtypes
    rows.to_csv('compare_result.csv' ,encoding='gb2312')


