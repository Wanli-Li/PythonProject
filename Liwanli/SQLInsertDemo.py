import pymssql

# 建立SQL Server 数据库连接
connect = pymssql.connect('LIWANLI-M2', 'sa', '890830', 'ContainerOperation')  # 建立连接
if connect:
    print("连接成功!")

cursor = connect.cursor()   #创建一个游标对象,python里的sql语句都要通过cursor来执行
sql = "insert into C_test (id, name, gender,C_Name)values(1003, 'Wei,Li', 'women','李卫')"
cursor.execute(sql)   #执行sql语句
connect.commit()  #提交
cursor.close()
connect.close()