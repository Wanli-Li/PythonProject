# 8个老师分配3个办公室
import random

teachers = ["A","B","C","D","E","F","G","H"]
offices = [[],[],[]]

for name in teachers:
    num = random.randint(0,2)
    offices[num].append(name)
# print(offices)
i = 1
for office in offices:
    print(f"办公室人数是{len(office)},老师分别是：")
    for name in office:
        print(name)
    i += 1
