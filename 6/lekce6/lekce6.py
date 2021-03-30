""" stažení více souborů najednou:
import wget

soubory = ["https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u202.csv",
           "https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u203.csv",
           "https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/u302.csv"]
for soubor in soubory:
  wget.download(soubor)

"""


import pandas
u202 = pandas.read_csv("u202.csv")

# dát true tam, kde chybí hodnota
chybi_true = u202["znamka"].isnull()
# print(chybi_true)

# dat false tam, kde chybí hodnota
chybi_false = u202["znamka"].notnull()

# vytisknout hodnoty, které jsou prázdné
# print(u202[u202["znamka"].isnull()])

# vrátí datový set očištěn od chybějících dat
# print(u202[u202["znamka"].dropna()])

# odstraní všechny sloupce, které obsahují chybějící data
# print(u202[u202["znamka"].dropna(axis=1)])

# nahradí všechna chybějící data a hodnoty hodnotou x
# print(u202[u202["znamka"].fillna(x)])

# jak tabulky spojit:
# nejprve každou tabulku uložíme do DataFrame s tím, že vyhodíme studenty, kteří na maturitu nedorazili

u202 = pandas.read_csv('u202.csv').dropna()
u203 = pandas.read_csv('u203.csv').dropna()
u302 = pandas.read_csv('u302.csv').dropna()

# funkce concat - pozor - rozbije index
maturita1 = pandas.concat([u202, u203, u302])

# když chceme index přepočítat, ale zase nevíme, kdo maturoval v jaké místnosti
maturita2 = pandas.concat([u202, u203, u302], ignore_index=True)

# uložíme si proto do původních tří tabulek nový sloupeček, kdo byl v jaké místnosti
u202["mistnost"] = "u202"
u203["mistnost"] = "u203"
u302["mistnost"] = "u302"

maturita = pandas.concat([u202, u203, u302], ignore_index=True)

# takhle už mám pěknou vyčištěnou tabulku, takže si ji uložím do csv, index ukládat nebudeme, ten si necháme vyrobit automaticky
maturita.to_csv("maturita.csv", index=False)
