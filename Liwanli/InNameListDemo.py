name_list = ["TOM","JACK","ROSE"]

name = input("Please Input You Name:")
if name in name_list:
    print(f"You Name is {name},Already Exists!")
else:
    print(f"You Name is {name},Not Exists!")

