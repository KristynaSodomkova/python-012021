class Package:
    def get_info(self):
        if self.delivered:
            return f"Balík na adresu {self.address} o hmotnosti {self.weight_in_kilos} kg byl doručen."
        return f"Balík na adresu {self.address} o hmotnosti {self.weight_in_kilos} kg nebyl doručen."

    def __init__(self, address, weight_in_kilos):
        self.address = address
        self.weight_in_kilos = weight_in_kilos
        self.delivered = False

    def deliver(self):
        self.delivered = True

class Valuable_package(Package):
    def get_value(self):
        return f"Balík na adresu {self.address} má hodnotu {self.value} Kč."
    def __init__(self, address, weight_in_kilos, value):
        super().__init__(address, weight_in_kilos)
        self.value = value

pox123 = Package("František Novák, Tichá 123, 555 05", "1")
pox234 = Valuable_package("Marta Kubišová, Nevimkdevpraze 123", 10, 32000)

print(pox123.get_info())
pox123.deliver()
print(pox123.get_info())
print(pox234.get_info())
print(pox234.get_value())
