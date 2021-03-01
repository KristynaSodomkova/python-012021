"""
Uvažuj program, který bude pracovat s výsledky z maturitní zkoušky. Každý student
může mít jeden z následujících výsledků:

"Prospěl s vyznamenáním", pokud je průměr jeho známek maximálně 1.5 a nemá žádnou trojku.
"Neprospěl", pokud má alespoň jednu pětku.
"Prospěl", pokud nemá vyznamenání a současně nedostal žádnou pětku.
Přidej funkci ohodnot_studenta(), která bude mít jeden parametr,
kterým je slovník se známkami studenta.
Funkce rozhodne, zda student prospěl, prospěl s vyznamenáním nebo
neprospěl podle výše popsaných kritérií.

Dále napiš cyklus, který projde seznam vysledky a pomocí
funkce ohodnot_studenta() zjistí prospěch studenta.
Následně pro každého studenta vypíše jeho jméno a informaci o tom,
zda prospěl, neprospěl či prospěl s vyznamenáním.

Výstup tvého programu by mohl vypadat např. takto:

Mirek Dušín: Prospěl s vyznamenáním
Jarka Metelka: Neprospěl
Jindra Hojer: Prospěl
Červenáček: Prospěl s vyznamenáním
Rychlonožka: Prospěl
"""
school_results = [
    {"name": "Mirek Dušín", "cj": 1, "mat": 1, "aj": 1, "ivt": 1},
    {"name": "Jarka Metelka", "cj": 2, "mat": 1, "aj": 2, "ivt": 1},
    {"name": "Jindra Hojer", "cj": 5, "mat": 5, "aj": 5, "ivt": 5},
    {"name": "Červeňáček", "cj": 3, "mat": 3, "aj": 3, "ivt": 3},
    {"name": "Rychlonožka", "cj": 3, "mat": 1, "aj": 1, "ivt": 1}
]


def ohodnot_studenta():
