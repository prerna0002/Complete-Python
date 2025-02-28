#CRUD
#CREATING
# RETRIVEING
# UPDATING
# DELETING

try:
    file = open("attendence.txt","x")
except FileExistsError:
    pass
file = open("attendence.txt","w")
attendence = {
    "pk":6,
    "sk":4,
    "rr":5
}
data = []
for key in attendence:
    file.write("\n".join(data))

#file.write(f"attendence = {str(attendence)}")
file.close()
 
with open("attendence.txt","r") as file:
    data = file.readline(100)
    print(data.split("\n"))
    print(data)

name = "josh"
days = 3
with open("attendence.txt","w") as file:
    file.write(f"\n{name},{days}")