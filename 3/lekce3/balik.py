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


pox123 = Package("František Novák, Tichá 123, 555 05", "1")

print(pox123.get_info())
pox123.deliver()
print(pox123.get_info())
