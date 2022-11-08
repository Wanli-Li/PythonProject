str1 = "abcdefgh"
for i in str1:
    if i == "e":
        print("E STOP")
        continue
    print(i)
else:
    print("STOP!")
