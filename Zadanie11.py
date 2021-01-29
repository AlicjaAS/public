from tkinter import *


Wynik =0
operacja=0


def Kasuj():
    global wyświetlaczStr,Suma
    wyświetlaczStr.set("0")
    Suma = 0

def Cyfra0():
    global wyświetlaczStr
    s = wyświetlaczStr.get()
    if(len(s) < 10 and s != '0'):
        s = s + '0'
        wyświetlaczStr.set(s)

def Cyfra(c):
    global wyświetlaczStr,b
    s = wyświetlaczStr.get()
    if(len(s) < 10):
        if(s == '0'):
            s = c
        else:
            s = s + c
        wyświetlaczStr.set(s)
        b=s

def PobierzA():
    global wyświetlaczStr, Wynik
    a = wyświetlaczStr.get()
    if(a != '0'):
        Wynik = int(a)
    else:
        Wynik = Wynik + int(a)
    
    wyświetlaczStr.set(str("0"))

def Plus():
    global wyświetlaczStr, Wynik,operacja
    PobierzA()
    operacja = 0
    
def Minus():
    global wyświetlaczStr, Wynik, operacja
    PobierzA()
    operacja = 1
    
def Dziel():
    global wyświetlaczStr, Wynik,operacja
    PobierzA()
    operacja = 2
    
def Mnoz():
    global wyświetlaczStr, Wynik, operacja
    PobierzA()
    operacja = 3
    
    
def RównaSię():
    global wyświetlaczStr, Wynik,operacja
    s=b
    if operacja == 0:
        Wynik = Wynik + int(s)
    elif operacja == 1:
        Wynik = Wynik - int(s)
    elif operacja == 2:
        Wynik = Wynik // int(s)
    elif operacja == 3:
        Wynik = Wynik * int(s)
    wyświetlaczStr.set(str(Wynik))

def ZmianaZnaku():
    global wyświetlaczStr
    a = wyświetlaczStr.get()
    Wynik=int(a)*(-1)
    
    wyświetlaczStr.set(str(Wynik))

def Cyfra1():
    Cyfra('1')

def Cyfra2():
    Cyfra('2')

def Cyfra3():
    Cyfra('3')

def Cyfra4():
    Cyfra('4')

def Cyfra5():
    Cyfra('5')

def Cyfra6():
    Cyfra('6')

def Cyfra7():
    Cyfra('7')

def Cyfra8():
    Cyfra('8')

def Cyfra9():
    Cyfra('9')

okno = Tk()
okno.title("Kalkulator")
wyświetlaczStr = StringVar()
wyświetlaczStr.set("0")
wyświetlacz = Entry(okno, width=15, font=("Courier New","12", "bold"),textvariable=wyświetlaczStr,justify=RIGHT)
wyświetlacz.grid(row=0,columnspan=5)

cyfra7 = Button(okno, text="7",command=Cyfra7, width=3)
cyfra7.grid(row=1,column=0)

cyfra8 = Button(okno, text="8",command=Cyfra8, width=3)
cyfra8.grid(row=1,column=1)

cyfra9 = Button(okno, text="9",command=Cyfra9, width=3)
cyfra9.grid(row=1,column=2)

cyfra4 = Button(okno, text="4",command=Cyfra4, width=3)
cyfra4.grid(row=2,column=0)

cyfra5 = Button(okno, text="5",command=Cyfra5, width=3)
cyfra5.grid(row=2,column=1)

cyfra6 = Button(okno, text="6",command=Cyfra6, width=3)
cyfra6.grid(row=2,column=2)

cyfra1 = Button(okno, text="1",command=Cyfra1, width=3)
cyfra1.grid(row=3,column=0)

cyfra2 = Button(okno, text="2",command=Cyfra2, width=3)
cyfra2.grid(row=3,column=1)

cyfra3 = Button(okno, text="3",command=Cyfra3, width=3)
cyfra3.grid(row=3,column=2)

cyfra0 = Button(okno, text="0",command=Cyfra0, width=3)
cyfra0.grid(row=4,column=0)

zmiana_znaku = Button(okno, text="+/-",command=ZmianaZnaku, width=3)
zmiana_znaku.grid(row=4,column=1)

plus = Button(okno, text="+",command=Plus, width=3, height=5)
plus.grid(row=1,column=4, rowspan=4)

minus = Button(okno, text="-",command=Minus, width=3)
minus.grid(row=2,column=3)

mnoz = Button(okno, text="X", command=Mnoz, width=3)
mnoz.grid(row=3,column=3)

dziel = Button(okno, text="/", command=Dziel, width=3)
dziel.grid(row=4,column=3)



równasię = Button(okno, text="=",command=RównaSię, width=3)
równasię.grid(row=4,column=2)

kasuj = Button(okno, text="C",command=Kasuj, width=3)
kasuj.grid(row=1,column=3)


okno.mainloop()
