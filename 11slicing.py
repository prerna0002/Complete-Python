x = [2,4,6,8,10,12,14,16,18,20]
print(x[3:8+1])
print(x[3:9])
print(x[4:] )
print(x[:5] )
print(x[:] )
print(len(x[4:] ))
print(x[3:-3] )
#start:stop:jump

print(x[3:-3:2] )
print(x[4::2] )
print(x[:5:3] )

print(x[2:7])
print(x[2:8:-1])
print(x[8:2:-1])
print(x[2:8])

#reverse

print(x[::-1])
print(x[2:8])

x = [2,4,6,8,10,["hi","hello","bye"],12,14,16,18,20]
x[5].pop()
#print([3:5]+x[5][:-1])
print(x.index(16))

print(range(7,11,2))
print(list(range(10)))
print(list(range(1,11)))

print(list(range(5,51,5)))

x= int(input("Enter a number: "))
y = int(input("last number"))
print(list(range[x:y:2]))