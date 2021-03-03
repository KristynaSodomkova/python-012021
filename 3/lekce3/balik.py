class Package:
    def get_info(self):
        return f"Balík na adresu {self.address} o hmotnosti {self.weight_in_kilos} kg {self.delivered} doručen."

    def __init__(self, address, weight_in_kilos):
        self.address = address
        self.weight_in_kilos = weight_in_kilos
        self.delivered = False

    def deliver(self):
        self.delivered = True


POX123 = Package("František Novák, Tichá 123, 555 05", "1")

print(POX123.get_info())
