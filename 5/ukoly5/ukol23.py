import pandas
import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")

staty = pandas.read_csv("country_vaccinations.csv")
# print(staty.columns)

# počty očkovaných v jednotlivých státech dne 2021-03-10
dane_datum = staty[staty["date"] == "2021-03-10"]
celkem_naockovanych = dane_datum["total_vaccinations"]
print(celkem_naockovanych)
# více než 1 mil naočkovaných dne 2021-03-10
naockovanych_pres_milion = staty[staty["total_vaccinations"] > 1_000_000]
print(naockovanych_pres_milion)
# kde za den naočkováno více než 1 mil nebo méně než 100 tis
extremni_hodnoty = staty[(staty["daily_vaccinations"] > 100_000) | (staty["daily_vaccinations"] < 100)]
print(extremni_hodnoty)

# dobrovolný doplněk:
# očkování za dny 2021-03-10 a 2021-03-11 v UK, Fin a Italy
uk_fin_it = staty[(staty["country"].isin(["United Kingdom", "Finland", "Italy"])) & (staty["date"].isin(["2021-03-10","2021-03-09"]))]
print(uk_fin_it)
# informace o Japan mezi daty 2021-03-03 a 2021-03-09
japonsko = staty[(staty["country"].isin(["Japan"])) & (staty["date"] >= "2021-03-03") & (staty["date"] <= "2021-03-09")]
print(japonsko)
