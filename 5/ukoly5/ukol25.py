import pandas
import pytemperature

teploty = pandas.read_csv("temperature.csv")
# teploty = teploty.set_index("City")
teploty["AvgTemperatureCelsia"] = pytemperature.f2c(teploty["AvgTemperature"])

# print(teploty.columns)
print(teploty.head())
# dotaz na řádky z 13. listopadu 2017
den_13 = teploty[teploty["Day"] == 13]
# dotaz na řádky z 13. listopadu z US - uložit do nové tabulky a pak použít
den_13_us = teploty[(teploty["Day"] == 13) & (teploty["Country"] == "US")]
# dotaz na řádky ve městě Washington a Philadelphia - pro data z předchozího dotazu
was_phi = den_13_us[(den_13_us["City"] == "Washington") | (den_13_us["City"] == "Philadelphia")]
print(was_phi)
# dobrovolný doplněk:
# průměrná hodnota ze všech měření 13. 11. v US
prumer = den_13_us["AvgTemperatureCelsia"].mean()
print(prumer)
# medián  ze všech měření 13. 11. v US
median = den_13_us["AvgTemperatureCelsia"].median()
print(median)
rozptyl = den_13_us["AvgTemperatureCelsia"].var()
print(rozptyl)
