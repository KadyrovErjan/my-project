from itertools import batched
from turtle import Terminator


#
# class SuperHero:
#
#     people = 'people'
#
#     def __init__(self, name, nickname, superpower, health_points, catchphrase):
#         self.name = name
#         self.nickname = nickname
#         self.superpower = superpower
#         self.health_points = health_points
#         self.catchphrase = catchphrase
#
#     def get_name(self):
#         return f'imya: {self.name}'
#
#     def double_health_points(self):
#         self.health_points *= 2
#         return f"zdorovya geroya teper: {self.health_points}"
#
#     def __str__(self):
#         return f"prozvishe: {self.nickname}, sposobnost: {self.superpower}, zdorovya: {self.health_points}, koronnaya fraza: {self.catchphrase}"
#
#     def __len__(self):
#         return len(self.catchphrase)
#
# Flash = SuperHero("Erjan","Era", "fast run", 100,"suuuuuuuf")
#
# print(SuperHero.get_name(Flash))
# print(SuperHero.double_health_points(Flash))
# print(Flash)
# print(f"dlina koronnoy frazy: {len(Flash)}\n")
#
# class Airhero(SuperHero):
#     superpower = "fly"
#
#     def __init__(self, name, nickname, superpower, health_points, catchphrase, speed, damage, fly = False):
#         super().__init__(name, nickname, superpower, health_points, catchphrase)
#         self.speed = speed
#         self.damage = damage
#
#     def double_health_points(self):
#         self.health_points **= 2
#         self.fly = True
#         return f"zdorovya geroya teper: {self.health_points}"
#
#     def fly_phrase(self):
#         if self.fly == True:
#             return f" fly in the True_phrase"
#         else:
#             return f"not fly"
#
#     def km_h(self):
#         return f"skorost: {self.speed}"
#
#     def uron(self):
#         return f"uron: {self.damage}"
#
#         self.fly = True
# Superman = Airhero("Jonh", "Super", "fly", 100, "Lets go", 100000, 10)
#
# print(Superman.get_name())
# print(Superman.km_h())
# print(Superman.uron())
# print(Superman.double_health_points())
# print(Superman)
# print(Superman.fly_phrase())
# print(f"dlina koronnoy frazy: {len(Superman)}\n")
#
# class Earthhero(SuperHero):
#     walk = "walk"
#     fly = False
#
#     def __init__(self, name, nickname, superpower, health_points, catchphrase, speed, damage):
#         super().__init__(name, nickname, superpower, health_points, catchphrase)
#         self.speed = speed
#         self.damage = damage
#
#     def double_health_points(self):
#         self.health_points **= 2
#         self.fly == True
#         return f"zdorovya geroya teper: {self.health_points}"
#     def fly_phrase(self):
#         if self.fly == True:
#             return f" fly in the True_phrase"
#         else:
#             return f"not fly"
#
#
#
#     def __init__(self, name, nickname, superpower, health_points, catchphrase, speed, damage):
#         super().__init__(name, nickname, superpower, health_points, catchphrase)
#         self.speed = speed
#         self.damage = damage
#     def km_h(self):
#         return f"skorost: {self.speed}"
#
#     def uron(self):
#         return f"uron: {self.damage}"
#
#
#
# Terminator = Earthhero("Arnold", "Terminator", "Strong", 100, "Hasta la vista, baby", 15, 10)
# print(Terminator.get_name())
# print(Terminator.km_h())
# print(Terminator.uron())
# print(Terminator.double_health_points())
# print(Terminator)
# print(Terminator.fly_phrase())
# print(f"dlina koronnoy frazy: {len(Terminator)}")
# #
# class Villain(Airhero):
#     people = "monster"
#
#     def ge(self, hero):
#         self.health_points -= self.damage
#         return f"zdorovye {self.name} umenshilos {self.damage}"
#
#     def crit(self):
#         return self.damage ** 2
#
# print(Villain.ge)


# инкапсуляция

# 1 - открытый, 2 - защищенный, 3 - скрытый
#
# class Student:
#     def __init__(self, name, age, id, group):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.group = group
#
#     def __str__(self):
#         return f"меня зовут {self.name}, мне {self.age} лет"
#
#     def __get_group(self):
#         return f"ты учишься в группе {self.group}"
#
#     def __sum_id(self):
#         return self.id * 2
#
#     @property
#     def sum_id_return(self):
#         return self.__sum_id
#
#
# ernist = Student("Ernist", 17, 2, "ИИ-3")
#
#
# print(ernist)
# print(ernist.sum_id_return())
# # print(ernist.__get_group())
# # print(dir(Student))
# # print(ernist._Student__get_group())

# создать класс Bank
# с защенными атрибутами (конструктора)
# name,balanse
#
# создать метод moneyX
# чтобы клиент мог добавить на свой счет еще денег (можно использовать инпут)
#
# создать защищенный метод kill
# чтобы клиент мог обнулить деньги
#
# cоздать СКРЫТЫЙ метод jackpot
# который умножает деньги на 10
#
# создать защищенный метод (название придумайте сами)
# который мог бы объеденить баланс одного объекта с текущим
# (допустим у меня на балансе есть 100
# и у вас есть 100 .вызвав этот метод у меня и указав вас он должен скопировать ваши деньги мне
# у вас так же 100 а у меня 200))

class Bank:

    def __init__(self, name, balance, balance2):
        self.name = name
        self.balance = balance
        self.balance2 = balance2

    def imya(self):
        return f"vashe imya: {self.name}"

    def moneyX(self):
        while True:
            add_ = int(input("ds: "))
            add_ += self.balance
            return f"vash balance: {self.balance} "

    def kill(self):
        self.balance = 0
        return f"vash balance obnulen {self.balance}"

    def jeckpot(self):
        self.balance *= 10
        return f"vash jeckpot {self.balance}"

    def combo_balance(self):
        self.balance = self.balance2
        self.balance += self.balance2
        self.balance2 = 0
        return f"vash balannce {self.balance}"

    def fs(self, other):
        if isinstance(other, Bank):
            self.balance += other.balance
            other.balance = 0
            print(f"Ваш новый баланс: {self._balance}")





Mbank = Bank("sa", 100, 100)

print(Mbank.imya())
print(Mbank.moneyX())
print(Mbank.jeckpot())
print(Mbank.combo_balance())
print(Mbank.fs())
print(Mbank.kill())

# class InstallmentPlan:
#     def __init__(self, price):
#         self.price = price
#
#
#     def calculate_total_cost(self):
#         return self.price
#
#
# class FixedInstallment(InstallmentPlan):
#     def __init__(self, price, months):
#         super().__init__(price)
#         self.months = months
#
#
#     def calculate_total_cost(self):
#         return self.price
#
#
# class VariableInstallment(InstallmentPlan):
#     def __init__(self, price, months, interest_rate):
#         super().__init__(price)
#         self.months = months
#         self.interest_rate = interest_rate
#
#
#     def calculate_total_cost(self):
#         return round(self.price * (1 + self.interest_rate / 100))
#
#
# fixed_plan = FixedInstallment(7000, 12)
# variable_plan = VariableInstallment(7000, 12, 5)
#
#
# print(f"Общая стоимость для фиксированного плана: {fixed_plan.calculate_total_cost()}")
# print(f"Общая стоимость для переменного плана: {variable_plan.calculate_total_cost()}")
#
#
#
#
#
