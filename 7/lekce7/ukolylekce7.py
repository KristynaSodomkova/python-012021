import matplotlib.pyplot as plt
import pandas
import wget
# wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/vizualizace/excs/hazeni-kostkami/assets/kostky.txt")
# wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/vizualizace/excs/call-centrum/assets/callcentrum.txt")

kostky = pandas.read_csv("kostky.txt", header=None)
kostky.plot(kind="hist")
plt.show()
# nejčastěji 7
# pravděpodobnost pro 2 a 12 je stejná s dvěma kostkami

callcentrum = pandas.read_csv("callcentrum.txt", header=None)
callcentrum = callcentrum[0].str.split(":", expand=True).astype(int)
print(callcentrum.head())

callcentrum = callcentrum.rename(columns={0: "minuty", 1: "vteriny"})
print(callcentrum.head())

callcentrum["celkovy_cas_v_vterinach"]= callcentrum["minuty"] * 60 + callcentrum["vteriny"]
print(callcentrum.head())

callcentrum["celkovy_cas_v_vterinach"].plot(kind="box")
plt.show()



