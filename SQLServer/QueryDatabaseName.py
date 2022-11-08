
# 导入QtSql模块
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# 创建数据库连接并打开（未指定数据库名，创建默认连接）
db = QSqlDatabase.addDatabase("QODBC")
db.setDatabaseName("Driver={Sql Server};Server=localhost;Database=master;Uid=sa;Pwd=890830")
db.open()

# 创建查询对象（使用默认数据库连接）
query = QSqlQuery()

# 查询数据库名（保存在master.sys.databases表中）
query.exec("Select name From sys.databases")

# 依次打印数据库名（系统数据库除外）
while query.next():
    # 获取名称字段的值
    name = query.value("name")
    # 如果不是系统数据库，打印之
    if name.lower() not in ('master', 'tempdb', 'model', 'msdb'):
        print(name)

# 关闭数据库
db.close()
