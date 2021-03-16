import pandas
import wget
# wget.download("https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/zakladni-dotazy/excs/ceska-jmena/assets/jmena.csv")


jmena = pandas.read_csv("jmena.csv")
# jmena = jmena.set_index("jméno")
# vybranaJmena[["jméno", "četnost"]]
# vybranaJmena.shape
# vybranaJmena = jmena[jmena["svátek"].isin(["1.2.", "2.2.", "3.2." ])]

# print(jmena.loc["Jiří"])
# print(jmena.loc[["Martin", "Zuzana", "Josef"]])
# print(jmena.loc[:"Martin"])
# prum_vek = jmena.loc["Martin":"Tereza"]
# print(prum_vek["věk"])
# jmena.loc["Martin":"Tereza", "věk"]
# od_libora = jmena.loc["Libor":]
# print(od_libora[["věk", "původ"]])
# jmena.loc["Libor":,["věk", "původ"]]
# print(jmena.loc[:, "věk":"původ"])

# print(jmena[jmena["věk"] > 60])
# print(jmena[(jmena["četnost"] > 80_000) & (jmena["četnost"] < 100_000)])
# slov_heb_puv = jmena[(jmena["původ"] == "hebrejský") | (jmena["původ"] == "slovanský")]
# print(slov_heb_puv)
# print(slov_heb_puv[["jméno", "četnost"]])
# vybranaJmena = jmena[[jmena["původ"].isin([["slovanský", "hebrejský"])]
# print(jmena[jmena["svátek"].isin(["1.2.", "2.2.", "3.2."])])