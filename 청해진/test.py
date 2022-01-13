#0. 한줄 if문 1) if '조건' : '참'
#             2) '참' if '조건' else '거짓' 


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

# # enumerate(list) (index, value)
# list = ['a','b','c']


# data = '4546793'
# data_list = list(map(int,data)) #[4, 5, 4, 6, 7, 9, 3]
# result = []

# for index, number in enumerate(data_list):
#     result.append(str(number))
#     if index < len(data_list)-1:
#         number_odd = (data_list[index] % 2 == 1) #홀:true 짝:false 
#         number_next_odd = (data_list[index+1] % 2 == 1)
#         if number_odd == number_next_odd:
#             if number_odd == True:
#                 result.append('-')
#             else:
#                 result.append('*')

# # "".join(result)

# print(result)
# print(''.join(result))


######################14번##  문자열 압축하기    ###########

# 문자열을 입력받아 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시해 문자열을 압축하여 표시하시오.

# 입력 예시: aaabbcccccca
# 출력 예시: a3b2c6a1

# data = 'aaabbcccccca'
# data_list = list(data) #['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'a']
# result = []

# ====================================================================

# 0~9의 문자로 된 숫자를 입력받았을 때,
# 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.

# 입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
# 출력 예시: True False False True False

# data = '0123456789'
# print(f'data의 길이 = {len(data)}')
# print(f'{set(data)} 의 길이 {len(set(data))}')

# def one_check(str):
#     str_len = len(str)
#     set_len = len(set(str))
#     if str_len == set_len:
#         if str_len == 10:
#             print("True")
#         else:
#             print("중복은 없지만 0~9를 모두 사용하지 않음 False")
#     else:
#         print("False")
        
      
# one_check("0123456789")
# one_check("01234567890")
# one_check("6789012345")
# one_check("012322456789")
# one_check("01234")
# # True False True False False


# 0~9의 문자로 된 숫자를 입력받았을 때, 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인하는 함수를 작성하시오.

# 입력 예시: 0123456789 01234 01234567890 6789012345 012322456789
# 출력 예시: True False False True False



# s = "aaaabbbcczzzza"

# #초기값을 설정합니다.
# result = s[0] #반복문 실행되는 동안 문자열 형태로 반환되는 결과들을 담을 변수
# count = 0 #반복되서 나오는 문자 수만큼 카운팅되는 값을 담을 변수

# for i in s:
#     if i == result[-1]: #result변수 마지막 문자와 비교합니다. else에서 result변수에 값이 추가되기 때문에 마지막 문자[-1]와 비교.
#         count += 1
#     else:
#         result += str(count) + i #마지막 글자와 i가 다를 경우 카운팅된 값을 문자열 형태로 result 변수 마지막에 추가 해주고 i를 마지막 문자로 추가합니다.
#         count = 1
# result += str(count) #결과들이 담긴 변수에 마지막으로 카운팅된 값을 문자열 형태로 추가합니다.

# print(result)


# 입력 예시: aaabbcccccca
# 출력 예시: a3b2c6a1

# def str_remove(string): #[1,1,3]
#     new_string = '' #새로 담을 문자열
#     count = 1
#     string = string + '\0'
    
#     for i in range(1,len(string)): #1,2, 
#         print(f'{i}번째{string[i-1]} {string[i]}')
#         if string[i-1] == string[i]:
#             count += 1
#         else:
#             new_string = new_string + string[i-1] + str(count) + str_remove(string[i:])
#             break
#     return new_string

# print(str_remove('aabbbcczzzza'))



# def stringCompress_rec(string):
#     ans = '' # 새로만들 변수
#     count = 1
#     string = string + '\0'
#     print(string)
#     for i in range(1, len(string)): # 1 ~ 10  
#         if string[i - 1] == string[i]: #현재 값과 다음값이 같으면 
#             count += 1
#         else:
#             ans += string[i - 1] + str(count) + stringCompress_rec(string[i:])
#             break
#     return ans

# print(stringCompress_rec('bbbcczzzza'))


# data = "aabbbcczzzza"
# new_data = '' # 새로운 문자열 
# count = 0
# new_data += data[0]

# for i in data:
#     if i == new_data[-1]:
#         count += 1
#     else:
#         new_data += str(count) + i
#         count = 1
# new_data += str(count)

# print(new_data)

# lis = [1,2,3]
# st = '123'

# # print(lis[-1])
# print(lis[:-1])


# 1. 참만 있을때 
# a = 3
# if a > 1:
#     print("참")

# if print("참") :
#     pass
#  10 if x > 0 else 20
# if print('참') a > 1 else print("거짓")
# if a>1 : print("참")

# print("참") if a>1 else print("거짓")
# print("참") if a<1 else print("거짓")

# a = 3 
# if a > 1:
#     print("참")

# if a > 1 : print("참")


# out_for = [1, 2, 3, 4] 
# in_for = [11, 22, 3, 44]

# for out_val in out_for:
#     for in_val in in_for:
#         if out_val == in_val:
#             print("충돌")
#             break
#     else:
#         continue
#     break
        
