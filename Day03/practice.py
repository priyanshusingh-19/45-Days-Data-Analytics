# string indexing

credit_number = "1123-4455-3322-3444"

credit_number = credit_number[::-1]
print(credit_number)

last_digits = credit_number[-4:]
print(f"The last four digit of credit card is XXXX-XXXX-XXXX-{last_digits}")

# print(credit_number[0])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::3])

# format specifiers

"""price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")"""