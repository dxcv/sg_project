# -*-coding:utf-8-*-
#######################################################
#openpyxl 只支持office 2010以上的版本，即后缀为xlsx的excel
#filename:test_openpyxl.py
#author:appadmin
#date:2018-03-01
#function：向excel文件中写入数据
#######################################################
import os
import pandas as pd
from openpyxl import load_workbook
import os
# 返回上一级目录，保存excel文件的路径
cur_path = os.path.dirname(os.getcwd())+ '\\excel\\'
"""
padas dataframe生成excel
"""
def dataFrame2sheet(dataframe,excelWriter):

   # DataFrame转换成excel中的sheet表
   dataframe.to_excel(excel_writer=excelWriter, sheet_name="info1",index=None)
   dataframe.to_excel(excel_writer=excelWriter, sheet_name="info2",index=None)
   dataframe.to_excel(excel_writer=excelWriter, sheet_name="info3",index=None)

   excelWriter.save()
   excelWriter.close()

"""
excel中新增sheet表
"""
def excelAddSheet(dataframe,excelWriter,sname = "info5"):

   book = load_workbook(excelWriter.path)
   excelWriter.book = book
   dataframe.to_excel(excel_writer=excelWriter,sheet_name=sname,index=None)
   excelWriter.close()

if __name__ == '__main__':

   # 数据集
   dataSet = [
       {"姓名": "张三", "年龄": 23, "性别": "男"},
       {"姓名": "李四", "年龄": 25, "性别": "男"},
       {"姓名": "王五", "年龄": 21, "性别": "女"}
   ]

   # excelPath
   excelPath=cur_path + u'委托资产投资报表-太平人寿非投连 2018-01-31.xlsx'

   # 生成DataFrame
   dataframe = pd.DataFrame(dataSet)


   #创建ExcelWriter 对象
   excelWriter=pd.ExcelWriter(excelPath,engine='openpyxl')

   # #生成excel
   #dataFrame2sheet(dataframe,excelWriter)

   #excel中增加sheet
   excelAddSheet(dataframe,excelWriter,'add1')