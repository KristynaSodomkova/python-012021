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


frantisek = Employee("František Novák", "kontruktér")
klara = Employee("Klára Nová", "svářeč")

print(frantisek.take_holiday(5))
print(frantisek.take_holiday(30))

class Manager(Employee):
    def add_subordinate(self, new_subordinate):
        self.subordinates.append(new_subordinate)
    def get_subordinates(self):
        subordinates = f"{self.name} má tyto podřízené: "
        for item in self.subordinates:
            subordinates += item.name + ", "
        return subordinates

    def __init__(self, name, position):
        super().__init__(name, position)
        # proč tady nemáme i remaining_holiday_days? A proč není zapsáno subordinates v atributech?
        self.subordinates = []

boss = Manager("Marian Přísný", "vedoucí konstrukčního oddělení")
print(boss.get_info())
boss.add_subordinate(frantisek)
boss.add_subordinate(klara)
print(boss.get_subordinates())

