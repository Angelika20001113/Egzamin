def putint (komunikat):

    while True:

        try:
            x= int(input("Podaj  " + komunikat+ ": "))
            return x

        except ValueError:
            print("Proszę podać liczbę ")

import math
figures= ["koło", "trójkąt", "prostokąt"]
print(figures)

choice= input("Podaj figurę, której pole chcesz policzyć: ")
def circle(r):
    return math.pi*r*r


def tribal(a, h):
    return a * h / 2

def square (a, b= None):
    if b is None:
        return a*a
    else:
        return a*b

if choice == "koło":

    r = putint("promienń koła")
    p=circle(r)

elif choice=="trójkąt: ":
    a = putint(" podstawę")
    h = putint("wysokość")
    p=tribal(a,h)

elif choice=="prostokąt":

    a= putint("bok prostokąta: ")
    b=putint("drugi bok prostokąta: ")
    p=square(a,b)
if choice in figures :
    print("Pole figury"+ str(choice)+ " o podanych wartościach wynosi" + str(p))
else:
    print("Wybrałeś figurę, której nie obsługuje program!")
