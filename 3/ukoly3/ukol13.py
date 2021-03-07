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

    def vrat_auto(self, stav_tachometru, pocet_dni):
        self.stav_tachometru = stav_tachometru
        self.pocet_dni = pocet_dni
        self.vypujcenost = True
        if pocet_dni < 7:
            cena = pocet_dni * 400
        else:
            cena = pocet_dni * 300
        return f"Cena za zapůjčení automobilu je {cena} Kč."

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


if looser_input == "Peugeot" or looser_input == "Škoda":
    stav_tachometru = int(input("Zapište stav tachometru: "))
    pocet_dni = int(input("Kolik dní jste měl/a automobil zapůjčený? "))
    if looser_input == "Peugeot":
        print(peugeot1.vrat_auto(stav_tachometru, pocet_dni))
    else:
        print(skoda1.vrat_auto(stav_tachometru, pocet_dni))







