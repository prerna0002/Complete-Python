name = input("Enter your name:")
weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in cm:"))

# Convert height from cm to m
height_in_m = height / 100

BMI = weight / (height_in_m * height_in_m)

if BMI < 18.5:
    print("Your weight is severe Underweight")
elif 18.5 <= BMI < 24.9:
    print("Your weight is normal weight")
elif 24.9 <= BMI < 29.9:
    print("Your weight is overweight")
elif 29.9 <= BMI < 34.9:
    print("Your weight is obesity class I")
elif 34.9 <= BMI < 39.9:
    print("Your weight is obesity class II")
else:
    print("Your weight is Obesity")