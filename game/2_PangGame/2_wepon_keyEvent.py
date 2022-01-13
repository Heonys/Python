import pygame
import os



pygame.init()  #초기화!! 반드시 한다고 생각

#화면설정
screen_widh = 640 #가로
screen_height = 480 #세로
screen = pygame.display.set_mode((screen_widh,screen_height))


# 화면 타이틀
pygame.display.set_caption("My Pang")

# FPS
clock = pygame.time.Clock()
#===================================================================

# 사용자 초기화 (배경, 이미지, 좌표, 속도, 시간, 폰트 등)





#경로설정
current_path = os.path.dirname(__file__) #os모듈 > 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images")

#배경
background = pygame.image.load(os.path.join(image_path, "background.png"))

#스테이지
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_height = stage.get_rect().size[1] 

#캐릭터
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_widh = character_size[0] 
character_height = character_size[1] 
character_x_con = (screen_widh/2 - character_widh/2)
character_y_con = (screen_height - stage_height - character_height)
character_speed = 0.3

character_x = 0
character_y = 0

#무기 
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect()
weapon_widh = weapon_size[0]
#여러발 발사가능 하다 
weapons = []
weapon_speed = 2



# 이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) # (델타) 초당 프레임수 성정 

    #이벤트 처리
    for event in pygame.event.get(): # 어떤 이벤트야?
        if event.type == pygame.QUIT: #창이 닫힌다면?
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                character_x += character_speed
            elif event.key == pygame.K_LEFT:
                character_x -= character_speed
            elif event.key == pygame.K_SPACE: #무기 발사
                weapon_x_con = character_x_con + (character_widh / 2) - (weapon_widh / 2)
                weapon_y_con = character_y_con
                weapons.append([weapon_x_con, weapon_y_con])
                
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                character_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                character_y = 0


    #위치 정의(캐릭터, 경계값)

    character_x_con += character_x *dt
    character_y_con += character_y *dt

    if character_x_con > (screen_widh - character_widh):
        character_x_con = (screen_widh - character_widh)
    elif character_x_con < 0:
        character_x_con = 0 
        
    #무기 위치정의
    # 무기가 위로 올라가니까 x좌표는 그대로고 y는 속도 만큼 빼줘야댐 
    weapons = [(w[0], w[1] - weapon_speed) for w in weapons]

    #천장에 무기가 닿으면 없애기
    weapons =  [(w[0], w[1]) for w in weapons if w[1] > 0 ]
    



 
    #충돌 처리 






    #화면에 그리기
    screen.blit(background,(0,0))

    for weapon_x_con, weapon_y_con in weapons:
        screen.blit(weapon, (weapon_x_con, weapon_y_con))
    
    screen.blit(stage,(0,(screen_height - stage_height)))
    screen.blit(character,(character_x_con, character_y_con) )


    #================================================
    # 무조건 해야됨
    pygame.display.update() #게임화면을 다시그리기 



# 게임 종료
pygame.quit()



