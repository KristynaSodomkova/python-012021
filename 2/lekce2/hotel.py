


def totalPrice(persons, breakfast = False):
    pricePersons = 850
    priceBreakfast = 125
    total = pricePersons * persons
    if breakfast:
        total+= priceBreakfast * persons
    return total


print(totalPrice(2))