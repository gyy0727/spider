import xlrd


# 打开文件方式1：
work_book = xlrd.open_workbook('wenxiong.xls')
# 方式2：
w2 = xlrd.book.open_workbook_xls('wenxiong.xls')

'''# 获取工作簿中sheet表数量
print(work_book.nsheets)
# 打印结果：
# 2

# 获取工作簿中所有sheet表对象
sheets = work_book.sheets()
print(sheets)
# ------运行结果------
# [<xlrd.sheet.Sheet object at 0x0000025838B69E80>,
# <xlrd.sheet.Sheet object at 0x0000025838B69E48>]
# ------运行结果------

# 获取工作簿所有sheet表对象名称
sheets_name = work_book.sheet_names()
print(sheets_name)
# ------运行结果------
# ['sheet1', 'Sheet2']
# ------运行结果------
'''
'''# 按索引获取sheet对象
sheet_1 = work_book.sheet_by_index(0)
print(sheet_1)
# ------运行结果------
# <xlrd.sheet.Sheet object at 0x000001CE3473C550>
# ------运行结果------'''

# 按sheet表名称获取sheet对象，名称分大小写
sheet_1 = work_book.sheet_by_name('wenxiong')
#print(sheet_1)
# ------运行结果------
# <xlrd.sheet.Sheet object at 0x000001C6A5B7C710>
# ------运行结果------

'''# 获取sheet表单元格对象，单元格数据类型：单元格值
cell_0 = sheet_1.cell(0,0)
print(cell_0)
# ------运行结果------
# text:'日期'
# ------运行结果------
'''
# 获取sheet表单元格值
cell_0_value = sheet_1.cell_value(1,1)
print(cell_0_value)
# ------运行结果------
# 日期
# ------运行结果------

'''# 获取单元格类型
cell_0_type = sheet_1.cell_type(0,0)
print(cell_0_type)
# ------运行结果------
# 1
# ------运行结果------

'''
