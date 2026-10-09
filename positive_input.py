a = 0
while True:
  n = int(input('Введите число: '))
  if n > 0:
    break
  a += 1
print('Квадрат числа:', n**2)
print('Количество отклонённых попыток:', a)
