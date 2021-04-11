import pandas
teploty = pandas.read_csv("temperature.csv")
import pytemperature
import matplotlib.pyplot as plt

# na stupně Celsia
teploty["AvgTemperatureC"] = pytemperature.f2c(teploty["AvgTemperature"])

mihelto = teploty[(teploty["City"] == "Miami Beach") | (teploty["City"] == "Helsinki") | (teploty["City"] == "Tokyo")]

ax = mihelto.plot("City", "AvgTemperatureC", kind="box", whis=[0, 100])
ax.set_ylabel("Teploty ve stupních Celsia")
ax.set_xlabel("Město")
ax.set_title("Porovnání teplot Miami - Helsinki - Tokyo")
plt.show()
# no a tady mi to udělá graf jen s jedním boxem a nevim proč - vždyť tam mám všechna tři města