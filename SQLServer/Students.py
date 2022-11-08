# ======================
#       imports
# ======================
import pymssql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Basedesk():
    """
    基准框模块
    """

    def __init__(self, master):
        self.root = master
        self.root.config()
        self.root.title('教务管理系统')
        self.width = 380  # 界面宽
        self.height = 300  # 界面高
        # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
        self.screenwidth = self.root.winfo_screenwidth()  # 屏幕宽
        self.screenheight = self.root.winfo_screenheight()  # 屏幕高
        self.alignstr = '%dx%d+%d+%d' % (
        self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.root.geometry(self.alignstr)
        self.R = Register(self.root)
        self.R.reigister(self.root)


class Register():

    def __init__(self, master):

        self.root = master
        # 基准框架 """以下三行需根据个人实际修改"""
        self.ip = 'LIWANLI-M2'
        self.id = 'sa'
        self.pd = '890830'

    """
        登录模块
    """

    def reigister(self, master):
        # 账号密码输入框
        self.initface = LabelFrame(self.root, text='教务系统登录', font=('微软雅黑', 14))
        self.initface.grid(padx=85, pady=30, )

        self.people = Label(self.initface, text='账号')  # 账号
        self.people.grid(row=1, column=0, padx=10, pady=10)
        self.password = Label(self.initface, text='密码')  # 密码
        self.password.grid(row=2, column=0, padx=10, pady=10)
        self.var1 = StringVar
        self.var2 = StringVar
        self.entry_people = Entry(self.initface, textvariable=self.var1)  # 账号输入框
        self.entry_people.grid(row=1, column=1, padx=10, pady=10)
        self.entry_password = Entry(self.initface, textvariable=self.var2, show='*')  # 密码输入框
        self.entry_password.grid(row=2, column=1, padx=10, pady=10)
        self.button_into = Button(self.initface, text='登录', command=self.conn)  # 登录按钮
        self.button_into.grid(row=3, column=0, padx=20, pady=20)
        self.button_into = Button(self.initface, text='退出', command=self.root.quit)  # 退出按钮
        self.button_into.grid(row=3, column=1, padx=20, pady=20)

    def conn(self):
        self.connect = pymssql.connect(self.ip, self.id, self.pd, 'student_Mis')  # 服务器名，账户，密码，数据库名
        self.cursor = self.connect.cursor()
        if self.connect:
            print('连接成功')
        self.sql = "select Students.学号,Students.密码 from Students"

        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchone()
        self.man = self.entry_people.get()
        # self.pd = self.entry_password.get()
        while self.result:
            print('%s|%s' % (self.result[0], self.result[1]))

            if self.result[0] == self.entry_people.get() and self.result[1] == self.entry_password.get():
                print('账号密码正确')

                self.initface.destroy()  # 销毁 initface
                self.check()

                break

            else:

                self.result = self.cursor.fetchone()
        else:
            # 账号或密码错误清空输入框
            self.entry_people.delete(0, END)
            self.entry_password.delete(0, END)
            messagebox.showinfo(title='提示', message='账号或密码输入错误\n请重新输入?')
            # break

        self.cursor.close()
        self.connect.close()

    """
        选择模块
    """

    def check(self):
        self.frame_checkbutton = LabelFrame(self.root, text='功能选择', font=('微软雅黑', 14))
        self.frame_checkbutton.grid(padx=60, pady=30)
        # 查询成绩按钮

        self.button_success = Button(self.frame_checkbutton, text='查询成绩', width=10, height=2, command=self.success)
        self.button_success.grid(row=0, column=0, padx=20, pady=20)
        # 修改密码按钮
        self.button_revise = Button(self.frame_checkbutton, text='修改密码', width=10, height=2, command=self.revise)
        self.button_revise.grid(row=0, column=1, padx=20, pady=20)

    def success(self):

        # 连接数据库
        self.connect = pymssql.connect(self.ip, self.id, self.pd, 'student_Mis')  # 服务器名，账户，密码，数据库名
        if self.connect:
            print('连接成功')
            print(self.man)
            # 查询语句
            search_sql = "select  convert(nvarchar(20), 姓名) , Students.学号,convert(nvarchar(20), 课程名) ,成绩 from  " \
                         "Students, Report, Course " \
                         "where Students.学号=Report.学号 and Report.课程号=Course.课程号 and Students.学号=%s" % self.man

            # 创建游标
            self.cursor1 = self.connect.cursor()
            self.cursor1.execute(search_sql)
            self.row = self.cursor1.fetchone()  # 读取查询结果

            # 表格框
            root = Tk()  # 初始框的声明
            root.geometry('500x400+100+100')
            root.title('成绩查询系统')
            columns = ("姓名", "学号", "课程", "成绩")
            self.treeview = ttk.Treeview(root, height=18, show="headings", columns=columns)
            self.treeview.column("姓名", width=150, anchor='center')  # 表示列,不显示
            self.treeview.column("学号", width=100, anchor='center')
            self.treeview.column("课程", width=150, anchor='center')
            self.treeview.column("成绩", width=100, anchor='center')

            self.treeview.heading("姓名", text="姓名")  # 显示表头
            self.treeview.heading("学号", text="学号")
            self.treeview.heading("课程", text="课程")
            self.treeview.heading("成绩", text="成绩")
            self.treeview.pack(side=LEFT, fill=BOTH)

            # 插入数据
            while self.row:
                self.treeview.insert('', 0, values=(self.row[0], self.row[1], self.row[2], self.row[3]))
                self.row = self.cursor1.fetchone()  # 读取查询结果,

            self.cursor1.close()
            self.connect.close()
            root.mainloop()

    def revise(self):
        self.window = Tk()  # 初始框的声明
        self.window.geometry('400x200+100+100')
        self.window.title('密码修改管理')
        self.frame_revise = LabelFrame(self.window)
        self.frame_revise.grid(padx=60, pady=60)
        self.label_revise = Label(self.frame_revise, text='新密码：')
        self.label_revise.grid(row=0, column=0, padx=10, pady=10)
        self.var3 = StringVar
        self.entry_revise = Entry(self.frame_revise, textvariable=self.var3)
        self.entry_revise.grid(row=0, column=1, padx=10, pady=10)
        self.button_ok = Button(self.frame_revise, text='确定', command=self.ok)
        self.button_ok.grid(row=1, column=0)
        self.button_resive = Button(self.frame_revise, text='取消', command=self.resive)
        self.button_resive.grid(row=1, column=1)
        self.button_quit = Button(self.frame_revise, text='退出', command=self.window.destroy)
        self.button_quit.grid(row=1, column=2)

    def ok(self):
        # 连接数据库
        self.connect = pymssql.connect(self.ip, self.id, self.pd, 'student_Mis')  # 服务器名，账户，密码，数据库名
        self.cursor2 = self.connect.cursor()  # 创建游标
        sql_revise = "update Students set 密码=%s where 学号=%s" % (self.entry_revise.get(), self.man)

        if self.connect:
            print('连接成功')
            print(self.man)
            self.cursor2.execute(sql_revise)
            self.connect.commit()
            print(self.entry_revise.get())
            messagebox.showinfo(title='提示', message='密码修改成功!')
            self.cursor2.close()
            self.connect.close()

    def resive(self):
        self.entry_revise.delete(0, END)


if __name__ == '__main__':
    root = Tk()
    Basedesk(root)
    mainloop()
