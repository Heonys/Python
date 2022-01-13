from os import environ
import pygame
from pygame.constants import CONTROLLER_BUTTON_BACK, SCRAP_SELECTION

#초기화 반드시 한다고 생각
pygame.init() 

#화면설정
screen_widh = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_widh,screen_height))


# 화면 타이틀
pygame.display.set_caption("My First Game")

# FPS
clock = pygame.time.Clock()

# 배경이미지 불러오기
background = pygame.image.load("C:/Users/siwmu/Desktop/web/PythonWorkspace/Python/game/background.png")

# 캐릭터 불러오기
character = pygame.image.load("C:/Users/siwmu/Desktop/web/PythonWorkspace/Python/game/charater.png")
character_size = character.get_rect().size #이미지 크기를 구함
character_widh = character_size[0] #가로크기
character_height = character_size[1] #세로크기
character_x_pos = (screen_widh / 2) - (character_widh / 2) # 절반크기의 해당
character_y_pos = screen_height - character_height 


#이동할 좌표
to_x = 0
to_y = 0

#이공속도
character_speed = 0.6

# enemy 캐릭터
enemy = pygame.image.load("C:/Users/siwmu/Desktop/web/PythonWorkspace/Python/game/enemy.png")
enemy_size = character.get_rect().size #이미지 크기를 구함
enemy_widh = character_size[0] #가로크기
enemy_height = character_size[1] #세로크기
enemy_x_pos = (screen_widh / 2) - (character_widh / 2) # 절반크기의 해당
enemy_y_pos = (screen_height / 2)  - (enemy_height /2) 


# 폰트정의
game_font = pygame.font.Font(None, 40) # 폰트객체 생성(폰트, 크기)

#총 시간
total_time = 10

# 현재 tick 정보 받아옴
start_ticks = pygame.time.get_ticks() # 초기화된 이후로 부터 시간 






# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) # (델타) 초당 프레임수 성정 
    # print(f"fps : {str(clock.get_fps())}")
    for event in pygame.event.get(): # 어떤 이벤트야?
        if event.type == pygame.QUIT: #창이 닫힌다면?
            running = False #루프 종료


        if event.type == pygame.KEYDOWN: #키가 눌려졌나?
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed 
            elif event.key == pygame.K_UP:
                to_y -= character_speed 
            elif event.key == pygame.K_DOWN:
                to_y += character_speed


        if event.type == pygame.KEYUP: #방향키를 때면 멈춤
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or  event.key == pygame.K_DOWN:
                to_y = 0


    character_x_pos += to_x * dt # 프레임이 달라진다고 게임 속도가 달라지면 안되기 때문
    character_y_pos += to_y * dt 

    # x좌표의 경계값
    if character_x_pos < 0:
        character_x_pos = 0
    if character_x_pos > (screen_widh - character_widh):
        character_x_pos = screen_widh - character_widh

    # y좌표의 경계값 
    if character_y_pos < 0:
        character_y_pos = 0
    if character_y_pos > (screen_height - character_height):
        character_y_pos = screen_height - character_height


    #충돌 처리
    #캐릭터의 좌표가 움직이지만 실제 rectangle정보는 처음위치로 고정됨
    # 그래서 rectangle정보를 바꿔줘야함
    # 움직인 좌표로 캐릭터의 rectangle정보를 업데이트 해줌
    character_rect = character.get_rect() #캐릭터의 rectangle정보
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # enemy의 rectangle정보를 정해줌
    enemy_rect = enemy.get_rect() #캐릭터의 rectangle정보
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos


    #충돌 체크 
    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running = False



    screen.blit(background, (0,0)) #배경 그리기
    screen.blit(character, (character_x_pos,character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    #타이머 집어넣기
    #경과시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #초단위로 표시 
    # render() >> 실제로 글자를 s그리는 것
    timer = game_font.render(str(int(total_time - elapsed_time)),True,(255,255,255) )
    
    screen.blit(timer, (10,10))

    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False


    #================================================
    pygame.display.update() #게임화면을 다시그리기

# 잠시 대기
pygame.time.delay(2000) #2초대기 >>  ms단위라서 1000곱해줌


# 게임 종료
pygame.quit()



