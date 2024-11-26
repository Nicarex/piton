def sum_distance(a, b):
    if a > b:
        a, b = b, a
    total_sum = 0
    for number in range(a, b + 1):
        total_sum += number
    return total_sum

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

result = sum_distance(a, b)
print("Сумма чисел от", a, "до", b, "равна:", result)
