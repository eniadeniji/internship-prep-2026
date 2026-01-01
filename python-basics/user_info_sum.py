# code to ask user for personal information

name = input("Please input your name:")
age = int(input("Please input your age:"))
num1 = int(float(input("Please input the first number to sum:"))) 
num2 = int(float(input("Please input the second number to sum:")))

sum_total = num1 + num2

print("Hello", name, "! You are", age, "years old. The sum of your numbers is", sum_total)