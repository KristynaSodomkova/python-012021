import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
import pandas
import pytemperature

teploty = pandas.read_csv("temperature.csv")

# na stupně Celsia
teploty["AvgTemperatureC"] = pytemperature.f2c(teploty["AvgTemperature"])

# teploty 13.11
dany_den = teploty[teploty["Day"] == 13]

# vyřaď -99
teploty = teploty[teploty["AvgTemperature"] != -99]

# seřadit od největší
teploty = teploty.sort_values(by="AvgTemperatureC", ascending=False)

#  měst s nejvyšší a  s nejnižší teplotou
print(teploty[["City", "AvgTemperatureC"]].head())
print(teploty[["City", "AvgTemperatureC"]].tail())