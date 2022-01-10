# bts = []
# bts.append("V")
# print(bts)
# bts.append("Jin")
# bts.append("Suga")
# print(bts)


# fruit = input("과일을 3개 입력해주세요 : ")
# print(fruit)


# like = 0
# list_f = []
# for i in range(3):
#     list_f.append(input("{}번째 과일을 입력하세요. ".format(i)))

# user_in = input("과일 이름을 입력하세요")
# for i in range(3):
#     if list_f[i] == user_in:
#         like = 1

# if like == 1:
#     print("이 과일은 당신이 좋아하는 과일입니다.")
# else:
#     print("좋아하지 않는 과일입니다.")


# list_s = [['kim', 28],['lee',32],['park',27]]

# max_0th = max( t[1] for t in list_s)


# print(max_0th)


# population = ['seoul', 9755, 'busan', 7334, 'daeheon', 5783]
# print("서울의 인구 :",population[1])
# print("대전의 인구 :",population[-1])
# print("도시 리스트 :",population[::2])
# print("인구의 합 :",sum(population[1::2]))

# test = ['a','b','c','d','e','f','g']
# test[2] = 'j'
# print(test)

# test[2:4] = [123,'z']
# print(test)
# test.insert(6,'gg')
# print(test)

# test.remove("g")
# print(test)
# del_t = test.pop()
# print(del_t)
# print(test)
# del test[0]
# print(test)

# import random

# tes = []
# tes.append("1 꿈을 지녀라")
# tes.append("2 분노는 바보")
# tes.append("3 귀중한 것은 하나도 없다")
# tes.append("4 사람은 사랑할 때")
# tes.append("5 시작이 반")

# print("#"*50)
# print(f"{'오늘의 명언': ^50}")
# print("#"*50)



# while True:

#     print('1. 명언 뽑기')
#     print('2. 명언 추가')
#     print('3. 종료')
#     num = int(input("번호입력 : "))

#     if num == 1:
#         daily =random.choice(tes)
#         print(daily) 
        
#     elif num == 2:
#         app = input("명언을 입력해주세요 : ")
#         tes.append(app)
        
#     elif num == 3:   
#         print("종료")
#         break
#     else:
#         print("오류")


# city = [('서울',9765),('부산',3441),('인천',2954),('광주',1501),('대전',1531)]



# # print(dict(city)['서울'])
# print(max(t[1] for t in city))


# print(f'최대인구 : {max(t[0] for t in city)}, 인구 : {max(t[1] for t in city)}천명')
# print(f'최소인구 : {min(t[0] for t in city)}, 인구 : {min(t[1] for t in city)}천명')
# print(f'리스트 도시 평균 인구 : {sum(t[1] for t in city) / len(city)}천명 ')


print(f'{"문제 1":#^50}')

fruit = ['orange','shine muscat','mango','tomato','banana']

len_list = list((len(t) for t in fruit))
max_len_index = len_list.index(max(len_list))
del fruit[max_len_index]
print(fruit)

print(f'{"문제 2":#^50}')
print(len_list)

print(f'{"문제 3":#^50}')













