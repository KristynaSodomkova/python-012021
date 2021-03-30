import pandas
import wget

# wget.download('https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/jmena.csv')
# wget.download('https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/studenti1.csv')
# wget.download('https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/agregace-a-spojovani/excs/assets/studenti2.csv')

jmena = pandas.read_csv("jmena.csv")
studenti1 = pandas.read_csv("studenti1.csv")
studenti2 = pandas.read_csv("studenti2.csv")

studenti1["puvod"] = "studenti1"
studenti2["puvod"] = "studenti2"
studenti_spojeno = pandas.concat([studenti1, studenti2], ignore_index=True)
# studenti_spojeno.to_csv("studenti_spojeno.csv", index=False)
print(studenti_spojeno[studenti_spojeno["ročník"].isnull()])
#od Aleše:
#print( studenti["ročník"].isnull() )
# print( studenti["ročník"].isnull().shape  )
# print( studenti[studenti["ročník"].isnull()].shape  )

# print( studenti.columns  )
# print( studenti[studenti["kruh"].isnull()].shape  )

# 33 žáků nestuduje
print(studenti_spojeno[studenti_spojeno["kruh"].isnull()])
# 27 žáků studuje dálkově

# očistíme od těch, co nestudují a od dálkařů
studenti_spojeno = studenti_spojeno.dropna()
print(studenti_spojeno.shape)

# kolik je na každém z oborů studentů:
print(studenti_spojeno.groupby("obor").count())

# průměrný prospěch studentů v každém oboru
print(studenti_spojeno.groupby("obor")["prospěch"].mean())

# propojit se jmény tak, abych věděla pohlaví
spojeni = pandas.merge(studenti_spojeno, jmena, on=["jméno"], how="outer")
print(spojeni)

print(spojeni.groupby("pohlaví").count())