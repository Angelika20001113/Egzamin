import time
import datetime
import math
def putint (komunikat):

    while True:

        try:
            x= int(input("Podaj  " + komunikat+ ": "))
            return x

        except ValueError:
            print("Proszę podać liczbę ")


t=putint("liczbę sekund, którą ma działać program")
plik=open("logs.txt", "w")
n=0
for i in range (t):
    d=datetime.datetime.now()
    s = d.strftime("%d %b %Y | %H:%M:%S ")
    v=time.time()
    y=math.trunc(v)
    print(d)
    time.sleep(1)
    plik.write(str(n)+ "|" +str(d)  + "|" + str(y) +"\n" )
    n+=1
plik.close()

