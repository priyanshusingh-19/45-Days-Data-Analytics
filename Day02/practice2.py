choice = input("1: C to F, 2: F to C: ")
temp = float(input("Enter temperature: "))
    
if choice == '1':
    print(f"{round((9 * temp) / 5 + 32, 1)}°F")
elif choice == '2':
    print(f"{round((temp - 32) * 5 / 9, 1)}°C")
else:
    print("Invalid choice")