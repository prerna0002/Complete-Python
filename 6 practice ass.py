name1 = input("Enter your full name: ")
name = name1.lower()
vowels = 'aeiou'
x = sum(name.count(c) for c in vowels)
j = {c: name.count(c) for c in vowels if c in name}
j = sorted(j.items(), key=lambda x: x[1], reverse=True)
j2 = j[1][0]
name = name.replace(j[0][0], j[1][0])
split_name = name.split(j[1][0])

print("Total number of vowels:", x)
print("Split name:", split_name)
print("Length of split name:", len(split_name))