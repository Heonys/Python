# 0. **kwargs >> 함수의 파라미터로 **을 주면 딕셔너리가 된다 
# 0. return >> return으로 함수를 즉시 빠져나가는 방법을 자주 사용한다, 
# 0. 항상변하는게 아닐때 함수의 매개변수 초기값 선언을 해준다 (매개변수=값)
#    단 초기화시키고 싶은 매개변수를 항상 뒤쪽 
# 0. input() + split() 으로 입력받은거 나눔 map()이나 강제형변환 응용해서씀
# 0. global >> 함수는 독립적으로 존재하는 것이 좋기 때문에 가급적 x 
# 
# 0. lamda >> 익명함수 ,함수가 복잡하지 않을때 함수를 한줄로 간결하게 만들때 사용 
#     ex) 메모리절약, 함수안에서 def를 사용하지 못할때 >> (lambda a, b : a+b)(3,4)
# 0.str.strip() >> 문자열 공백 제거 
# 0. sum(a) >> 리스트나 튜플의 합을 구함 sum(a,b) 이런식으로 쓰는 거 아님 
# 0. list.sort()  >> 리스트를 정렬해서 변환
#    sorted(list) >> 본체는 냅두고 정렬할 새로운 리스트 반환
# 0. 특이한 파이썬의 and, or 연산값 
# 0. ==는 값을 비고 is는 객체를 비교 (고유의 id값으로)
# 0. x in list, x not in list 값이 있는지 없는지 확인 (리스트, 문자열, 튜플, 딕셔너리, 집합 등)
# 0. 반복문에 else 사용가능 >> while의 else는 if때와 동일, for문은 모두 실행된 후 else 실행 
# 0. 재귀함수를 통해 점화식을 표현가능 
# 0. 딕셔너리는 요솟값을 구하려고할때 단한가지임 > KEY값을 이용한 방법 // 애초에 순서가 없어서 인덱스 사용 안됨
# 0. dict.get(key,n) = key값에 해당하는 값이 없으면 n을 리턴해서 오류가 발생하지 않음 >> n 생략하면 기본값은 none
# 0. pop() vs dell 차이 둘다 인덱스로 값을 지우지만 pop은 지운것을 반환 dell은 반환안함
#    remove() >> pop, dell과 다르게 값으로 지움, 중복시 먼저나온 값 // 3개다 원본 값을 바꾸기때문에 주의
# 0. 음수 index >> 맨 뒤부터 -1임 
# 0. 변수에 객체를 할당하면 네임스페이스 안에 저장 // 상위(밖)는 하위(안) 참조x  , 하위는 상위 참조가능 
# 0. packing >> 함수의 인자의 개수를 유연하게 해줌 def func(*args): print(args)  >> 매개변수 앞에 *
# 0. unpacking은 여러개의 객체를 포함하고 있는 하나의 객체를 풀어줌 >> 인자 앞에 * 
# 0. 에러발생시키기 > raise
# 0. 예외처리 >> try >>  except
# 0. 컴프리헨션 >> [x for x in range(10)] 와 같이 간단히 줄여쓰도록 지원하는 것 
# 0. 컴프리헨션 문법을 사용하면 제너레이터가 생성됨  >> 리스트는 평가되있기 때문에 제너레이터 생성x 
# 0. 제너레이터는 기억하지않는 1회용 이라서 소비되고 next(gen) 함수로 하나씩 사용가능 

