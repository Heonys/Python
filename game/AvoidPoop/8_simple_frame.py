import pygame


pygame.init()  #초기화!! 반드시 한다고 생각

#화면설정
screen_widh = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_widh,screen_height))


# 화면 타이틀
pygame.display.set_caption("My  Game")

# FPS
clock = pygame.time.Clock()
#===================================================================


# 사용자 초기화 (배경, 이미지, 좌표, 속도, 시간, 폰트 등)



# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) # (델타) 초당 프레임수 성정 

    #이벤트 처리
    for event in pygame.event.get(): # 어떤 이벤트야?
        if event.type == pygame.QUIT: #창이 닫힌다면?
            running = False 




    #위치 정의(캐릭터, 경계값)

    #충돌 처리

    #화면에 그리기


    #================================================
    # 무조건 해야됨
    pygame.display.update() #게임화면을 다시그리기 



# 게임 종료
pygame.quit()



