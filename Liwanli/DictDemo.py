dict1 = {"name":"TOM","gender":"Man","age": 20}
dict1["id"] = 110
print(dict1)

dict1["name"] = "ROSE"
print(dict1)

# dict1.clear()
# print(dict1)

print(dict1["name"])

print(dict1.get("name"))
print(dict1.get("gender"))

print(dict1.keys())     # 打印Key值

print(dict1.values())   # 打印对应的值

print(dict1.items())

