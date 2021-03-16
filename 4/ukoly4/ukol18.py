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
    def uloz_zapis(self, zapis_z_pohovoru):
        if datetime.now() < self.datum_pohovoru:
            return f"Chybně zadaný datum pohovoru."
        else:
            self.zapis_z_pohovoru = input("Zápis z pohovoru: ")
            self.zapis_z_pohovoru = zapis_z_pohovoru
            return f"Zápis byl uložen"

pohovor1 = Uchazec("Cyril Pažout", "pazout@seznam.cz", "19. 5. 2021")
pohovor2 = Uchazec("Josef Horáček", "horacek@seznam.cz", "12. 2. 2021")

print(pohovor1.uloz_zapis("bylo to super"))
print(pohovor2.uloz_zapis("bylo to strašný"))

