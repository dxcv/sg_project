# -*- coding: utf-8 -*-
__author__ = 'XMM'

import pandas as pd
import datetime
import sqlite3 as lite
from pandas.io import sql
from read_o32andgs_data import read_file

o32_file = 'D:/fixed_income/' + u'综合信息查询_组合证券' + '.xls'
o32_data = pd.read_excel(o32_file)
print (o32_data)