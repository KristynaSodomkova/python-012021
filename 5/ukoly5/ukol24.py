import pandas
import pytemperature
import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
teploty = pandas.read_csv("temperature.csv")
teploty = teploty.set_index("City")

print(teploty.head())
print(teploty.loc["Prague"])
nad_osmdesat = teploty[teploty["AvgTemperature"] > 80]
print(nad_osmdesat)
evropa_nad_sedesat = teploty[(teploty["AvgTemperature"] > 60) & (teploty["Region"] == "Europe")]
print(evropa_nad_sedesat)
extremni_hodnoty = teploty[(teploty["AvgTemperature"] > 80) | (teploty["AvgTemperature"] < -20)]
print(extremni_hodnoty)

# pokročilá varianta:
teploty["AvgTemperatureCelsia"] = pytemperature.f2c(teploty["AvgTemperature"])
nad_tricet = teploty[teploty["AvgTemperatureCelsia"] > 30]
print(nad_tricet)
evropa_nad_patnact = teploty[(teploty["AvgTemperatureCelsia"] > 15) & (teploty["Region"] == "Europe")]
print(evropa_nad_patnact)
extremni_hodnoty = teploty[(teploty["AvgTemperatureCelsia"] > 30) | (teploty["AvgTemperatureCelsia"] < -10)]
print(extremni_hodnoty)
# zdá se, že je chyba v některých hodnotách - nevidim tady celou tabulku, ale zřejmě jde o některé státy Afriky
podezrele_hodnoty = teploty[teploty["AvgTemperatureCelsia"] < -40]
print(podezrele_hodnoty)
# hm, tak koukám, že jsou ta data asi velmi chybová a nesmyslné hodnoty se vyskytují i v Asii