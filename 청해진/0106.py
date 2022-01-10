# list = [1,2,3,4]

# for student in range(10):
#     if student in list:
#         print("ok")
#     else:
#         print("no")


# import random as rd 

# t = rd.randrange(1,50)

# ls = list(range(1,10))

# sample1 = rd.sample(ls,3)
# print(sample1)


# import turtle

# t = turtle.Turtle()
# t.speed(0)
# t.width(3)

# lengh = 10 

# while lengh < 500:
#     t.forward(lengh)
#     t.right(100)
#     lengh +=5




# import random 
# tries = 0 
# quess = 0
# answer = random.randint(1,100)
# print("1부터 100 사이의 숫자를 맞추시오")
# while quess != answer:
#     quess = int(input("숫자를 입력하시오: "))
#     tries = tries + 1
#     if quess < answer:
#         print("낮음!")
#     elif quess > answer:
#         print("높음")

# print("축하합니다. 총 시도횟수=",tries)

# breads = ["허니오트","하티","위트","화이트","파마산 오레가노","플랫브레드"]
# cheese = ["슈레드치즈","모짜렐라치즈","아메리칸치즈"]
# vegis = ["양상추","토마토","오이","피망","양파","피클","할라피뇨","아보카도","올리브"]
# sauces = ["랜치","마요네즈","스위트어니언","스위트칠리","핫칠리","머스타드"]

# print("서브웨이 가능한 조합")

# list = []

# 전화번호 생성기 

import random as rd
from typing import Type
import time 

com = ['SKT','KT ','LG ']
num = ''
count = 0
fina = 0

while True:

    num = num + str(rd.sample(com,1)) + " "

    while count < 8:
        if count == 4:
            num += ' '
        first = str(rd.sample(range(10),1))
        num += first
        count +=1 

    count = 0
    print(num)
    num = ''
    fina += 1 
    time.sleep(0.3)




