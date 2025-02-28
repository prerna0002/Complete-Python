x ={
"name" : " prerna",
2: False,
True :[3,4,5],
(2,3) : 2,
}


info = {}

#Prompt the user for specific information

info["name"] = input("Enter your name: ")
info["age"] = input("Enter your age: ")
info["email"] = input("Enter your email address: ")
info["phone"] = input("Enter your phone number: ")

print("Information of user:")
for key, value in info.items():
    print(f"(key): {value}")