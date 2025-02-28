x = round(2837.392,-1)
print(x)

x = round(5837.392,-4)  #function
print(x)

x = abs(4.5)
print(x)

x = pow(2,4,6)
print(x)
print(34.3//1)
int()

x = "hello 4"
print(x.lower()) #method, temprory.. 
print(x.upper())
print(x.title())
print(x.capitalize())

#count,split,replace,truncate,starts_with, ends_with

x= input("write your name:")
print(f"your name is {x.title()}")

#count
x = "Hello my name is m m m"
print(x.lower().startswith("h"))
print(x.endswith("m m"))
print(x.count("l"))

print(x.lower().count("a") )

print( x.split())
print(x.replace("my","your"))
print(x.replace("my","your").replace("m","pikachu",2))

print(x.replace("my","your").replace("m","pikachu",-7))

#print(x.reversed(x))
#index
x = "Hello my name is m m m"
x.replace("m"," ")
print (x.index("m"))
print(len(x.replace("m","")))
#print(x.replace("m","_",-1).index("m"))

##############################################3

pi = 3.142857157143
print(f"Value of pi is {pi}")

print(f"Value of pi is {pi:2f}", pi)
###########################################

full_name = input("Enter your full name: ")
vowels = 'aeiouAEIOU'
vowel_count = sum(c in vowels for c in full_name)
first_vowel_index = next((i for i, c in enumerate(full_name) if c in vowels), None)
vowel_freq = {c: full_name.count(c) for c in vowels if c in full_name}
most_used_vowel = max(vowel_freq, key=vowel_freq.get)
second_most_used_vowel = sorted(vowel_freq, key=vowel_freq.get)[-2]

full_name = full_name.replace(most_used_vowel, second_most_used_vowel)
split_name = full_name.split(second_most_used_vowel)

print("Total number of vowels:", vowel_count)
print("Index of the first vowel:", first_vowel_index)
print("Split name:", split_name)
print("Length of split name:", len(split_name))