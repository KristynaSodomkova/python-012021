# Vyvíjíš software pro obchod s elektronickými součástkami.
# Firma eviduje informace o počtu součástek na skladě ve slovníku.
# Klíč slovníku je kód součástky a číslo je počet součástek na skladě.
# Napiš software, který bude využívat prodavač v případě, že do obchodu přijde
# zákazník.
# Software se nejprve zeptá na kód součástky a poté na množství,
# které si zákazník chce koupit.
# Obě informace si ulož. Následně naprogramuj následující varianty:
# Pokud zadaný zadaný kód není ve slovníku, není součástka skladem.
# Vypiš tedy zprávu, že součástka není skladem.
# Pokud zadaná součástka na skladě je, ale je jí méně,
# než požaduje zákazník, vypiš text o tom,
# že lze prodat pouze omezené množství kusů.
# Následně součástku odeber ze slovníku, protože je vyprodaná.
# Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci,
# že poptávku lze uspokojit v plné výši,
# a sniž počet součástek na skladě o množství požadované zákazníkem.

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

code = input("Zadejte kód součástky: ")

amount = int(input("Zadejte počet kusů: "))


if code in sklad:
    if amount >= sklad[code]:
        print(f"Maximální prodané mnnožství je {sklad[code]} a toto množství bylo přidáno do košíku.")
        sklad.pop(code)

    else:
        print("Zboží bylo přidáno do košíku")
        sklad[code] -= amount

else:
    print("Součástka není skladem.")

# print(sklad)