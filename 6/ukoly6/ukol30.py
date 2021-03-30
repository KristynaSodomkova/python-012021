import pandas
import openpyxl
vykazy = pandas.read_csv("vykazy.csv")
info_pro_zakaznika = vykazy.groupby("project")["hours"].sum()
# ulož tabulku s celkovými počty hodin z příkladu 27 jako excel soubor
# info_pro_zakaznika.to_excel("info_pro_zakaznika.xlsx")
# jde tam taky dát přímo cesta, místo toho názvu v uvozovkách:C:\Users\ksodomkova\PycharmProjects\python-012021\6\ukoly6\info_pro_zakaznika.xlsx

# zkus data z Excelu naopak načíst pomocí funkce read_excel() a ověř, že se soubor načetl v pořádku
zkouska = pandas.read_excel("info_pro_zakaznika.xlsx")

# rozšířené zadání
from openpyxl import Workbook
from openpyxl.styles import PatternFill

wb = Workbook()
ws1 = wb.active
ws1.title = "rozvrh"

rozvrh_hodin = [
  ["Anglický jazyk", "Přírodopis", "Dějepis", "Matematika", "Oběd", "Tělesná výchova", "Tělesná výchova", ],
  ["Občanská výchova", "Hudební výchova", "Matematika", "Oběd", "Výtvarná výchova", "Dějepis", ],
  ["Matematika", "Chemie", "Přírodopis", "Fyzika", "Oběd", "Zeměpis", ],
  ["Fyzika", "Anglický jazyk", "Matematika", "Český jazyk", "Dějepis", "Oběd", ],
  ["Český jazyk", "Zeměpis", "Český jazyk", "Výtvarná výchova", "Oběd", ]
]
radek = 1
for den in rozvrh_hodin:
  sloupec = 1
  for predmet in den:
    # Zde zapiš kód pro uložení předmětu do buňky
    sloupec += 1
  radek += 1

wb.save(filename="rozvrh_hodin.xlsx")