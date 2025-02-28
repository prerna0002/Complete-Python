 # Ques.) ------------------->>>>  Calculate mean, mode , median >>>>>>-----------------------------------------

x = [2, 4, 5, 2, 6, 7, 3, 6, 1, 3, 8]

#..........................................MEAN  ................................................................

print(f"Mean: {sum(x)/len(x)}") 
x = [2, 4, 5, 2, 6, 7, 3, 6, 1, 3, 8]

# ........................................Median.................................................................
x.sort()
if len(x)%2 == 0:
    median = round((x[len(x) // 2 - 1] + x[len(x) // 2]) / 2, 2)
else:
    median = round(x[len(x) // 2], 2)
print("Median: ", median)

# .........................................Mode...............................................

x = [2, 4, 5, 2, 6, 7, 3, 6, 1, 3, 8]
freq_dict = {}
for item in x:
    if item in freq_dict:
        freq_dict[item] += 1
    else:
        freq_dict[item] = 1
max_key = max(freq_dict, key=freq_dict.get)
print("The mode is:", max_key)


#-------------------------------------------------- DATE = 18 june----------------------------------------------

# initialize an empty dictionary
# now just iterate on the list, and any new element we get, we create a new key in the dictionary.
# if we get an element already present in the dictionary increase the value
# in the end just print out the key with the highest value

freq_dict = {}
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana', 'grape']
for item in my_list:
    if item in freq_dict:
        freq_dict[item] += 1
    else:
        freq_dict[item] = 1
max_key = max(freq_dict, key=freq_dict.get)
print("The most frequent item is:", max_key)

# -------------------------> ---- Print the inverted right angle triangle ---- <----------------------------
n = int(input("Enter the number of rows: "))
for i in range(n):
    print(' ' * (n-i-1) + '*' * (i+1))