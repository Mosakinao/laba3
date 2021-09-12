sum = float(input("Введите сумму покупки:"))
if sum > 500 and sum < 1000 :
    sum2= float(sum * 0.97)
    print("Скидка составила 3%")
elif (sum > 1000):
    sum2 = sum *0.95
    print("Скидка составила 5%")
else :
    sum2 = sum
print ("К оплате:", sum2)
