tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

luckyNumber = input("Jaké je Vaše číslo lístku?")
luckyNumber = int(luckyNumber)

if luckyNumber in tombola:
    print ("Vyhráváte:", tombola[luckyNumber])
    tombola.pop(luckyNumber)
else:
    print("Bohužel nevyhráváš nic.")