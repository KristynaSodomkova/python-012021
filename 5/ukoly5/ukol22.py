import pandas
import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")

mrtvoly = pandas.read_csv("character-deaths.csv")
mrtvoly = mrtvoly.set_index("Name")

print(mrtvoly.columns)
print(mrtvoly.loc["Hali"])
print(mrtvoly.loc["Gevin Harlaw" : "Gillam"])
vyber1 = mrtvoly.loc["Gevin Harlaw" : "Gillam"]
print(vyber1["Death Year"])
print(mrtvoly.loc["Gevin Harlaw":"Gillam", "GoT":"DwD"])
print(vyber1.loc[:, "GoT":"DwD"])
print(mrtvoly.loc["Gevin Harlaw":"Gillam", "Death Year"])
print(mrtvoly.loc["Gevin Harlaw":"Gillam", "GoT":"DwD"])
