from datetime import datetime, timedelta

class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email
class Uchazec(Kontakt):
    def __init__(self, jmeno, email, datum_pohovoru):
        super().__init__(jmeno, email)
        self.datum_pohovoru = datetime.strptime(datum_pohovoru, "%d. %m. %Y")
        self.zapis_z_pohovoru = ""
        self.aktualni_datum = datetime.now()
    def uloz_zapis(self):
        if self.aktualni_datum < self.datum_pohovoru:
            return f"Chybně zadaný datum pohovoru."
        else:
            self.aktualni_datum = self.zapis_z_pohovoru
            return f"Zápis byl uložen"

pohovor1 = Uchazec("Cyril Pažout", "pazout@seznam.cz", "19. 5. 2021", )
pohovor2 = Uchazec("Josef Horáček", "horacek@seznam.cz", "12. 2. 2021", )

print(pohovor1.uloz_zapis())
print(pohovor2.uloz_zapis())

# něco tady neštimuje - proč to chce na řádce 14 str? Vždyť to jinak neporovnam...?