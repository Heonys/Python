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


# 공 만들기 (4개 처리)

ball_imgaes = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]

# 공 크기에 따라 속도가 다름
ball_speed_y = [-18, -15, -12, -9]

# 공 
balls = []

balls.append({
    'pos_x' : 50, # x좌표
    'pos_y' : 50, # y좌표
    'img_idx' : 0, # 공의 이미지 인덱스
    'to_x' : 2,   # x축 이동방향
    'to_y' :-6,   # y축 이동방향
    'init_speed_y' : ball_speed_y[0] #최초속도
})

# 사라질 무기, 공 저장 변수
weapon_to_remove = -1
ball_to_remove = -1





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
                weapon_x_con = character_x_con + (character_widh/2) - (weapon_widh/2)
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
    

    # 공 위치 정의

    for ball_index, ball_val in enumerate(balls):
        ball_pos_x = ball_val['pos_x']
        ball_pos_y = ball_val['pos_y']
        ball_img_idx = ball_val['img_idx']

        ball_size = ball_imgaes[ball_img_idx].get_rect().size
        ball_widh = ball_size[0]
        ball_height = ball_size[1]

        # 가로 벽(x)축 에 닿았을때의 공 이동방향 반대로 
        if ball_pos_x < 0 or ball_pos_x > (screen_widh - ball_widh):
            ball_val['to_x'] *= -1 

        # 세로 (y)축 처리 >> stage에 튕기면 속도가 줄어들어야됨
        if ball_pos_y >= screen_height - stage_height - ball_height: #닿은순간의 y좌표
            ball_val['to_y'] = ball_val['init_speed_y']
        else:
            ball_val['to_y'] += 0.5
            
        ball_val['pos_x'] += ball_val['to_x']
        ball_val['pos_y'] += ball_val['to_y']

 
    #충돌 처리 
    character_rect = character.get_rect()
    character_rect.left = character_x_con 
    character_rect.top = character_y_con 

    for ball_index, ball_val in enumerate(balls):
        ball_pos_x = ball_val['pos_x']
        ball_pos_y = ball_val['pos_y']
        ball_img_idx = ball_val['img_idx']

        # 공 rect 정보 업데이트
        ball_rect = ball_imgaes[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # 공과 캐릭터의 충돌 처리 
        if character_rect.colliderect(ball_rect):
            running = False
            break


        # 무기는 한발이 아니라 여러발을 쏴서 리스트로 관리 하기 때문에
        # 공과 여러발의 무기 처리 
        for weapon_inx, weapon_val in enumerate(weapons):
            #웨폰 현재 좌표 가져오기
            weapon_x_con = weapon_val[0]
            weapon_y_con = weapon_val[1]

            # 웨폰 rect 정보 업데이트 
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_x_con
            weapon_rect.top = weapon_y_con

            #충돌 체크 >> 충돌시 공과 그 충돌한 무기도 없애야함 
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_inx
                ball_to_remove = ball_index
                break


    # 충돌된 공, 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1 
    
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1  
    
        


    #화면에 그리기
    screen.blit(background,(0,0))

    for weapon_x_con, weapon_y_con in weapons:
        screen.blit(weapon, (weapon_x_con, weapon_y_con))

    for idx, val in enumerate(balls):
        ball_pos_x = val['pos_x']
        ball_pos_y = val['pos_y']
        ball_img_idx = val['img_idx']
        screen.blit(ball_imgaes[ball_img_idx], (ball_pos_x, ball_pos_y))

    
    screen.blit(stage,(0,(screen_height - stage_height)))
    screen.blit(character,(character_x_con, character_y_con) )


    #================================================
    # 무조건 해야됨
    pygame.display.update() #게임화면을 다시그리기 



# 게임 종료
pygame.quit()



