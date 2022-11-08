import pymssql

connect = pymssql.connect('LIWANLI-M2', 'sa', '890830', 'ContainerOperation')  # 建立连接
if connect:
    print("连接成功!")

cursor = connect.cursor()  # 创建一个游标对象,python里的sql语句都要通过cursor来执行
cursor.execute("CREATE TABLE systemUsers(Id int NOT NULL, JobNo nvarchar(50) NULL, Name nvarchar(50) NULL, Gender nvarchar(50) NULL) ")  # 执行sql语句
connect.commit()  # 提交
cursor.close()  # 关闭游标
connect.close()  # 关闭连接