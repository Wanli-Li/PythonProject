import pymssql

# 建立SQL Server 数据库连接
connect = pymssql.connect('LIWANLI-M2', 'sa', '890830', 'ContainerOperation')  # 建立连接
if connect:
    print("连接成功!")

cursor = connect.cursor()   # 创建一个游标对象,python里的sql语句都要通过cursor来执行

sql = "select * from systemUsers"
cursor.execute(sql)   # 执行sql语句
row = cursor.fetchone()  # 读取查询结果,
while row:              # 循环读取所有结果
    print("|Id:%s    |JobNo:%s    |Name=%s   |Gender=%s   |" % (row[0], row[1], row[2], row[3]))   # 输出结果
    row = cursor.fetchone()

cursor.close()
connect.close()
