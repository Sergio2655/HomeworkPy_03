import random
my_list = [5]
for i in range(5):
    my_list.append(random.randint(0, 100))
print(my_list)
sum = 0
for i in range(1, len(my_list)):
    if i % 2 != 0:
        sum = sum + my_list[i]
print(sum)