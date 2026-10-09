a = int(input())
f = int(input())
t = first
pc = 1 if f > 0 else 0
max = f
for _ in range(a - 1):
  num = int(input())
  t += num
  if num > 0:
    pc += 1
  if num > m:
    max = num
print('Сумма:', t)
print('Количество положительных:', pc)
print('Максимум:', max)
