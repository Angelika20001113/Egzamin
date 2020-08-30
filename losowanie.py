numbers=[]
n=0
while  True:
    x= input("Podaj liczbę: ")
    if x.isnumeric():
        numbers.append(x)
        n+= 1
    else:
        if x =="exit":
            print(numbers,"\n")
            break
        else:
            print("Podałeś "+ str(n)+" liczb, dalej się nie bawię")
            break
