def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)
    
def triangle_number(number):  
    if number == 0:
        return 0
    else:
        return number + triangle_number(number - 1)
    
number = int(input("Введите число "))
print(f"Факториал числа {number} - {factorial(number)}")
print(f"Треугольное число от числа {number} - {triangle_number(number)}")