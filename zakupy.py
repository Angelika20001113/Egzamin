shop= str(input("Podaj listę zakupów: "))
shop=shop.upper()
shoplist= set(shop.split(","))
cennik= {}
for x in  shoplist :
    komunikat="Wpisz cenę dla "+x+ ": "
    try:
        cena= int(input(komunikat))
    except ValueError:
        cena= 0
    cennik[x]=cena

print (cennik)
suma=0

for a in cennik.values():
    suma=+int(a)

if suma <=100:
    print("Możesz kupić wszystkie produkty")
else:
    print("Niestety masz za mało pieniędzy")
