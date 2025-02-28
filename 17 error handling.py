
name "J"
days = 3
with open("attendence.txt", "a") as file:
    file.write(f"\n{name}, {days}")
    new_data = []
    with open("attendence.txt", "r") as file:

old_data = file.read().split("\n")

for line in old_data:

Line = line split(".")

line [1] = str (int(line [1]) + 1)

new_data.append(",".join(line))
with open("attendence.txt", "w") as file:

new_data = "\n".join(new_data)
file.write(new_data)
