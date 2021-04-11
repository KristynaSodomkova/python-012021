import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

import pandas
import matplotlib.pyplot as plt

twilio = pandas.read_csv("twlo.csv")
# twilio["Date"] = pandas.to_datetime(twilio["Date"])
twilio.plot("Date", "Close")
# plt.show()
# změnil se popisek osy x, protže máme převedené datum

# Dobrovolný doplněk: popisky os a titulek grafu
ax = twilio.plot("Date", "Close")
ax.set_ylabel("Cena v dolarech")
ax.set_xlabel("Datum")
ax.set_title("Vývoj ceny akcií Twilio")
plt.show()
