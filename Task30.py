#Заполните массив элементами арифметической прогрессии. 
#Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.

a1 = int(input('Введите первый элемент арифметической прогрессии: '))
d = int(input('Введите разность арифметической прогрессии: '))
n = int(input('Введите кол-во элементов арифметической прогрессии: '))

arif_numbers = [a1 + (i - 1) * d for i in range(1, n+1)]
print(*arif_numbers)