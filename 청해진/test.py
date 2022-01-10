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


target = ['  cat ', ' tiger ', '    dog', 'snake   ']

def my_key(string):
     return len(string.strip())


print(sorted(target, key=my_key))