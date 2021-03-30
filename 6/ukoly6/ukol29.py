import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
import pandas
# od lídy: teploty[teploty["AvgTemperature"] != -99]
teploty = pandas.read_csv("temperature.csv")
import pytemperature
# převod na stupně C
teploty["AvgTemperatureCelsia"] = pytemperature.f2c(teploty["AvgTemperature"])
# vyfiltruj si info o telotách 13.11.2017
teploty = teploty[teploty["Day"] == 13]
# vyřaď teploty, které mají hodnotu -99
teploty = teploty[teploty["AvgTemperature"] != -99]
# vypočti počet dat, které máš pro daný den za jednotlivé regiony
print(teploty.groupby("Region").count())
# vypočti průměrnou teplotu za jednotlivé regiony
print(teploty.groupby("Region")["AvgTemperatureCelsia"].mean())
#vypočti maximální a minimální teplotu v každém regionu
print(teploty.groupby("Region")["AvgTemperatureCelsia"].max())
print(teploty.groupby("Region")["AvgTemperatureCelsia"].min())