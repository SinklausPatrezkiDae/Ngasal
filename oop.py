#class
class Player:

#constructor
    def __init__(self,name,health,attack,armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        
    #method tampil data
    def tampildata(self):
        print(45*"=")
        print("Name   : ",self.name)
        print("Health : ",self.health)
        print("Attack : ",self.attack)
        print("armor  : ",self.armor)
        print(45*"=")

player1 = Player("P1",100,100,100)
player2 = Player("P2",200,41,76)
player3 = Player("P3",200,48,56)
player4 = Player("P4",23,41,56)
player5 = Player("P5",20,41,56)
player6 = Player("P6",280,41,56)
player7 = Player("P7",290,41,56)
player8 = Player("P8",240,41,56)

player1.tampildata()
player2.tampildata()
player3.tampildata()
player4.tampildata()
player5.tampildata()
player6.tampildata()
player7.tampildata()
player8.tampildata()
