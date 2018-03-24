#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 16:09
# @Author  : XMM
# @Site    :
# @File    : merger_excel.py
# @Software: PyCharm
# -*- coding:utf-8 -*-

import xlrd, xlsxwriter

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

def write_file_valuse(allxls,endxls):
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


def merger_file(from_execls,to_excles):
    from xlrd import open_workbook
    from xlutils.copy import copy
    rb = open_workbook(to_excles)
    # 通过sheet_by_index()获取的sheet没有write()方法
    rs = rb.sheet_by_index(0)
    wb = copy(rb)
    # 通过get_sheet()获取的sheet有write()方法
    ws = wb.get_sheet(0)
    write_file_valuse(from_execls, ws)
    #ws.write(0, 0, 'changed!')
    wb.save(to_excles)

if __name__ == '__main__':

    # 待合并excel
    allxls = ["D:\\python_scripts\\sg_project\\read_excel\\excel\\compare_result.xls"]
    # 目标excel
    end_xls = "D:\\python_scripts\\sg_project\\read_excel\\excel\\final_excel.xls"
    merger_file(allxls,end_xls)