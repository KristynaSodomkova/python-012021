class Book:
    def get_info(self):
        return f"{self.title} má {self.pages} stran a stojí {self.price} Kč."
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price
    def sale(self, percentage):
        self.on_sale = self.price - (self.price * percentage / 100)
        return f"Máte slevu {percentage}% a cena je nyní {self.on_sale}"

BX56 = Book("Atlas světa", "200", 2500)
BX42 = Book("Smutné tropy", "250", 500)

print(BX56.get_info())
print(BX42.sale(10))
