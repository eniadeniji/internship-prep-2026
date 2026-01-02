# Program to ask user fro input, convert input, calc sum, compare num.

# Asking for two numbers
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

# calculate sum
sum_number = num1 + num2

print("Sum:", sum_number)

# compare num
if num1 > num2:
   print("First number is greater")

elif num2 > num1:
   print("Second number is greater")

else:
   print("Both numbers are equal")