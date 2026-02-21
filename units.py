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
<<<<<<< HEAD
    def __init__(self):
        super().__init__()
=======
    def __init__(self, location):
        super().__init__(location)
>>>>>>> 0e92356ec6156f666f488307060e5ee4617a0601
        self.hp = 3