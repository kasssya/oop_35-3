class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name=name
        self.nickname=nickname
        self.superpower=superpower
        self.health_points=health_points
        self.catchphrase=catchphrase

    def __str__(self):
        return \
            f'Name: {self.name}\n'\
            f'Nickname: {self.nickname}\n'\
            f'Superpower: {self.superpower}\n'\
            f'Health points: {self.health_points}\n'\
            f'Catchphrase: {self.catchphrase}'
    def printName(self):
        return \
                f'Name: {self.name}'

    def printHealt(self):
        return f'Health points doubled: {self.health_points*2}'

    def __len__(self):
        return f'Len catchphrase: {len(self.catchphrase)}'

hero1=SuperHero('Robert Downey', 'Iron man', 'fly', 10, "I'm Iron Man"  )

print(hero1)
print(hero1.printName())
print(hero1.printHealt())
print(hero1.__len__())
