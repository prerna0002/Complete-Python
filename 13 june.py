x = [1,2,3,4,5]
y = [6,7,8,9,10]
print(x+y)
x.append("yaay")
print(x)

x = [1,2,3,4,5]
y = [6,7,8,9,10]
x.insert(len(x),"prernakapoor")
y = x.pop(2)
x.append(y)
print(x)

x.reverse()
print(x)

x = list(reversed(x))
print(x)

y = x.copy()
y = x # pass by refersence
print(x,y)


x[2] = 10
print(x,y)

x = [1,3,2,7,4,5] + [3,4,5,6,3]
print(x)

x = [0]*1000
print(x)

x = [""]*30
x[6] = "prerna"
print(x)

x.append("kapoor")
print(x)