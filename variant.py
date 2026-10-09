a = int(input('Введите кол-во чисел: '))
c = 0
t = 0
for _ in range(a):
  n = int(input('Введите число: '))
  if n % 3 == 0:
    c += 1
    t += n
print('=' * 40)
print('Количество:', c)
print('Сумма:', t)
print('=' * 40)
