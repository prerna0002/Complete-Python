print(15, "hello" , sep="\n", end=" ")
print("dog")


f_name = "prerna"
l_name = "kapoor"
clg_name = "YMCA"
h = 5
age = 20
p = "Haryana"

full_name = "{} {}".format(f_name,l_name)

print("my name is" + f_name +" "+ l_name)
print("my name is ", f_name, l_name + ".")
print("my name is {} {}".format(f_name,l_name))

print("my name is ", full_name)

print(f"my name is {f_name}, {l_name}")

print(f"my \nna\vme \ti\as {f_name}, {l_name}")

print(f"my \rname \ni\as {f_name}, {l_name}")

print("my name is {f_name} {l_name}" )



print("please enter the following details...")
f_name = input("enter first name:")
l_name = input("enter last name:")
print(f"{f_name} {type(f_name)}")

