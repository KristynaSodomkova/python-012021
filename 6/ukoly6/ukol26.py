import wget
import pandas
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")
liberec = pandas.read_csv("zam_liberec.csv")
plzen = pandas.read_csv("zam_plzeň.csv")
praha = pandas.read_csv("zam_praha.csv")
platy = pandas.read_csv("platy_2021_02.csv")

# ke každé tabulce přidej nový sloupec mesto:
liberec["mesto"] = "Liberec"
plzen["mesto"] = "Plzeň"
praha["mesto"] = "Praha"

# vytvoř novou tabulku zamestanci a ulož do ní info o všech
zamestnanci = pandas.concat([liberec, plzen, praha], ignore_index=True)
# zamestnanci.to_csv("zamestnanci.csv", index=False)

# načti platy zaměstnanců a join se zaměstananci pomocí sloupce cislo_zamestnance:
zamestnanci_s_platy = pandas.merge(zamestnanci, platy, on=["cislo_zamestnance"], how="outer")

# porovnej rozměry tabulek před a po spojení
print(zamestnanci.shape)
print(zamestnanci_s_platy.shape)
print(platy.shape)

# spočti průměrný plat zaměstnanců v jednotlivých kancelářích
print(zamestnanci_s_platy.groupby("mesto")["plat"].mean())

# dobrovolný doplněk:
# ulož do proměnné počet zaměstnanců, kteří již ve firmě nepracují
nepracuji_pocet = zamestnanci_s_platy[zamestnanci_s_platy["plat"].isnull()].shape[0]

# vytvoř tabulku, která obsahuje jména zaměstnanců, kteří již ve firmě nepracují - ulož do csv
nepracuji_jmena = zamestnanci_s_platy[zamestnanci_s_platy["plat"].isnull()]
# nepracuji_jmena.to_csv("nepracuji_jmena.csv", index=False)