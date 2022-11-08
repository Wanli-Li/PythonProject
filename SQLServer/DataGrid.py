import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *


def initializeModel(model):
    # 设置表格名称
    model.setTable("systemUsers")
    # 设置编辑策略
    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    # 调用select方法
    model.select()
    # 设置表格头
    model.setHeaderData(0, Qt.Horizontal, "ID")
    model.setHeaderData(1, Qt.Horizontal, "姓名")
    model.setHeaderData(2, Qt.Horizontal, "地址")


def createView(title, model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view


def findrow(i):
    delrow = i.row()
    print("选中第{}行".format(delrow))


def addrow():
    # 在model.rowCount()行后插入1行，并返回插入的行所在行数
    ret = model.insertRows(model.rowCount(), 1)
    print("添加第{}行".format(ret))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase("systemUsers")
    # 设置数据库名字（路径）
    db.setDatabaseName("./db/database.db")

    # 创建一个数据库的表格模型，QSqlTableModel()会自动关联到db上
    model = QSqlTableModel()
    delrow = -1
    # 初始化这个表格模型（函数在上面）
    initializeModel(model)

    # 根据model创建QTableView对象
    view = createView("展示数据", model)
    view.clicked.connect(findrow)

    window = QDialog()
    layout = QVBoxLayout()
    layout.addWidget(view)
    addBtn = QPushButton("添加一行")
    addBtn.clicked.connect(addrow)

    delBtn = QPushButton("删除一行")
    # 下面view.currentIndex().row()表示view中被选中的单元格对象所在行数
    delBtn.clicked.connect(lambda : model.removeRow(view.currentIndex().row()))

    layout.addWidget(addBtn)
    layout.addWidget(delBtn)
    window.setLayout(layout)

    window.setWindowTitle("Database Demo")
    window.resize(550, 400)
    window.show()

    sys.exit(app.exec_())