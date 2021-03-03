class Employee:
    def take_holiday(self, days):
        if self.remaining_holiday_days >= days:
            self.remaining_holiday_days -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.remaining_holiday_days} dní."
    def get_info(self):
        msg = f"{self.name}"
        return f"{self.name} pracuje na pozici {self.position}"


    def __init__(self, name, position, probation):
        self.name = name
        self.position = position
        self.remaining_holiday_days = 25
        self.probation = False

frantisek = Employee("František, Novák", "kontruktér")

print(frantisek.take_holiday(5))
print(frantisek.take_holiday(30))