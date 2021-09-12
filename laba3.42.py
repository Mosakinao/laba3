from array import *
D = array('i',[7,100,30,13,3,19,5,14])
print("Обновленный массив:")
for i in D:
    if i < 15:
        i= i*2
        print(i)
    else:
        print(i)

