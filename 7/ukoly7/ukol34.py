import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")
import pandas
import matplotlib.pyplot as plt

velikonoce = pandas.read_csv("velikonoce.csv")

ax = velikonoce.plot("Datum", "Počet", kind="bar")
ax.set_ylabel("Počet dnů")
ax.set_xlabel("Datumy")
ax.set_title("Kolikrát na který datum připadly Velikonoce")
plt.show()

# rozšířené zadání - vytvořit si dateframe sama
from dateutil import easter
data = []
for rok in range(1600,2100):
    datum = easter.easter(rok)
  # Naformátuj datum jako řetězec tak, aby obsahovalo jen měsíc a den. Měsíc dej na začátek a za něj den - použij funkci strftime, kterou jsme spolu probírali
    datum = datum.strftime("%m %d")
  # Naformátovaný datum ulož do seznamu data
    data.append(datum)

data = pandas.DataFrame(data, columns=["Datum"])
data = data.groupby("Datum").size()
# data = data.rename(columns={"0":"Počet"})
data.to_csv("mujsoubor.csv")
# nejde mi pojmenovat ten druhý sloupeček :( a rename mi nefunguje, leda mě napadá udělat to pak z toho vytvořeného souboru
# a v něm to pak pojmenovat, ale to mi přijde jako nepěkné řešení...