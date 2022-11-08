import pyodbc

# 建立SQL Server 数据库连接
conn =pyodbc.connect('DRIVER={SQL Server};SERVER=LIWANLI-M2;DATABASE=ContainerOperation;UID=sa;PWD=890830')
cursor =conn.cursor()

cursor.execute("SELECT VessName, VoyNo FROM ContainerBill WHERE ConId = '0901'")
rows = cursor.fetchall()
for row in rows:
    print(row.VessName, row.VoyNo)

cursor.close()
conn.close()