from math import sqrt

a = int(input("Введите длину стороны треугольника 1: "))
b = int(input("Введите длину стороны треугольника 2: "))
c = int(input("Введите длину стороны треугольника 3: "))
if a < 0 or b < 0 or c < 0:
    print("Вы ввели отрицательное число")
else:
    perim = a + b + c
    p = perim / 2
    area = sqrt(p * (p-a) * (p-b) * (p-c))

    print(f"Площадь треугольника равна: {area}\nПериметр равен: {perim}")
