# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
my_list = [1.1, 1.2, 3.1, 5, 10.01]
current_list = []
for i in range(len(my_list)):
    current_list.append(round((my_list[i] % 1), 2))
print(current_list)
min = current_list[0]
max = current_list[1]
for i in range(len(current_list)):
    if current_list[i] > max:
        max = current_list[i]
    elif current_list[i] < min and current_list[i] != 0:
        min = current_list[i]
print(min, max, max - min)