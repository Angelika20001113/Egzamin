
from random import random

n=int(input("Podaj ilość wartości do wylosowania: "))
numbers=[]
for x in range(n):
    numbers.append(random())
print(sorted(numbers))
f = open('percent.txt', 'w')
for i in sorted(numbers):
    a=100*i
    b=round(a)
    f.write(str(i)+";"+str(b) +"%"+ "\n")
f.close()