# Firma eviduje volné meetingové místnosti v průběhu dne ve slovníku.
# Klíč slovníku je hodina a hodnotou slovníku seznam zasedaček, které jsou v té době volné.
# Napiš software, který se zeptá uživatele na číslo hodiny, kdy chce zamluvit meeting room.
# Poté vypíše počet volných místností, které jsou k dispozici.

volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}

request = int(input("Zadejte číslo hodiny: "))

print(len(volnePokoje[request]))

# userrequest = int(userrequest)

# print(volnePokoje.values())


#
# chosenHour = request
#
# print(len(chosenHour))

 # for i in volnePokoje.keys():
 #    if i == userrequest:
 #        print(volnePokoje.get(i))



