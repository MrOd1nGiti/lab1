n = 0

while True:
  number = int(input('Введите число: '))
  if number > 0:
    break
  n += 1

# Вывод результатов
print('Квадрат числа:', number**2)
print('Количество отклонённых попыток:', n)
