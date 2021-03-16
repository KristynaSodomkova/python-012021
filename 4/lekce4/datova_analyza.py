"""instalace:
file - settings - python: project:python-012021 - python interpreter - tam je
přehled modulů, které máme
tlačítko plus - instaluje model
nainstalovat modul pandas
tlačítko instal package - yes
modul wget stahuje věci z netu"""

# import wget
# wget.download("http://nove.kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")

import pandas
nakupy = pandas.read_csv("nakupy.csv")
# print(nakupy)
# nakupy.info()
# print(nakupy.shape)
# print(nakupy.sape[0])
# print(nakupy.columns)
# print(nakupy.iloc[3])
# print(nakupy.iloc[0:5])
# print(nakupy.iloc[:3])
# print(nakupy.iloc[8:])
# print(nakupy.iloc[-3:])
# print(nakupy.head())
# print(nakupy.tail())
# print(nakupy.iloc[:5,0])
print(nakupy.iloc[:, [0,3]])

