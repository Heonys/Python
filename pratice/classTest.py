# # 기본유닛
# from _typeshed import StrPath


# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#         print("{} 유닛 생성".format(self.name))


#     def move(self,location):
#         print("{name}은 {location}로 이동합니다.".format(name=self.name,location=location))

# #공중 유닛
# class Flyable():
#     def __init__(self, flyspeed):
#         self.flyspeed = flyspeed

# #공격 가능 유닛

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         super().__init__(name, hp)
#         self.damage = damage
#         print("공격력 {} 입니다".format(self.damage))

#     def moveAttack(self, location):
#         print("{name}은 {location}로 공격합니다.".format(name=self.name, location=location))


# #공중 공격 유닛 
# class FlyableAttack(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flyspeed):
#         super().__init__(name, hp, damage)

#         Flyable.__init__(self, flyspeed)
    

# #레이스 생성
# unit2 = FlyableAttack("레이스",30,10,4)


# 강남 / 아파트 / 매매 // 10억 / 2010년

# class House():
#     def __init__(self, location, house_type, deal_type, price, year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.year = year

#     def show_detail(self):
#         print("{} {} {} {} {}".format(self.location,self.house_type \
#             , self.deal_type, self.price, self.year))

    

# house1 = House("강남","아파트","매매","10억","2010년")
# house1.show_detail()


# ================= 예외처리 ==============================

try:
    print("한자리수 전용 나누셈 입니다.")
    num1 = int(input("첫번째 숫자를 입력해주세요"))
    num2 = int(input("두번째 숫자를 입력해주세요"))

    if num1>=10 or num2>=10:
        raise ValueError
    print("{0} 나누기 {1}는 {2}입니다.".format(num1,num2,num1/num2))
except ValueError:
     print("한자리수를 입력해주세요")