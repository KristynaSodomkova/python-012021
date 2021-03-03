"""class Employee:
    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}."

frantisek = Employee()
frantisek.name = "František Novák"
frantisek.position = "konstruktér"

klara = Employee()
klara.name = "Klára Nová"
klara.position = "konstruktérka"

print(frantisek.get_info())
print(klara.get_info())"""

"""class Employee:
    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}."
    def __init__(self, name, position):
        self.name = name
        self.position = position

frantisek = Employee("František Novák", "konstruktér")
klara = Employee("Klára Nová", "svářeč")

print(frantisek.get_info())
print(klara.get_info())"""

class Employee:
    def take_holiday(self, days):
        if self.remaining_holiday_days >= days:
            self.remaining_holiday_days -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.remaining_holiday_days} dní."
    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}"
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.remaining_holiday_days = 25


frantisek = Employee("František, Novák", "kontruktér")

print(frantisek.take_holiday(5))
print(frantisek.take_holiday(30))
