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

class Serial(Polozka):
    def __init__(self, name, genre, number_of_episodes, episode_length):
        super().__init__(name, genre)
        self.number_of_episodes = number_of_episodes
        self.episode_length = episode_length
    def get_info(self):
        return f"{self.name} se řadí k žánru {self.genre}. Série obsahuje {self.number_of_episodes} dílů. Jedna epizoda trvá {self.episode_length} min."

stranger_things = Serial("Stranger Things", "sci-fi", 25, 45)
moonrise_kingdom = Film("Moonrise Kingdom", "romantika/komedie", 95)

print(stranger_things.get_info())
print(moonrise_kingdom.get_info())

