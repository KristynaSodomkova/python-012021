"""from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = int(input("Zadejte množství požadované měny: "))
pozadovana_mena = input("Zadejte požadovanou měnu: ")
cena_v_korunach = prevodnik.convert(pozadovana_mena, 'CZK', pozadovano_v_cilove_mene)
cena_v_eurech = prevodnik.convert("EUR", "CZK", pozadovano_v_cilove_mene)
print(cena_v_korunach)
print(cena_v_eurech)"""

from forex_python.bitcoin import BtcConverter
b = BtcConverter()
pozadovana_mena = input("Zadejte požadovanou měnu: ")
pocet_bitcoinu = int(input("Zadejte počet požadovaných bitcoinů: "))
potrebne_mnnozstvi_meny = (b.convert_btc_to_cur(pocet_bitcoinu, pozadovana_mena))

print(potrebne_mnnozstvi_meny)
