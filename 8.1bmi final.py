name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

# Convert height from cm to m
height_in_m = height/100

# Calculate BMI
BMI = weight / (height_in_m ** 2)

# Print the BMI for verification
print(f"{name}, your BMI is: {BMI:.2f}")

if BMI < 18.5:
    print(f"{name}, your weight is severe underweight")
elif 18.5 <= BMI < 24.9:
    print(f"{name}, your weight is normal")
elif 24.9 <= BMI < 29.9:
    print(f"{name}, your weight is overweight")
elif 29.9 <= BMI < 34.9:
    print(f"{name}, your weight is obesity class I")
elif 34.9 <= BMI < 39.9:
    print(f"{name}, your weight is obesity class II")
else:
    print(f"{name}, your weight is obesity class III")
