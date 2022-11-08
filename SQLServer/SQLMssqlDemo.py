import pymssql

# 建立SQL Server 数据库连接
conn = pymssql.connect(
    server='LIWANLI-M2',
    port='1433',
    user='sa',
    password='890830',
    database='ContainerOperation'
)

cursor = conn.cursor()  # 创建一个游标对象,python里的sql语句都要通过cursor来执行
sql = "select * from systemUsers"
cursor.execute(sql)  # 执行sql语句
row = cursor.fetchone()  # 读取查询结果,
while row:  # 循环读取所有结果
    print("Name=%s  Gender=%s" % (row[2], row[3]))  # 输出结果
    row = cursor.fetchone()

cursor.close()
conn.close()
