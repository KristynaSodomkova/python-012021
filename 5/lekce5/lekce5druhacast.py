import pandas
import wget

# wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/assets/staty.json")

staty = pandas.read_json("staty.json")
staty = staty.set_index("name")
# print(staty.head())
# print(staty.info())
# print(staty.index)
# print(staty.loc["Czech Republic"])
# print(staty.loc["Czech Republic":"Dominican Republic"])
# print(staty.loc[:"Dominican Republic"])
# print(staty.loc["Uzbekistan":])
# print(staty.loc[["Czech Republic", "Slovakia"]])
# print(staty.loc[["Czech Republic", "Slovakia"], "capital"])
# print(staty.loc[["Poland", "Slovakia", "Austria", "Germany"], ["area", "population"]])

# print(staty["population"])
# print(staty[["population", "area"]])
# populace = staty["population"]
# print(populace.sum())

# pidistaty = staty[staty["population"] < 1000]
# print(pidistaty[["area", "population"]])

# lidnate_evropske_staty = staty[(staty["population"] > 20_000_000) & (staty["region"] == "Europe")]
# print(lidnate_evropske_staty["population"])
# vyznamne_staty = staty[(staty["population"] > 1_000_000_000) | (staty["area"] > 3_000_000)]
# print(vyznamne_staty)
zap_vych_evropa = staty[staty["subregion"].isin(["Western Europe", "Eastern Europe"])]
print(zap_vych_evropa)

