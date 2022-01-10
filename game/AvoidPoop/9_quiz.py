import pygame
import random as rd

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
background = pygame.image.load("C:/Users/siwmu/Desktop/web/PythonWorkspace/Python/game/AvoidPoop/background.png")



charater = pygame.image.load("C:/Users/siwmu/Desktop/web/PythonWorkspace/Python/game/AvoidPoop/charater.png")
charater_size = charater.get_rect().size
charater_widh = charater_size[0]
charater_height = charater_size[1]
charater_x_pos = screen_widh/2 - (charater_widh/2)
charater_y_pos = screen_height - charater_widh 

charater_speed = 0.3
to_x = 0
to_y = 0

game_font = pygame.font.Font(None,40) 
total_time = 60
start_ticks = pygame.time.get_ticks() # 초기화된 이후로 부터 시간 



enemy = pygame.image.load("C:/Users/siwmu/Desktop/web/PythonWorkspace/Python/game/AvoidPoop/enemy.png")
enemy_size = charater.get_rect().size
enemy_widh = charater_size[0]
enemy_height = charater_size[1]
enemy_x_pos = rd.randrange(0,screen_widh)
enemy_y_pos = 0
enemy_speed = 10


# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) # (델타) 초당 프레임수 성정 

    #이벤트 처리
    for event in pygame.event.get(): # 어떤 이벤트야?
        if event.type == pygame.QUIT: #창이 닫힌다면?
            running = False 


        #위치 정의(캐릭터, 경계값)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= charater_speed
            elif event.key == pygame.K_RIGHT:
                to_x += charater_speed





        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

        



    charater_x_pos += to_x * dt
    charater_y_pos += to_y * dt   

    enemy_y_pos += enemy_speed

    if charater_x_pos <= 0:
        charater_x_pos = 0
    elif charater_x_pos >= screen_widh - charater_widh:
        charater_x_pos = screen_widh - charater_widh

    if charater_y_pos <= 0:
        charater_y_pos = 0
    elif charater_y_pos >= screen_height - charater_height:
        charater_y_pos = screen_height - charater_height
#=========================================================

    if enemy_x_pos <= 0:
        enemy_x_pos = 0
    elif enemy_x_pos >= screen_widh - enemy_widh:
        enemy_x_pos = screen_widh - enemy_widh

    # if enemy_y_pos <= 0:
    #     enemy_y_pos = 0
    # elif enemy_y_pos >= screen_height - enemy_height:
    #     enemy_y_pos = screen_height - enemy_height

    if enemy_y_pos >= screen_height:
        enemy_x_pos = rd.randrange(0,screen_widh)
        enemy_y_pos = 0

    #충돌 처리
    charater_rect = charater.get_rect() 
    charater_rect.left = charater_x_pos 
    charater_rect.top = charater_y_pos

    
    enemy_rect = enemy.get_rect() 
    enemy_rect.left = enemy_x_pos 
    enemy_rect.top = enemy_y_pos

    if charater_rect.colliderect(enemy_rect):
        print("충돌")
        running = False        



    #화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(charater,(charater_x_pos,charater_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))

    #경과시간
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 
    timer = game_font.render(str(int(total_time - elapsed_time)),True,(255,255,255))

    screen.blit(timer,(10,10))

    if total_time - elapsed_time <=0:
        print('시간초과')
        running = False
        







    #================================================
    # 무조건 해야됨
    pygame.display.update() #게임화면을 다시그리기 



# 게임 종료
pygame.quit()



