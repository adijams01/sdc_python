# 14.8
import random
class avatar():
    def __init__(self,name,hit_points,attack_power,defence_power):
        self.name=name
        self.hit_points=hit_points
        self.attack_power=attack_power
        self.defence_power=defence_power
        
        
    def attack(self):
        self.z=(random.randint(1,self.attack_power))
        print("attack :",self.z)
    def defend(self):
        self.h=(self.z-self.defence_power)
        if(self.h<0):
            self.h=0            
        print("resistance :",self.h)
    def is_alive(self):
        self.hit_points-=self.h
        if(self.hit_points>0):
            print("Alive")
        else:
            print("Dead")
n=str(input("name : "))
h=int(input("hitpoints : "))
at=int(input("attack power : "))
d=int(input("defence : "))
a=avatar(n,h,at,d)
a.attack()
a.defend()
a.is_alive()
# a.lists()
# a.vs()

    
        
        
