import pyodbc

# 建立SQL Server 数据库连接
conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=LIWANLI-M2; DATABASE=ContainerOperation; UID=sa; PWD=890830')
cursor = conn.cursor()

cursor.execute("SELECT Name, Gender FROM systemUsers WHERE Id = '1003'")
rows = cursor.fetchall()
for row in rows:
    print(row.Name, row.Gender)

cursor.close()
conn.close()
