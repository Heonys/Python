import pygame
from pygame.constants import SCRAP_SELECTION

#초기화 반드시 한다고 생각
pygame.init() 

#화면설정
screen_widh = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_widh,screen_height))


# 화면 타이틀
pygame.display.set_caption("My First Game")

# 배경이미지 불러오기
background = pygame.image.load("C:/Users/siwmu/Desktop/web/PythonWorkspace/Python/game/background.png")

 


# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    screen.blit(background, (0,0)) #배경 그리기

    pygame.display.update() #게임화면을 다시그리기


# 게임 종료
pygame.quit()



