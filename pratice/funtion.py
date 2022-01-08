#   1.  함수 기본값 >>매개변수 = 값

#   2. 키워드값으로 호출  funtion(name= x, age= y)
#    키워드로하면 뒤죽박죽으로 호출해도됨 

#   3. 가변인자  >> (* + 매개변수)
# 
#   4. 전역변수 , 지역변수
#   전역변수 선언 global

#  5. round  함수 >> 소수점 몇자리만 표시

# def fun(x,*y):
#     print(x)
#     print([i for i in y]) # 한줄 for문 

# fun(3,1,2,3)    

# scores = {'math':50,'korean':10,'codding':100}

# for subject, score in scores.items():
#     print(subject.ljust(8),str(score).rjust(8), sep=":")


# for i in range(1,21):
#     print("대기번호",str(i).zfill(3),sep=" : ")



# 6. ljust(x) 왼쪽 정렬 rjust(x) 오른쪽 정렬 >> x만큼 공간 확보
#    
# 7. sep= "", end="" 표준입출력 
# 
# 8. zfill(x) >> x만큼 공간확보하고 빈공간은   0채우기
#
# 
# 9. 다양한 출력포멧 ex) {0:,} >> 천의자리마다 , 찍어줌
#       {0: >10} >> 빈공간 공백으로 오른쪽 정렬 공간 10만큼
# 
# 
# 10. 파일 입출력 옵션 w는 덮어쓰기 a는 apend 추가하기




# end



# openfile = open("openfle.txt","w",encoding="utf8")
# print("수학: 10", file=openfile)
# print("영어: 20", file=openfile)
# openfile.close()

# openfile = open("openfle.txt","a",encoding="utf8")
# openfile.write("\n어팬드 테스트")
# openfile.write("\n잘되네")
# openfile.close()


# openfile = open("openfle.txt","r",encoding="utf8")
# print(openfile.read())


# import pickle

# # picklefile = open("pickle.pickle", "wb")
# # list = ["유재석","박명수","정형돈","길"]
# # pickle.dump(list,picklefile)
# # picklefile.close()


# picklefile = open("pickle.pickle", "rb")
 
# print(pickle.load(picklefile))

# picklefile.close()

# import pickle

# with open("pickle.pickle","rb") as picklefile:
#     print(pickle.load(picklefile))

# with open("with.txt","w",encoding="utf8") as withfile:
#     withfile.write("with로 텍스트 쓰기")


# 11. __init__ 파이썬의 생성자

# 12. pass >> 넘김 throws과 같은 느낌

# 13. 클래스를 만들면 반드시 생성자로 초기화 여기서 self 반드시 체크 
#     상속을 했으면 상속한거 전부 초기화



# with open("openfile.txt","a",encoding="utf8") as openfile:
#     openfile.write("22widh 써서 넘기기")


# class Color():
#     def __init__(self,name):
#         self.name = name

#     def __repr__(self):
#         return "나는 {} 입니다.".format(self.name)
        
#     # def __str__(self):
#     #     return f'__str__: {self.name=}'
    
#     # def __repr__(self):
#     #     return f'__repr__: {self.name=}'


# red = Color('red')
# yellow = Color('yellow')
# black = Color('black')

# arr = [red, yellow, black]

# for ar in arr:
#     print (ar)
