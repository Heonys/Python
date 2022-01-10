#   1.  함수 기본값 >>매개변수 = 값

#   2. 키워드값으로 호출  funtion(name= x, age= y)
#    키워드로하면 뒤죽박죽으로 호출해도됨 

#   3. 가변인자  >> (* + 매개변수)


#  5. round  함수 >> 소수점 몇자리만 표시

# ==========================================================================
# def basic(name ='xx', age = 3):
#     print(name,age)


# def calculate_area(radius):
#     area = 3.14 * radius**2
#     return area

# result = calculate_area(5)
# print(result)


# def get_sum(start, end):
#     s = 0
#     for i in range(start, end+1):
#         s += 1
#     return s 

# print (get_sum(1,10))
# x = get_sum(1,10)
# print('x =',x)

# y = get_sum(1,20)
# print("y =",y)
#===================================================
# from math import pi
# import turtle
# import random as rd


# t= turtle.Turtle()
# t.shape("turtle")

# t.speed(0)

# while True:
#     pos1 = rd.randrange(-300,300)
#     pos2 = rd.randrange(-300,300)
#     color = ['red','pink','tomato','aqua','blue']
    
#     t.width(5)
#     t.penup()
#     t.goto(pos1,pos2)
#     t.pendown()  
   
#     t.circle(10,steps=rd.randrange(3,10))

#     t.begin_fill()
#     t.color(rd.sample(color,1))
#     t.end_fill()

# import math 

# def print_counter():
#     global counter
#     counter = 200
#     print('counter =',counter)

# counter = 100
# print_counter()
# print('counter =', counter)

# #========================================
# print('='*30)

# def calculate_area(radius):
#     global area
#     area = 3.14 * radius **2
#     return

# area = 0 
# r = float(input('원의 반지름: '))
# calculate_area(r)
# print(round(area,2))

# def weeklypay(rate,hour):
#     if(hour>48):
#         money = rate*48 + 1.5*rate*(hour-48)
#     else:
#         money = rate*hour
#     return money
# r = int(input("시급을 입력하세요: "))
# h = int(input("근무 시간을 입력하시오: "))
# print("주급은",str(weeklypay(rate=r,hour=h)))

# import turtle

# def drawBar(height):
#     t.begin_fill()
#     t.lt(90)
#     t.fd(height)
#     t.write(str(height),font=("times new roman",16,'bold'))
#     t.write(90)
#     t.fd(40)
#     t.rt(90)
#     t.fd(height)
#     t.lt(90)
#     t.end_fill()

# data = [120,56,390,220,156,23,98]

# t = turtle.Turtle()
# t.color("tomato")
# t.fillcolor("pink")
# t.pensize(3)

# for d in data:
#     drawBar(d)

# turtle.done()

print("========== 문제 1 ==========")
def maxNum(n1, n2, n3):
    list = [n1,n2,n3] 
    print("최대값:",max(list))

def minNum(n1, n2, n3):
    list = [n1,n2,n3]
    print("최소값:",min(list))

maxNum(3,4,5)
minNum(3,4,5)

print("========== 문제 2 ==========")
#(섭씨온도 × 1.8) + 32 = 화씨온도

def change(temp):
    print("섭씨온도{0}는 화씨온도{1} 입니다.".format(temp,round((temp*1.8) + 32)))

change(67)


print("========== 문제 3 ==========")

def triangle(length):
    for i in range(3):
        t.fd(length)
        t.lt(120)


import turtle
t = turtle.Turtle()
t.shape("turtle")

triangle(100)
