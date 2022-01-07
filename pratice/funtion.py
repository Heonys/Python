#   1.  함수 기본값 >>매개변수 = 값

#   2. 키워드값으로 호출  funtion(name= x, age= y)
#    키워드로하면 뒤죽박죽으로 호출해도됨 

#   3. 가변인자  >> (* + 매개변수)
# 
#   4. 전역변수 , 지역변수
#   전역변수 선언 global

#  5. round  함수 >> 소수점 몇자리만 표시

def fun(x,*y):
    print(x)
    print([i for i in y])




fun(3,1,2,3)    