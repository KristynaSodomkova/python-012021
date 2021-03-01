"""
Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který
provede následující činnosti:

Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří,
že číslo má správný formát.
Zeptá se uživatele na zprávu, kterou chce zaslat.
Následně vypíše, kolik zpráva bude stát.
Tvůj program bude obsahovat dvě funkce:

První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může
být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420").
Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True,
jinak vrátí hodnotu False.
Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla.
Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a
pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

Tip: Zkus svoji první funkci vytunit tak, že si bude umět poradit s
mezerami v telefonním čísle. Mezer se zbavíš tak, že použiješ funkci replace() a
tečkovou notaci. První parametr je znak, který chceš nahradit, a druhý parametr
nový znak. Níže je příklad použití.

tel_cislo = "+420 734 123 456"
tel_cislo = tel_cislo.replace(" ", "")
"""

phone_number = input ("Zadejte  číslo, kam chcete zprávu zaslat: ")
phone_number = phone_number.replace(" ", "")

def verification(phone_number):
    if len(phone_number) == 9:
        # print("True")
        return True
    elif len(phone_number) ==13:
        # print("True")
        return True
    else:
        print("Zadané číslo neodpovídá formátu.")
        # return False


ok_number = verification(phone_number)

if ok_number:
    user_text = input("Napište text, který chcete zaslat: ")
    text_parts = int(len(user_text) / 180)
    if text_parts == 0:
        text_parts = 1
    def price(text_parts):
        money = text_parts * 3
        return money
    to_pay = price(text_parts)
    print(f"Výsledná cena je {to_pay}Kč.")

