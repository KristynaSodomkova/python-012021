passwords = {
    "Jiří": "tajne-heslo",
    "Natálie": "jeste-tajnejsi-heslo",
    "Klára": "nejtajnejsi-heslo"
}

name = input("Zadej své jméno: ")

if name in passwords:
    userpass = input("Zadej své heslo: ")
    if userpass in passwords:
        print("Buď vítán.")
    else:
        print("Špatně zadané heslo.")

else:
    print("Nejsi pozvaný.")
