class Auto:
    def get_info(self):
        return f"Automobil s registrační značkou {self.reg_znacka} má značku {self.znacka} {self.typ}."

    def __init__(self, reg_znacka, znacka, typ, kilometry):
        self.reg_znacka = reg_znacka
        self.znacka = znacka
        self.typ = typ
        self.kilometry = kilometry
        self.vypujcenost = True

    def pujc_auto(self):
        if self.vypujcenost:
            self.vypujcenost = False
            return f"Potvrzuji zapůjčení vozidla"
        return f"Vozidlo není k dispozici"


peugeot1 = Auto("4A2 3020", "Peugeot", "403 Cabrio", "47534")
skoda1 = Auto("1P3 4747", "Škoda", "Octavia", "4123")

looser_input = input("O jakou značku automobilu máte zájem? ")
if looser_input == "Peugeot":
    print(peugeot1.get_info())
    print(peugeot1.pujc_auto())
elif looser_input == "Škoda":
    print(skoda1.pujc_auto())
    print(skoda1.get_info())
else:
    print("Takovou značku tady nevedeme, baby. Jestli chceš být sexy, zvol Škoda nebo Peugeot.")

looser_input = input("O jakou značku automobilu máte zájem? ")
if looser_input == "Peugeot":
    print(peugeot1.get_info())
    print(peugeot1.pujc_auto())
elif looser_input == "Škoda":
    print(skoda1.get_info())
    print(skoda1.pujc_auto())
else:
    print("Takovou značku tady nevedeme, baby. Jestli chceš být sexy, zvol Škoda nebo Peugeot.")

# nevim, proč mi to při dotazu na Škodovku přehazuje výpis textu pro uživatele...?!?
# taky by mě zajímalo, jestli jde nějak vytáhnout info o tom, jaké značky
# máme na skladě, abych nějak automaticky získávala list značek, které máme na skladě,
# jenom tím, že je zadáme do nějakého nově zařazeného auta. Takhle jsem to vlastně dost obešla.
# Například kdybych teď přidala nové auto značky Volvo, tak už mi podmínka nebude fungovat.
"""návod od Jirky:

auta = {
    "peugeot": Auto("4A2 3020", "Peugeot", "403 Cabrio", "47534"),
    "skoda": Auto("4A2 3020", "Škoda", "403 Cabrio", "47534"),
}
peugeot = auta["peugeot"]"""
