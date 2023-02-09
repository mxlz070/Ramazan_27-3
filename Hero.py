class SuperHero:
    people = 'people'
    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def get_name(self):
        return f'name is {self.name}'
    def multy_hillpoint(self):
        return self.health_points * 2
    def __str__(self):
        return f'catchphrase is {self.catchphrase}\n' \
               f'superpower is {self.superpower}\n' \
               f'health_points is {self.health_points}'
    def __len__(self):
        return len(self.catchphrase)
play = SuperHero('Alim', 'Alimmal', 'fire', 200, 'yabestmal')
print(play)
print(play.get_name())
print(play.multy_hillpoint())
print(play.__len__())

class FlyHero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def multy_hillpoint(self):
        self.fly = True
        self.health_points **= 2
        print(f"Updated health points: {self.health_points}")

    def method_fly(self):
        print(f'Fly in the {self.fly}_phrase')

class SpaceHero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def multy_hillpoint(self):
        self.fly = True
        self.health_points **= 2
        print(f"Updated health points: {self.health_points}")

    def method_fly(self):
        print(f'Fly in the {self.fly}_phrase')

flyHero = FlyHero('SuperMan', 'S', 'Devil Eyes', 500, 'Batman is so weak!!!', 100)
print(flyHero)
flyHero.multy_hillpoint()
flyHero.method_fly()
print()

spaceHero = SpaceHero('Sasu', 'Saske', 'Chidori', 700, 'Narutoooo!', 150)
print(spaceHero)
spaceHero.multy_hillpoint()
spaceHero.method_fly()
print()

class Villain(SpaceHero):

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage, fly)
        SuperHero.people = 'monster'

    def gen_X(self):
        pass

    def crit(self, hero):
        return hero.damage ** 2


villain = Villain('Nara', 'Naruto', 'Beast', 1000, 'Dattebayo', 4000)
print(villain.crit(flyHero))