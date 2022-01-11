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
# 0. dict.get() = key값에 해당하는 값이 없으면 None을 리턴해서 오류가 발생하지 않음 >> 유용하게 씀
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


