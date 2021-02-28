"""Vstup a výstup
print("Divadlo Pěst na oko")
nazev = "Představení 1"
cas = "16:30 h"
print (nazev + " - " + cas)
hodina = int(19)
minuta = int(30)
print(nazev + " - " + str(hodina) + ":" + str(minuta))
print(input("Zadejte vaše jméno: "))
vek = input("Zadejte váš věk: ")
print(int(vek))"""

""" Zakázka pro divadlo
print("Divadlo pěst na oko")
print("Vítejte v online rezervaci vstupenek")
print("Pro vstup do systému je nejprve potřeba registrace")
user_name = input("Zadejte vaše uživatelske jmeno: ")
age = int(input("Zadejet váš věk: "))
print(user_name + " " + str(age))"""

"""Házení kostkami
import random

dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)
print(int(dice_1 + dice_2))"""

"""Generátor čísel
import random
num_1 = int(input("Zadejte dolní mez: "))
num_2 = int(input("Zadejte horní mez: "))
print(random.randint(num_1, num_2))"""

""" Jednoduché podmínky
password = "simsalabim"
user_name = input("Zadejte vaše uživatelské jméno: ")
user_password = input("Zadejte vaše heslo: ")
if user_password == password:
    user_age = int(input("Zadejte váš věk:"))
    if user_age >= 18:
        print("Smíš vstoupit")
else:
    print("Vstup nepovolen")"""

"""Cena vstupenky
password = "simsalabim"
user_name = input("Zadejte vaše uživatelské jméno: ")
user_password = input("Zadejte vaše heslo: ")
if user_password == password:
    user_age = int(input("Zadejte váš věk:"))
    full_price = 12
    if user_age >= 18:
        print("Smíš vstoupit")
        if user_age < 6:
            user_price = 0
        elif user_age <= 26:
            user_price = 0.65 * full_price
        elif user_age <= 64:
            user_price = full_price
        else:
            user_price = 0.5 * full_price
        user_price = float(user_price)
        user_price = round(user_price, 2)
        print("Cena vstupného je " + str(user_price) + " euro.")
    else:
        print("Vrať se za pár let.")
else:
    print("Vstup nepovolen")"""

"""Registrace
user_name = input("Zadejte své uživatelské jméno: ")
first_password = input("Zadejte své heslo: ")
second_pasword = input("Zadejte heslo znovu: ")
if first_password == second_pasword:
    if len(first_password) >=8:
        print("Registrace proběhla v pořádku.")
    else:
        print("Vaše heslo je příliš krátké.")
else:
    print("Hesla se neshodují")"""

"""Ruleta
user_number = int(input("Zadejte své číslo: "))
if user_number <= 36:
    if user_number == 0:
        print("Hodnota je nula.")
    elif user_number <= 10:
        if user_number % 2 == 0:
            print("Číslo je sudé a černé.")
        else:
            print("Číslo je liché a červené.")
    elif user_number <= 18:
        if user_number % 2 == 0:
            print ("Číslo je sudé a červené.")
        else:
            print("Číslo je liché a černé.")
    elif user_number <= 28:
        if user_number % 2 == 0:
            print("Číslo je sudé a černé.")
        else:
            print("Číslo je liché a červené.")
    elif user_number <= 36:
        if user_number % 2 == 0:
            print ("Číslo je sudé a červené.")
        else:
            print("Číslo je liché a černé.")
else:
    print("Není v ruletě.")"""

"""Přestupný rok
year = int(input("Napište rok: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Je to přestupný rok.")
        else:
            print("Není to přestupný rok.")
    else:
        print("Je to přestupný rok.")
else:
    print("Není to přestupný rok.")"""

"""Řetězce jako sekvence
user_name = input("Zadejte své uživatelské jméno: ")
user_mail = input("Zadejte váš e-mail: ")
if len(user_mail) <= 4:
    print("Špatně zadaná e-mailová adresa.")
zavinac = "@"
dot = "."
if zavinac not in user_mail:
    print("Špatně zadaná e-mailová adresa.")
if dot not in user_mail:
    print("Špatně zadaná e-mailová adresa.")
first_password = input("Zadejte své heslo: ")
second_pasword = input("Zadejte heslo znovu: ")
if first_password == second_pasword:
    if len(first_password) >=8:
        print("Registrace proběhla v pořádku.")
    else:
        print("Vaše heslo je příliš krátké.")
else:
    print("Hesla se neshodují")"""

"""Ověřování hesla
password = "simsalabim"
password_input = input("Zadej heslo: ")
if password[1] == password_input[1]:
    if password[5] == password_input[5]:
        if password[6] == password_input[6]:
            print("Můžeš vstoupit")
else:
    print("Heslo není zadané správně.")"""

"""Seznam hodnocení
hodnoceni = [7, 9, 6, 7, 9, 8]
for h in hodnoceni:
    view = str(h) + "/10"
    print(view)"""

"""Procházení seznamu
hesla = [
  'xyz101',
  'punťa',
  'razor-blade',
  '1234',
  '12011986',
  'martin111',
  'trhnisi',
  'hokuspokus',
  'jeník15',
  'kristus-te-spasi',
  'beruška',
  'strčprstskrzkrk'
]
for h in hesla:
    if len(h) > 8:
        print(h)

for k in hesla:
    if "-" in k:
        print(k)"""

"""SLožitější seznam
mesice = [
  ['leden', 31],
  ['únor', 28],
  ['březen', 31],
  ['duben', 30],
  ['květen', 31],
  ['červen', 30],
  ['červenec', 31],
  ['srpen', 31],
  ['září', 30],
  ['říjen', 31],
  ['listopad', 30],
  ['prosinec', 31]
]
for m in mesice:
    print(m[0])
for month in mesice:
    print(m[1])"""

"""Hry
hry = [
  ['Ňadro na ňadru na nádru', 180],
  ['Útok plyšových krokodýlů', 95],
  ['Cesta do říše zelí', 128],
  ['Romance na zdymadle', 144],
  ['Zátiší s mimozemšťanem', 135],
  ['Čtyři facky a dortík', 100],
  ['Motorová okurka', 165],
  ['Johnny Noir', 140],
  ['Pražská kavárna vrací úder', 130],
  ['Pět sester ve vratech', 111],
  ['Stařec a krajta', 187],
  ['Růžová nemoc', 210],
  ['Smrt v přímém přenosu', 265]
]

for p in hry:
    if p[1] > 120:
     print(p[0])

for h in hry:
    minuty = h[1] % 60
    hodiny = h[1] // 60
    print(h[0] + "  " + str(hodiny) + ":" + str(minuty))"""

"""Průměr  ????
seznam = [10.12, 15.68, 19.025, 20.4]
soucet = 0
for n in seznam:
    soucet = soucet + n
    prumer = soucet[3] /len(seznam)
    print(prumer)"""

"""Největší prvek ????
cisla = [2, 10, 85, 45, 23]

for n in cisla:
    """