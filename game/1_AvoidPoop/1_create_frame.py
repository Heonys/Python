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

# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

# 게임 종료
pygame.quit()



