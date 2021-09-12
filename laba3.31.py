A = int(input("Введите первое число:"))
B = int(input("Введите второе число:"))
sum=0
for i in range(A, B+1, 1):
    sum += i**2
print("Сумма квадратов чисел равна:", sum)