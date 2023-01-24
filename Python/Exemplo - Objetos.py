class BaseMob:

    def __init__(self, hp, atk, defense):
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def baseAtk(self):
        print("Basic attack used.")


class Rhoa(BaseMob):

    def __init__(self, hp, atk, defense):
        #super().__init__(hp, atk, defense)
        #BaseMob.__init__(hp, atk, defense)
        self.hp = hp
        self.atk = atk
        self.defense = defense
    
    def Charge(self):
        print("Charge!")

rhoas = []
for i in range(3):
    rhoas.append(Rhoa(10, 20, 30))


rhoas[2].hp = 15

print (rhoas[2].atk)



