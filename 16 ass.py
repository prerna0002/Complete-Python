def custom_mean(lst):
    if len(lst) == 0:
        return None  # or raise ValueError("List is empty")
    sum = 0
    for num in lst:
        sum += num
    return sum / len(lst)


def custom_count(lst, target):
    count = 0
    for elem in lst:
        if elem == target:
            count += 1
    return count

def custom_index(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1  # return -1 if target not found

numbers = [1, 2, 3, 4, 5]
print(custom_mean(numbers))  
print(custom_count(numbers, 3)) 
print(custom_index(numbers, 3))