n = int(input('Введите количество дней от 0 до 100 '))
count = 0 #  счётчик тёплых дней 
maxCount = 0 # счётчик наидольшего периода тёплых дней
for i in range(n):
    t = int(input('Введите суточную температуру t = '))
    if (t > 0):
         count+=1 
    else:
            count = 0
    if(count > maxCount):
        maxCount = count
print(maxCount)




               
