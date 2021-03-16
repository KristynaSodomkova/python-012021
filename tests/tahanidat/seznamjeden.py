seznam1 = [
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
  'strčprstskrzkrk',
    7, 9, 6, 7, 9, 8
]
seznam2= [7, 9, 6, 7, 9, 8]

# vytisknout všechna čísla, jinak vytisknout nenalezeno:
for i in seznam1:
    if type(i) == int:
        print(i)


# sečíst všechna čísla v seznamu:
suma = 0
for h in range(0, len(seznam2)):
    suma += seznam2[h]
print(suma)

total = sum(seznam2)
print(total)

# sečíst všechna čísla ve smíšeném seznamu:
for m in seznam1:
    if type(m) == int:
        tot = sum(seznam2)
print(tot)

# zjistit, jestli je položka v seznamu:
if "punťa" in seznam1:
    print("nalezeno")

# přidat položku do seznamu:
seznam2.append(5)
print(seznam2)

# ubrat položku ze seznamu:
seznam2.pop(6)
print(seznam2)

# vymazat nějaké konkrétní položy, ne podle polohy
seznam1.remove("beruška")
print(seznam1)

# vymazat číslo ze seznamu: - ale co když chci vymazat všechny sedmičky?
for z in seznam2:
    seznam2.remove(7)
print(seznam2)
