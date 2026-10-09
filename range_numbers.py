n = int(input('Введите первое число: '))
c = int(input('Введите второе число: '))
if n < c:
    for i in range(n,c+1,1):
        print(i)
elif n > c:
    for i in range(n,c-1,-1):
            print(i)
else:
     print(n)
