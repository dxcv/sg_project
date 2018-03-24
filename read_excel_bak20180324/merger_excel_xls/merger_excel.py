#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 16:09
# @Author  : XMM
# @Site    : 
# @File    : merger_excel.py
# @Software: PyCharm
# -*- coding:utf-8 -*-

import xlrd, xlsxwriter

# 待合并excel
allxls = ["D:\\python_scripts\\sg_project\\read_excel\\excel\\compare_r.xls",
          "D:\\python_scripts\\sg_project\\read_excel\\excel\\compare_result.xls"]

# 目标excel
end_xls = "D:\\python_scripts\\sg_project\\read_excel\\excel\\final_excel.xls"


def open_xls(file):
    try:
        fh = xlrd.open_workbook(file)
        return fh
    except Exception as e:
        print("打开文件错误：" + e)


# 根据excel名以及第几个标签信息就可以得到具体标签的内容
def get_file_value(filename, sheetnum):
    rvalue = []
    fh = open_xls(filename)
    sheet = fh.sheets()[sheetnum]
    row_num = sheet.nrows
    for rownum in range(0, row_num):
        rvalue.append(sheet.row_values(rownum))
    return rvalue

#def get_first_valuse(excel_sheet1):
# 定义一个目标excel
endxls = xlsxwriter.Workbook(end_xls)
workbook = []
count = -1
for excel_i in allxls:
    count += 1
    # 获取第一个excel的sheet个数以及名字作为标准
    #first_file_fh = open_xls(allxls[0])
    first_file_fh = open_xls(excel_i)
    first_file_sheet = first_file_fh.sheets()
    first_file_sheet_num = len(first_file_sheet)
    sheet_name = []
    for sheetname in first_file_sheet:
        sheet_name.append(sheetname.name)

    all_sheet_value = []
    # 把所有内容都放到列表all_sheet_value中
    for sheet_num in range(0, first_file_sheet_num):
        all_sheet_value.append([])
        #for file_name in excel_i:
        file_name = excel_i
        print("正在读取" + file_name + "的第" + str(sheet_num + 1) + "个标签...")
        file_value = get_file_value(file_name, sheet_num)
        all_sheet_value[sheet_num].append(file_value)

    #print(all_sheet_value)

    num = -1
    sheet_index = -1

    # 将列表all_sheet_value的内容写入目标excel
    for sheet in all_sheet_value:
        sheet_index += 1

        workbook.append(sheet_name[sheet_index])
        #判断sheet名称出现的次数是否大于1
        if  workbook.count(sheet_name[sheet_index]) > 1 :
            sheet_name_new = sheet_name[sheet_index] + '副本'+ str(count)
            workbook.append(sheet_name_new)
        else:
            sheet_name_new = sheet_name[sheet_index]

        end_xls_sheet = endxls.add_worksheet(sheet_name_new)

        num += 1
        num1 = -1
        for sheet1 in sheet:
            for sheet2 in sheet1:
                num1 += 1
                num2 = -1
                for sheet3 in sheet2:
                    num2 += 1
                    # print(num,num1,num2,sheet3)
                    # 在第num1行的第num2列写入sheet3的内容
                    end_xls_sheet.write(num1, num2, sheet3)

endxls.close()


##################################
'''
#将多个Excel文件合并成一个
import xlrd
import xlsxwriter
 
#打开一个excel文件
def open_xls(file):
    fh=xlrd.open_workbook(file)
    return fh
 
#获取excel中所有的sheet表
def getsheet(fh):
    return fh.sheets()
 
#获取sheet表的行数
def getnrows(fh,sheet):
    table=fh.sheets()[sheet]
    return table.nrows
 
#读取文件内容并返回行内容
def getFilect(file,shnum):
    fh=open_xls(file)
    table=fh.sheets()[shnum]
    num=table.nrows
    for row in range(num):
        rdata=table.row_values(row)
        datavalue.append(rdata)
    return datavalue
 
#获取sheet表的个数
def getshnum(fh):
    x=0
    sh=getsheet(fh)
    for sheet in sh:
        x+=1
    return x
 
 
if __name__=='__main__':
    #定义要合并的excel文件列表
    allxls=['F:/test/excel1.xlsx','F:/test/excel2.xlsx']
    #存储所有读取的结果
    datavalue=[]
    for fl in allxls:
        fh=open_xls(fl)
        x=getshnum(fh)
        for shnum in range(x):
            print("正在读取文件："+str(fl)+"的第"+str(shnum)+"个sheet表的内容...")
            rvalue=getFilect(fl,shnum)
    #定义最终合并后生成的新文件
    endfile='F:/test/excel3.xlsx'
    wb1=xlsxwriter.Workbook(endfile)
    #创建一个sheet工作对象
    ws=wb1.add_worksheet()
    for a in range(len(rvalue)):
        for b in range(len(rvalue[a])):
            c=rvalue[a][b]
            ws.write(a,b,c)
    wb1.close()
    print("文件合并完成")

'''

