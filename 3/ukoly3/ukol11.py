class Auto:
    def get_info(self):
        if self.vypujcenost:
            return f"Automobil s registrační značkou {self.reg_znacka} má značku {self.znacka} a počet najetých kilometrů je {self.kilometry}. Automobil je momentálně k dispozici."
        return f"Automobil s registrační značkou {self.reg_znacka} má značku {self.znacka} a počet najetých kilometrů je {self.kilometry}. Automobil je momentálně vypůjčen."

    def __init__(self, reg_znacka, znacka, kilometry):
        self.reg_znacka = reg_znacka
        self.znacka = znacka
        self.kilometry = kilometry
        self.vypujcenost = True

    def vypujcit(self):
        self.vypujcenost = False

auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534")
auto2 = Auto("1P3 4747", "Škoda Octavia", "4123")

print(auto1.get_info())
auto2.vypujcit()
print(auto2.get_info())

