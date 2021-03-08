slovnik1 = {
    "a": "adam", "b": 1, "c": 2, "d": 3
}
vypis_vseho_slovnik1 = slovnik1
print(vypis_vseho_slovnik1)

vypis_hodnot_slovnik1 = slovnik1.values()
print(vypis_hodnot_slovnik1)

vypis_klicu_slovnik1 = slovnik1.keys()
print(vypis_klicu_slovnik1)

vypis_vybrane_hodnoty_slovnik1 = slovnik1["a"]
print(vypis_vybrane_hodnoty_slovnik1)

# vypis klice, který je na určité pozici
vypis_vybrane_hodnoty_dle_poradi = list(slovnik1.values())[0]
print(vypis_vybrane_hodnoty_dle_poradi)

# vypis klice, který má konkrétní hodnotu
for k,v in slovnik1.items():
    if v == 3:
        print(k)


# udělat slovník, který neobsahuje některé hodnoty:
"""slovnik1.pop("a")
print(slovnik1)"""

# tady si vypisuju jen čísla:
"""jen_cisla = slovnik1.pop("a")
print(jen_cisla)"""

"""for items in slovnik1:
    jen_cisla{}"""

# vypsat všechny int ve slovníku
for items in slovnik1.values():
    if type(items) == int:
        print(items)
# sečíst všechny int ve slovníku



