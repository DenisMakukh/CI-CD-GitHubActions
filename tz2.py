import datetime

filename = input()
file = open(filename,'r')
for line in file:
    sp = line.split()
file.close()
sp1 = [int(i) for i in sp]
print('Количество элементов в файле:', len(sp1))

a = datetime.datetime.now()

def _min(num):
    mini = 1000000^10000
    for _ in range(len(num)):
        if num[_] <= mini:
            mini = num[_]
    return mini

def _max(num):
    maxi = -(1000000^10000)
    for j in range(len(num)):
        if num[j] >= maxi:
            maxi = num[j]
    return maxi

def _sum(num):
    counter = 0
    for i in num:
        counter += i
    return counter

def _mult(num):
    total = 1
    for i in num:
        total *= i
    return total

print('Минимальное:', _min(sp1))
print('Максимальное:', _max(sp1))
print('Сумма:', _sum(sp1))
print('Произведение:', _mult(sp1))
b = datetime.datetime.now()
c = b - a

