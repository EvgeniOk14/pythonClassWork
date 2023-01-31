n = int(input('Введите количество арбузов N: '))
print('Вы ввели количество арбузов N= ', n)
min = 100
max = 0
for i in range(n):
    mass = int(input('Введите массу арбуза: '))
    if( mass > max):
        max = mass
    if(mass < min):
        min = mass
print('самый тяжёлый арбуз равен: ', max)
print(' ')
print('Самый лёгкий арбуз равен: ', min)
