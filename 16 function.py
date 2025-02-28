def func(x,y):
    return "Hello"

print(type(func(1,2)))


def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"

full = get_full_name("prerna", "kapoor")
print(full)


x = 5
def change():
    global x
    x=3
    return x
print(x)
change()
print(x)


x = [1,2,3,4]
def change(y):
     y.append(5)
change(x)
print(x)

x = 5
def change(y):
     y += 3
change(x)
print(x)