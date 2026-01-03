
age = int(input("Please enter your age:"))

if age < 0:
    print("Invalid age")
elif age < 18:
    print("Minor")
elif 18 <= age <= 64:  
    print("Adult")
else:
    print("Senior")
 
  
