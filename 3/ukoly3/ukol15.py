"""
Vytvoř program na prodej vstupenek do letního kina. Ceny vstupenek jsou v tabulce níže.
Datum: 1.7.2021 - 10.08.2021 cena: 250Kč
Datum: 11.8.2021 - 31.8.2021 cena: 180 Kč
Mimo tato data je středisko zavřené.

Tvůj program se nejprve zeptá uživatele na datum a počet osob,
pro které uživatel chce vstupenky koupit. Uživatel zadá datum ve středoevropském
formátu. Převeď řetězec zadaný uživatelem na datum pomocí funkce datetime.strptime().
Následně se zeptej na počet osob,

Pokud by uživatel zadal příjezd mimo otevírací dobu, vypiš, že letní kino je v
té době uzavřené. Pokud je letní kino otevřené, spočítej a vypiš cenu za ubytování.

Data lze porovnávat pomocí známých operátorů <, >, <=, >=, ==, !=.
Tyto operátory můžeš použít v podmínce if. Níže vidíš příklad porovnání dvou dat.
Program vypíše text "První datum je dřívější než druhé datum.".

from datetime import datetime
prvni_udalost = datetime(2021, 7, 1)
druha_udalost = datetime(2021, 7, 3)
if prvni_datum < druhe_datum:
  print("Druhá událost se stala po první události")
"""
from datetime import datetime, timedelta

datum = input("Zadejte datum ve formátu dd. mm. YYYY: ")
prevedene_datum = datetime.strptime(datum, "%d. %m. %Y")
zacatek_sezony = datetime(2021, 7, 1)
zlom_sezony = datetime(2021, 8, 10)
konec_sezony = datetime(2021, 8, 31)

if prevedene_datum > konec_sezony or prevedene_datum < zacatek_sezony:
    print("V této době je letní kino uzavřené.")
elif prevedene_datum > zlom_sezony:
    pocet_osob = int(input("Zadejte počet osob: "))
    cena = pocet_osob * 180
    print(f"Cena za lístky je {cena} Kč.")
else:
    pocet_osob = int(input("Zadejte počet osob: "))
    cena = pocet_osob * 250
    print(f"Cena za lístky je {cena} Kč.")





