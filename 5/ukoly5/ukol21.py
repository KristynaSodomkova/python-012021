import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")
import pandas

twilio = pandas.read_csv("twlo.csv")

print(twilio.shape)
print(twilio.iloc[:5])
print(twilio.head())
print(twilio.iloc[301])
# dobrovolná část:
pocet_radku = int(twilio.shape[0])
zacatek = int(twilio.iloc[0,5])
konec = int(twilio.iloc[301,5])
procentualni_narust = (100 * (int(konec) - int(zacatek))) / zacatek
print(procentualni_narust)




