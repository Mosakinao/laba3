sum=0
from array import *
D = array('i',[7,100,13,3,10])
print("Массив:")
for i in D:
    print(i)
    if D.index(i) % 2 ==1:
        sum += i
print("Сумма элементов, стоящих на нечетных местах равна: ", sum)