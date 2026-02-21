class Zombie:
    def __init__(self, location):
        self.location = location

class NormalZombie(Zombie):
    def __init__(self, location):
        super().__init__(location)
        self.hp = 1

class FatZombie(Zombie):
    def __init__(self, location):
        super().__init__(location)
        self.hp = 2

class VeryFatZombie(Zombie):
    def __init__(self, location):
        super().__init__(location)
        self.hp = 3