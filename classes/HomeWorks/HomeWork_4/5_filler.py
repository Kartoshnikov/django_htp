my_list = input("Enter space-separated number: ").split()
length = len(my_list)
new_list = [int(x) for x in my_list if int(x) != 0]

for i in range(length - len(new_list)):
    new_list.append(-1)
print(my_list, new_list, sep='\n')