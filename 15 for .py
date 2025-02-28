x = (i**2 for i in range (1,11))
print(x)

x = tuple(i**2 for i in range (1,11))
print(x)

x = list(i**2 for i in range (1,11))
print(x)

x = " " .join(["_"for i in range (1,11)])
print(x)

x = " " .join(["hi" for i in range (1,11)])
print(x)

unique_x = set(x)
highest_freq = 0
for e1 in unique_x:
    freq = x.count(e1)

    if freq> highest_freq:
        highest_freq = freq
        highest_freq_number = e1

        print(f"{e1} - {freq}")

print(highest_freq_number)

s1 = "mouse"
s2 = "keyboard"

for char in s1:
    if char in s2:
        print("yes")
        break
    else:
        print("no")

s1 = "mouse"
s2 = "keyboard"

common = set(s1).intersection(set(s2))
if len(common)>0:
    print("yes")
else:
    print("no")

    s1 = "mouse"
s2 = "keyboard"

common = set(s1).intersection(set(s2))
if len(common):
    print("yes")
else:
    print("no")

##################################

s1 = "Ashwani"
common = set(s1)
print(common)

##############################
counter = {}

for e1 in x:
    if e1 in counter:
        counter[e1] +=1
        highest_freq = 0
        mode = 0
        for e1 in counter:
            if counter[e1]>highest_freq:
                highest_freq = counter[21]
                mode = e1
print(mode)
