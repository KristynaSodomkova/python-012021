class Employee:
    def take_holiday(self, days):
        if self.remaining_holiday_days >= days:
            self.remaining_holiday_days -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.remaining_holiday_days} dní."
    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}. "
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

class Part_time_employee(Employee):
    def __init__(self, name, position, workload):
        super().__init__(name, position)
        self.workload = float(workload)
    def get_workload_info(self):
        return f"Má úvazek {self.workload}."
    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position} a má {self.workload} úvazku."


boss = Manager("Marian Přísný", "vedoucí konstrukčního oddělení")
bimbo = Part_time_employee("Andrej Zkošic", "práce všeho druhu", 0.25)
print(boss.get_info())
boss.add_subordinate(frantisek)
boss.add_subordinate(klara)
print(boss.get_subordinates())
print(bimbo.get_info())
