#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 19:18
# @Author  : XMM
# @Site    : 
# @File    : to_excel.py
# @Software: PyCharm

import pandas as pd
import numpy as np
if __name__ == '__main__':
    dates = pd.date_range('20180101',periods=5)

    #lastday = get_lastday()
    df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
    print(df)
    print('**********')
    print(len(df))
    '''
    #方法1：定义Series，循环生成一个100-len（df）行的DataFrame
    s2 = pd.Series(['申港固收自营1号', 0], index=['A', 'B'])
    for r in range(len(df),100+1):
        df = df.append(s2,ignore_index=True)
    #df.to_excel('test_row_col.xlsx',startrow= 3, startcol=1)
    '''
    # 方法2：定义全0的n行2列的数组，通过二维的ndarray生成DataFrame
    df2 = pd.DataFrame(np.zeros([101-len(df),2]), columns=['A', 'B'])
    #print(df2)
    df = df.append(df2,ignore_index=True)
    print(df)
    df.to_excel('test_row_col.xlsx', startrow=15, startcol=8)