# 비교적 자주쓰는 내장함수!~
# 0. abs() > 절대값 // all() > iterable자료형의 각항들이 전부 참일때 만 참 // any() > 하나라도 참이면 참 all()과 반대
#    divmod(a, b) > a/b, a%b를 튜플로 반환 // filter() > map()과 문법 동일 조건에 의해 iterable자료형을 걸러내는 함수 (for문과 같이씀)
#    hex() > 16진수 // oct() > 8진수 // pow(x, y) > x의 y제곱
#
# 0. list(range(5, 10)) [5, 6, 7, 8, 9]
# 0. enumerate() // 주로 for문과 같이사용하여 iterable자료형을 (인덱스 , 값 ) 의 튜플로 반환 
# 0. pickle 모듈 사용하기 // pickle.dump(data, file) 넣기 pickle.load(file)로 불러오기
# 0. time.sleep(1) // 잠시 재우기  time.ctime() // 현재시간
# 0. random.randint(1, 10) // 1 ~ 10 무작위 난수 // choice > 무작위 가져옴 // shuffle 섞기
# 0. join() >>  '구분자'.join(리스트)
# 0. 예외처리시 에러 발생하는 순간 탈출 후 finally
#  



#+===================================================================



# def print_kwargs(**kwargs):
#       print(kwargs)
# print_kwargs(a='python',b='javascript')

# def say_nick(nick):
#     if nick == "바보":
#         return
#     print(f'나의 별명은{nick}입니다.')


# def say_myself(name, old, man=True): 
#     print("나의 이름은 %s 입니다." % name) 
#     print("나이는 %d살입니다." % old) 
#     if man: 
#         print("남자입니다.")
#     else: 
#         print("여자입니다.")

# say_myself("박응용", 27)
# say_myself("박응용", 27, True)


# target = ['  cat ', ' tiger ', '    dog', 'snake   ']

# def my_key(string):
#      return len(string.strip())


# print(sorted(target, key=my_key))
# ====================================================

# class Calc:

#     #생성자
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
        
#     def add(self):
#         return self.first + self.second
#     def mul(self):
#         return self.first - self.second
#     def sub(self):
#         return self.first * self.second
#     def div(self):
#         return self.first / self.second


# calc = Calc(12,3)
# print(calc.add())
# print(calc.mul())
# print(calc.sub())
# print(calc.div())

# class MoreCalc(Calc):
#     def __init__(self, first, second):
#         super().__init__(first, second)
    
#     def more(self):
#         return self.first ** self.second
        
# more = MoreCalc(12,3)

# print(more.more())


# nan = enumerate(['a','b','c'])
# print(type(nan))

#######################1번#############
# a:b:c:d  >> a#b#c#d
# 문자열의 split와 join 함수를 사용하여 위 문자열을 다음과 같이 고치시오.

# str = 'a:b:c:d'
# str_split = list(str.split(':'))

# print("#".join(str_split))


#######################2번#############
#C에 해당하는 값이 없을 경우 70반환 

# class MyError(Exception):
#     pass


# a = {'A':90, 'B':80}
# print(a.get('Z','없음'))

#######################4번#############

# a1 = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

# a2 = filter(lambda x:x>=50,a1)
# print(sum(a2))

#######################5번#######################################
#0, 1, 1, 2, 3, 5, 8, 13, ...

# def fib(num):
#     if num == 1:
#         return 0 
#     elif num == 2:
#         return 1
#     else:
#         return fib(num-1) + fib(num-2)


# def fib_list(num):
#     return [fib[i+1] for i in range(num)] # 에러
#     # print([ fib(i+1) for i in range(num)])

# print(fib_list(3))


#######################6번#############
#65,45,2,3,45,8

# def sum_list(*args):
#     print(sum(args))

# sum_list(65,45,2,3,45,8)

######################7번#############
# 구구단을 출력할 숫자를 입력하세요(2~9): 2
# 2 4 6 8 10 12 14 16 18

# i = int(input("몇단 : "))
# for j in range(1,10):
#     print(f'{i*j}',end=" ")

######################8번#############
# str_abc = """
# DDD
# EEE
# CCC
# BBB
# AAA
# """

# with open("abc.txt","w") as str_file:
#     str_file.write(str_abc)


######################13번#############

# DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤 문자열 안에서 홀수가 연속되면 두 수 사이에 - 를 추가하고,
#  짝수가 연속되면 * 를 추가하는 기능을 갖고 있다. DashInsert 함수를 완성하시오.

# 입력 예시: 4546793
# 출력 예시: 454*67-9-3

