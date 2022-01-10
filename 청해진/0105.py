# import random 

# kick = ['left','mid','right']

# user = random.sample(kick,1)
# computer = random.sample(kick,1)
# print("user:",user," computer:",computer)

# if computer == user:
#     print("패널티킥 성공")
# else:
#     print("패널티킥 실패")

# for i in range(5):
#     print("환영합니다.for")

# i = 0 
# while i< 5:
#     print("환영합니다.while")
#     i +=1


# list = ['Hello'] 

# for t in list:
#     print(t)

# print("========문제 3=========")
# for i in range(2,10):
#     for j in range(1,10):
#         print(i,"x",j,"=",i*j)


# print("========문제 4========")
# singer = ['BTS','TWICE','BLACKPINK','IU']
# for i in singer:
#     print("가수는:",i)



# dic = {1:'a',2:'b',3:'c'}

# for key,value in dic.items():
#     print("key:",key,"value:",value)




# def add(a,b):
#     return a+b


# def add2(*args):  #받은 값을 튜플로 만들어줌 
#     result = 0 
#     for i in args:
#         result += i
#     return result       

# for i in range(10,-1,-1):
#     print(i)


# import turtle

# t= turtle.Turtle()
# t.shape("turtle")

# s = turtle.textinput("turtle","몇 각형을 그리시겠습니까?")
# n = int(s)

# for i in range(n):
#     t.forward(10)
#     t.left(360/n)

# t.fillcolor("red")

import turtle as t
import random as rd

t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")

n1= rd.randrange(1,360)
n2= rd.randrange(1,360)
n3= rd.randrange(1,360)

t1.speed(0)
t2.speed(0)
t3.speed(0)





for i in range(1000):
  
    
    t1.penup()
    t1.goto(rd.randrange(-250,250),rd.randrange(-250,250))
    t1.left(360/rd.randrange(1,360))
    t1.pendown()

    t2.penup()
    t2.goto(rd.randrange(-250,250),rd.randrange(-250,250))
    t2.left(360/rd.randrange(1,360))
    t2.pendown()

    t3.penup()
    t3.goto(rd.randrange(-250,250),rd.randrange(-250,250))
    t3.left(360/rd.randrange(1,360))
    t3.pendown()
   


t1.done()


