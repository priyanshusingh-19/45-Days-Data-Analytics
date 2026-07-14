Weight = float(input("Enter Your Weight in Kilograms:"))
Height = float(input("Enter Your Height in Meters:"))

bmi = round(Weight/(Height**2),2)

print(f"Your BMI is {bmi}kg/m^2.")