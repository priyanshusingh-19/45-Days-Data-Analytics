# Get the bill amount from the user
user_discount_calculation = float(input("Enter the total bill amount to calculate the discount: "))

# Calculate discount based on the bill amount
if user_discount_calculation >= 5000:
    discount = user_discount_calculation * 0.2
    final_discount = user_discount_calculation - discount
    print(f"The original bill amount is: {user_discount_calculation}")
    print("The discount percentage will be 20%")
    print(f"The discount amount: {discount}")
    print(f"The final amount the customer has to pay: {final_discount}")

elif user_discount_calculation >= 2000 and user_discount_calculation < 5000:
    discount = user_discount_calculation * 0.1
    final_discount = user_discount_calculation - discount
    print(f"The original bill amount is: {user_discount_calculation}")
    print("The discount percentage will be 10%")
    print(f"The discount amount: {discount}")
    print(f"The final amount the customer has to pay: {final_discount}")

elif user_discount_calculation >= 0 and user_discount_calculation < 2000:
    print(f"The original bill amount is: {user_discount_calculation}")
    print("The customer does not receive any discount.")

else:
    print("Enter a valid amount please!")