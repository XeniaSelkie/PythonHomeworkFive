def sum(number_one, number_two):
    if number_one == 0:
        return number_two
    else:
        return sum(number_one - 1, number_two + 1)
    

number_one = int(input("Введите первое число "))
number_two = int(input("Введите второе число "))
print(f"Сумма чисел {number_one} и {number_two} равна {sum(number_one, number_two)}")