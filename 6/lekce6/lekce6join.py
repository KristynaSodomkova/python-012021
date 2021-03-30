import pandas
u202 = pandas.read_csv("u202.csv")
preds = pandas.read_csv('predsedajici.csv')
studenti = pandas.read_csv("studenti.csv")

# print(studenti.head())

# propojeni souboru
propojenyDF = pandas.merge(u202, studenti)
# print(propojenyDF.head())

# kontrola, zda jsme o nějaká data nepřišli:
# print(u202.shape)
# print(propojenyDF.shape)

# pripojime dalsi soubor:
# novy_propojenyDF = pandas.merge(propojenyDF, preds)
# print(novy_propojenyDF.head())

# to nevyšlo, protože "jmeno" je sloupec jednou pro předsedající a jednou pro studenta
# proto mu musím říct, jak to propojit:
# novy_propojenyDF = pandas.merge(propojenyDF, preds, on=["den"])
# print(novy_propojenyDF.head())
#  jenže to nám zmizely některé řádky, proto chceme tyto hodnoty zachovat:
# novy_propojenyDF = pandas.merge(propojenyDF, preds, on=["den"], how="outer")
# print(novy_propojenyDF)
# teď si chceme zobrazit to, kde nám chybí ti studenti/kde je chyba:
# print(novy_propojenyDF[novy_propojenyDF["datum"].isnull()])
# problém je v tom, že zůstala mezer u pondělí (po)
# proto mezery odstraníme metodou strip() - ta odstraní mezery na zač a konci
preds["den"] = preds["den"]. str.strip()
novy_propojenyDF = pandas.merge(propojenyDF, preds, on=["den"], how="outer")
# print(novy_propojenyDF.shape)

# nicméně se dva sloupce přejmenovaly (jmeno -x a jmeno-y)
# můžeme použít metodu rename:
novy_propojenyDF = novy_propojenyDF.rename(columns={"jméno_x": "jméno", "jméno_y": "předs"})

# agregace:
maturita = pandas.read_csv("maturita.csv")
# průměry
print(maturita.groupby("predmet").mean())
# nejhorší výsledky:
print(maturita.groupby("predmet").max())
# rozsah var
# sum - sečtení
print(maturita.groupby("predmet")["znamka"].sum())
# průměrná známka z jednotlivých předmětů:
print(maturita.groupby("predmet")["znamka"].mean())

