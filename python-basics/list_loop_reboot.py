my_list = [1, 2, 3, 4, 5, 6]
print(len(my_list))
print(my_list[-1])

my_list[4] = 10
my_list.insert(3, 99)
my_list.append(7) 

print("Updated list:", my_list)

for num in my_list:
    print(num)

for i in range(len(my_list)):
    print(f"Index: {i} Value: {my_list[i]}")

for num in my_list:
   if num % 2 == 0: 
    print(num, "even")
   else:
    print(num, "odd")