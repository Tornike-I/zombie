class Zombie:
    def __init__(self):
        self.location = 1

class NormalZombie(Zombie):
    def __init__(self):
        super().__init__()
        self.hp = 1

class FatZombie(Zombie):
    def __init__(self):
        super().__init__()
        self.hp = 2

class veryFatZombie(Zombie):
    def __init__(self):
        super().__init__()
        self.hp = 3