import pymysql

conn = pymysql.connect(host='localhost', user='root', password='12345678qwer', database='test01', charset='utf8mb4')

cursor = conn.cursor()
sql='''use test01'''
cursor.execute(sql)
cursor.close()
conn.close()