import random
class Vlad:
    def __init__(self, name='Vlad', home=None, money=None, toy=None, friend=None, ruchka=None, nastriy=None, foog=None ):
        self.name = name
        self.home = home
        self.money = 200
        self.toy = toy
        self.friend = 2
        self.ruchka = 1
        self.nastriy = 1
        self.food = 0

    def get_toy(self):
        if self.toy==1:
            self.friend+=1

    def get_name(self):
        pass

    def get_home(self):
        pass

    def get_money(self):
        pass

    def get_batki(self):
        if self.ocinki > 8:
            self.money+100

    def get_ocinki(self):
        pass
    def get_friend(self):
        pass

    def get_ruchka(self):
        pass

    def get_nastriy(self):
        pass

    def get_food(self):
        if self.money==300:
            self.food+1

class chincila:
    def __int__(self):
        if self.money==100:
            self.toy+5

class school:
    def __int__(self):
        if self.friend ==1:
            self.ocinki ==10

class ruchka:
    def __int__(self):
        if self.ruchka==1:
            self.ruchka+1
        brand_of_ruchka = {
            "red": {"fuel": 1, "strenght": 1, "consumption": 1},
            "blue": {"fuel": 2, "strenght": 2, "consumption": 2},
            "white": {"fuel": 3, "strenght": 3, "consumption": 3},
            "black": {"fuel": 4, "strenght": 4, "consumption": 4}}

class food:
    def __int__(self):
        if self.food==1:
            self.nastriy+4

