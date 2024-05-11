# 4.1: Lists

my_list_1 = [1, 2, 'a', 'b', 'Hi!', '5.0']
print(my_list_1[1])
print(my_list_1[4])
print(my_list_1[-1])
print(my_list_1[2:5])

my_list_1.append('Hi again!')
print(my_list_1)

my_list_1[2] = 'T'
print(my_list_1)

my_list_1.remove('b')
print(my_list_1)

del my_list_1[4]
print(my_list_1)

my_list_1.extend("Hello")
print(my_list_1)

my_list_1.pop(5)
print(my_list_1)

my_list_1.insert(5, "Y")
print(my_list_1)

print(len(my_list_1))

my_list_2 = [3, 5, 8]
my_list_3 = my_list_1 + my_list_2
print(my_list_3)

print('Hi!' in my_list_1)

for x in my_list_3:
    print(x, end="---")
print()
