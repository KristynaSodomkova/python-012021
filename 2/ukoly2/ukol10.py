"""
Obchodníci v naší softwarové firmě používají jednoduchý systém,
aby odhadli šanci na úspěch potenciální zakázky.
Každé zakázce přiřadí body od 0 do 10 a platí:

Pokud má zakázka méně než 5 bodů, šance na záskání je malá.
Pokud má zakázka 6 až 8 bodů, šance na získání je střední.
Pokud má zakázka více bodů, šance na získání je vysoká.
Body přidělují podle následujících kritérií:

Odvětví: Firma nejlépe prodává do automotive, o něco hůře do retailu.
Pokud potenciální zákazník podniká v automotive, přičti 3 body, pokud v retailu,
přičti 2 bod, jinak 0.
Obrat: Firma nejlépe prodává zákazníkům se středním obratem.
U malých většinou neuspěje, u velkých občas ano.
Pokud má firma obrat menší než 10 mil. Euro, přičti 0. Pokud je mezi 10 a 1 000 mil.
Euro, přičti 3 body, jinak 1 bod.
Země: Firma je nejúspěšnější v Česku a na Slovensku (2 body),
o něco méně v Německu a ve Francii (1 bod). Ostatním zemím dej 0.
Konference: Firma loni pořádala odbornou konferenci pro zákazníky.
Pokud se zákazník konference účastnil, přičti 1 bod, jinak 0.
Newsletter: Firma též rozesílá newsletter o svém produktu.
Pokud zákazník newsletter odebírá, přičti 1 bod.
Napiš funkci, které bude mít 5 parametrů, které reprezentují zadaná kritéria.
Poslední dvě kritéria zadej jako nepovinná s výchozí hodnotou False.
Funkce vrátí šanci na získání zakázky jako řetězec.
"""

def success_evaluation(odvetvi, obrat, zeme, konference=False, newsletter=False):
    points = 0
    if odvetvi == "automotive":
        points += 3
    elif odvetvi == "retail":
        points += 2
    else:
        points += 0

    if obrat < 10000000:
        points += 0
    elif obrat < 1000000000:
        points += 3
    else:
        points += 1

    if zeme == "Česko" or zeme == "Slovensko":
        points += 2
    elif zeme == "Německo" or zeme == "Francie":
        points += 1
    else:
        points += 0

    if konference:
        points += 1
    else:
        points += 0

    if newsletter:
        points += 1
    else:
        points += 0

    if points < 5:
        return "Šance na získání zakázky je malá."
    elif points <= 8:
        return "Šance na získání zaázky je střední."
    else:
        return "Šance na získání zakázky je vysoká."

area_of_business = input("Zadejte odvětví: ")
turnover = int(input("Zadejte obrat: "))
country = input("Zadejte zemi: ")
conference = input("Účast na konferenci: ")
bulletin = input("Odběr newsletteru: ")

if conference == "ano":
    if bulletin == "ano":
        print(success_evaluation(area_of_business, turnover, country, True, True))
    else:
        print(success_evaluation(area_of_business, turnover, country, True, False))
else:
    if bulletin == "ano":
        print(success_evaluation(area_of_business, turnover, country, False, True))
    else:
        print(success_evaluation(area_of_business, turnover, country, False, False))