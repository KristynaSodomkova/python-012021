import pandas
teploty = pandas.read_csv("temperature.csv")
import pytemperature
import matplotlib.pyplot as plt

# na stupně Celsia
teploty["AvgTemperatureC"] = pytemperature.f2c(teploty["AvgTemperature"])

mihelto = teploty[(teploty["City"] == "Miami Beach") | (teploty["City"] == "Helsinki") | (teploty["City"] == "Tokyo")]
# šlo použít i isin
mihelto = mihelto[["City", "AvgTemperatureC"]]

ax = mihelto.boxplot(by="City", whis=[0, 100])
ax.set_ylabel("Teploty ve stupních Celsia")
ax.set_xlabel("Město")
ax.set_title("Porovnání teplot Miami - Helsinki - Tokyo")
plt.show()
