import wget
import pandas
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")
staty = pandas.read_json("staty.json")
gdp = pandas.read_csv("gdp.csv")

# vyfiltruj státy, které leží v Evropě
evropske_staty = staty[staty["region"] == "Europe"]
# zjisti počet států v jednotlivých subregionech Evropy
print(evropske_staty.groupby("subregion")["name"].count())
# zjisti počet obyvatel v jednotlivých subregionech Evropy:
print(evropske_staty.groupby("subregion")["population"].sum())

# rozšířené zadání
# odeber státy, které nemají komplet info o gdp
ciste_gdp = gdp.dropna()
# spoj tabulky čistého gdp a států podle třípísmenného kódu
staty = staty.rename(columns={"alpha3Code":"Country Code"})
staty_s_gdp = pandas.merge(staty, gdp, on=["Country Code"], how="outer")
# spočti celkové hdp za rok 2019 a celkový počet obyvatel za jednotlivé subregiony
sub_popul_gdp2019 = staty_s_gdp.groupby("subregion")[["population", "2019"]].sum()
print(sub_popul_gdp2019)

# k vytvořené tabulce vypočti GDP v roce 2019 na obyvatele, tj přidej sloupec
sub_popul_gdp2019["gdp per capita"] = sub_popul_gdp2019["2019"] / sub_popul_gdp2019["population"]
print(sub_popul_gdp2019)
# a kdybych to chtěla zpřehlednit podle světadílu? Tak nevím
