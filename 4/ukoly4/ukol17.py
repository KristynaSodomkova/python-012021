class Polozka:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
    def get_info(self):
        return f"{self.name} se řadí k žánru {self.genre}."

class Film(Polozka):
    def __init__(self, name, genre, length):
        super().__init__(name, genre)
        self.length = length
    def get_info(self):
        return f"{self.name} se řadí k žánru {self.genre}. Film trvá {self.length} min."
    def get_celkova_delka(self):
        return self.length

class Serial(Polozka):
    def __init__(self, name, genre, number_of_episodes, episode_length):
        super().__init__(name, genre)
        self.number_of_episodes = number_of_episodes
        self.episode_length = episode_length
    def get_info(self):
        return f"{self.name} se řadí k žánru {self.genre}. Série obsahuje {self.number_of_episodes} dílů. Jedna epizoda trvá {self.episode_length} min."
    def get_celkova_delka(self):
        return self.episode_length * self.number_of_episodes

class Uzivatel:
    def __init__(self, uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.zhlednute_porady = []
    def zhledni_polozku(self, porady):
        self.zhlednute_porady.append(porady)
    def get_porady(self):
        zhlednute_porady = f"Uživatel {self.uzivatelske_jmeno} zhlédl tyto pořady: "
        for item in self.zhlednute_porady:
            zhlednute_porady += item.name + ", "
            return zhlednute_porady
    def delka_sledovani(self):
        celkova_delka_sledovani = 0
        for item in self.zhlednute_porady:
            celkova_delka_sledovani += item.length
            return f"Uživatel již strávil sledováním pořadů {celkova_delka_sledovani} min."

    def get_info(self):
        return f"Uživatel {self.uzivatelske_jmeno}."


stranger_things = Serial("Stranger Things", "sci-fi", 25, 45)
moonrise_kingdom = Film("Moonrise Kingdom", "romantika/komedie", 95)
nina_svehlova = Uzivatel("Nina Švehlová")

print(stranger_things.get_info())
print(moonrise_kingdom.get_info())
print(moonrise_kingdom.get_celkova_delka())
print(stranger_things.get_celkova_delka())
# print(nina_svehlova.pripocti_zhlednuti(10))
print(nina_svehlova.get_info())
nina_svehlova.zhledni_polozku(moonrise_kingdom)
# print(nina_svehlova.get_porady())
print(nina_svehlova.delka_sledovani())

# nejde mi dát celkovou dobu sledování do funkce get_info u uživatele... Help me please
