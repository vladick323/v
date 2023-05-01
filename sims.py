import random
class Human:
    def __init__(self,name='Human', job=None, home=None, car=None, money=None, toy=None, ):
        self.name=name
        self.money=10000
        self.gladness=50
        self.satiety=50
        self.job=job
        self.home=home
        self.car=car
        self.toy=toy

        def get_toy(self):
            pass
        def get_money(self):
            pass
    def gey_home(self):
        self.home=House
    def gey_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
        return
        self.job=Job(job_list)
    def gey_car(self):
        self.car=Auto(brand_of_car)
    def eat(self):
      if  self.home.food<=0:
          self.shopping("food")
      else:
          if self.satiety>=100:
              self.satiety=100
              return
            self.satiety+=5
            self.home.food-=5
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel<20:
                self.shopping("fuel")
                return
            self.money+=self.job.salary
            self.gladness-=self.job.gladness_less
            self.satiety-=4
    def shopping(self,manage):


    if self.car.drive():
        pass
    else:
        if self.car.fuel < 20:
            manage=="fuel"
              print("kupi palne")
            self.money-=100
            self.car.fuel+=100
        elif manage=="food"
            print("kypi igy")
            self.money-=50
            self.home.foos+=50
        elif manage=="delecacies"
            print("ehf cvfrjkbrb")
            self.gladness+=10
            self.satiety+=2
            self.money+=15

    def chill(self,toy):
        if chill<=1:
            self.shopping.toy
            self.chill+=10

    def clean_home(self):
        pass
    def to_repair(self):
        pass
    def days_indexes(self,day):
        day=f"Today the {day} of {self.name}'s life"
        print(f"{day:=^50}""," "\n")
        human_indexes=self.name+"s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money - {self.money}")
        print(f"Saliety - {self.saliety}")
        print(f"Gladness - {self.gladness}")
        home_indexes="Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes=f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strenght - {self.car.strenght}")
    def is_alive(self):
        if self.gladness<0:
            print("dipresion")
            return False
        elif self.statiety<0:
            print("golod")
            return False
        elif self.money<-500:
            print("bankrot")
    def live(self,day):
        if self.is_alive()==False:
            return False
        if self.home is None:
            print("zaselennya v budinok")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"ya kypiv maxiny {brand_of_car}")
        if self.job is None:
            self.get_job
            print("v mene nema roboti{self.job.job}, z zarplatoyu {self.job.salary}")
        self.days_indexes(day)
        dice=random.randint(1,4)
        if self.satiety<20:
            print("yisty")
            self.eat()
        elif self.gladness<20:

class Auto:
    def __init__(self,brand_list):
        self.brand=random.choice(list(brand_list))
        self.fuel=brand_list[self.brand]["fuel"]
        self.strenght=brand_list[self.brand]["strenght"]
        self.consuption=brand_list[self.brand]["consunption"]

    def drive(self):
        if self.strenght>0 and self.fuel>=self.consuption:
           self.fuel-=self.consuption
           self.strenght-=1
            return True
        else:
            print("машина не може рухатися")
            return False




class House:
    def __int__(self):
        self.mess=0
        self.food=0

        brand_of_car={
            "BMW":{"fuel":100, "strenght":100,"consumption":6},
            "Lada": {"fuel": 50, "strenght": 40, "consumption": 10},
            "Volvo": {"fuel": 70, "strenght": 150, "consumption": 8},
            "Ferrari": {"fuel": 80, "strenght": 120, "consumption": 14}}

class Job:
    def __init__(self, job_list):
        self.job=random.choise(list(job_list))
        self.salary=job_list[self.job]["salary"]
        self.gladnes_less=job_list[self.job]["gladness_less"]

    job_list={
        "Java developer":{"salary":50, "gladness_less":10},
        "Python developer": {"salary": 40, "gladness_less": 3},
        "C++ developer": {"salary": 45, "gladness_less": 25},
        "Rust developer": {"salary": 70, "gladness_less": 1}}