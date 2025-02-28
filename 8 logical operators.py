x = 2>4
print(x)

x = 4
y = 4
print(x==y)

x = True
y = True
print(x==(not y))
print(not( x==y))
print(x and y)
x = bool(1)
y = bool(0)
print(x * y) # multiply
print(x + y) # add

if True:
    print(False)
else:
    print(True)

name = input("name:")

if name:
    print("hello!",name)
else:
    print("Hello! Anonymous")

if name:
    pass
else:
    print("Hello! Anonymous")
print(f"hello!{name}")


age = input("age:")

if age:
    print(f"you are {age} years old")
else:
    print("you aren't even born")


age = input("age:")

if age:
    if age=="0":
        print(f"you aren born")
    else:
        print(f"you are {age} years old")
else:
    print("you didnt mention the age")

age = input("age:")

if age=="0":
    print(f"you aren born")
elif age:
    print(f"you are {age} years old")
else:
    print("you didnt mention the age")

if not age:
    print("you didnt mention the age")
elif age=="0":
    print(f"you arent born")
else:
    print(f"you are {age} years old")


age = input("age:")
if (age !="") and (age!= "0"):
    print(f"you are {age} years old")
elif not age:
    print("you didnt mention the age")
else:
    print(f"you arent born")