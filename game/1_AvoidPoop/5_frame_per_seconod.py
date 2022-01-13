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
character = pygame.image.load("C:/Users/siwmu/Desktop/web/PythonWorkspace/Python/game/chacrater.png")
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




    screen.blit(background, (0,0)) #배경 그리기
    screen.blit(character, (character_x_pos,character_y_pos)) # 캐릭터 그리기
    
    pygame.display.update() #게임화면을 다시그리기


# 게임 종료
pygame.quit()



