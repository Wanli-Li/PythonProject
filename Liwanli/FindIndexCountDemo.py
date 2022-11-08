# find(),index(),count()

mystr = "hello world and itcast and itheima and pthon"

print(mystr.find("and"))    # 12
print(mystr.find("and",15,30))  # 23
print(mystr.find("ands"))   # -1

print(mystr.index("and"))    # 12
print(mystr.index("and",15,30))  # 23
# print(mystr.index("ands"))   # 报错

print(mystr.count("and"))    # 3
print(mystr.count("and",15,30))  # 1
print(mystr.count("ands"))   # 0

print(mystr.rfind("and"))    # 35
print(mystr.rfind("and",15,30))  # 23
print(mystr.rfind("ands"))   # -1

print(mystr.rindex("and"))    # 35
print(mystr.rindex("and",15,30))  # 23
# print(mystr.rindex("ands"))   # 报错