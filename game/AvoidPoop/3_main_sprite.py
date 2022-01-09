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

# 캐릭터 불러오기
character = pygame.image.load("C:/Users/siwmu/Desktop/web/PythonWorkspace/Python/game/chacrater.png")
character_size = character.get_rect().size #이미지 크기를 구함
character_widh = character_size[0] #가로크기
character_height = character_size[1] #세로크기
character_x_pos = (screen_widh / 2) - (character_widh / 2) # 절반크기의 해당
character_y_pos = screen_height - character_height 








# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    screen.blit(background, (0,0)) #배경 그리기
    screen.blit(character, (character_x_pos,character_y_pos))

    pygame.display.update() #게임화면을 다시그리기


# 게임 종료
pygame.quit()



