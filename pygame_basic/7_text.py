import pygame

pygame.init() # 초기화 (반드시 필요) pygame을 import하면 init은 무조건 해준다.

# 화면 크기 설정
screen_width=480  # 가로크기
screen_height=640
screen=pygame.display.set_mode((screen_width,screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("Yeom Game")  # 게임이름


# FPS
clock=pygame.time.Clock()


# 배경 이미지 불러오기
background=pygame.image.load("C:\\Users\\johny\\Desktop\\pythonworkplace\\pygame_basic\\background.png")


# 캐릭터(스프라이트) 불러오기
character=pygame.image.load("C:\\Users\\johny\\Desktop\\pythonworkplace\\pygame_basic\\enemy.png")
character_size=character.get_rect().size    # 이미지의 크기를 구해옴.
character_width=character_size[0]  # 캐릭터의 가로 크기
character_height=character_size[1]  # 캐릭터의 세로 크기
character_x_pos=screen_width/2-(character_width/2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos=screen_height-character_height  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x=0
to_y=0

# 이동속도
character_speed=0.6


# 적 enemy 캐릭터
enemy=pygame.image.load("C:\\Users\\johny\\Desktop\\pythonworkplace\\pygame_basic\\character.png")
enemy_size=enemy.get_rect().size    # 이미지의 크기를 구해옴.
enemy_width=enemy_size[0]  # 캐릭터의 가로 크기
enemy_height=enemy_size[1]  # 캐릭터의 세로 크기
enemy_x_pos=screen_width/2-(enemy_width/2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치
enemy_y_pos=(screen_height/2)-enemy_height


# 폰트 정의
game_font=pygame.font.Font(None, 40)  # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time=10

# 시작 시간
start_ticks=pygame.time.get_ticks()  # 시작 tick을 받아옴



# 이벤트 루프: 프로그램이 종료되지 않도록 계속 대기하는 것.
# 중간에 사용자가 키보드를 입력하는 지, 마우스로 클릭을 하는 지 체크를 한다.
running=True   # 게임이 진행중인가?
while running:
    dt=clock.tick(60)   # 게임화면의 초당 프레임 수를 설정
    # print("FPS: " + str(clock.get_fps()))

    # 캐릭터가 1초 동안에 100만큼 이동을 해야함
    # 10 fps: 1초 동안에 10번 동작 -> 1번에 10만큼 이동 -> 10*10=100
    # 20 fps: 1초 동안에 20번 동자 -> 1번에 5만큼 이동 -> 20*5=100
    for event in pygame.event.get():   # pygame을 하려면 무조건 적어야 하는 코드 (깊게 몰라도 된다.) # 어떤 이벤트가 발생했는가?
        if event.type==pygame.QUIT:    # 창이 닫히는 이벤트가 발생했는가?
            running=False

        if event.type==pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key==pygame.K_LEFT:
                to_x-=character_speed   
            if event.key==pygame.K_RIGHT:
                to_x+=character_speed
            if event.key==pygame.K_UP:
                to_y-=character_speed
            if event.key==pygame.K_DOWN:
                to_y+=character_speed

        if event.type==pygame.KEYUP:    # 방향키를 떼면 멈춤
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0
            elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                to_y=0
             
    character_x_pos+=to_x*dt    # 프레임이 달라진다고 게임의 속도가 달라지면 안되기 때문에 dt를 곱하여 보정해줌.
    character_y_pos+=to_y*dt    # 프레임을 바꿔서 실행해보면 같은 거리를 이동할 때의 속도는 같다.


    # 가로 경계값 처리
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width

    # 세로 경계값 처리
    if character_y_pos<0:
        character_y_pos=0
    elif character_y_pos>screen_height-character_height:
        character_y_pos=screen_height-character_height

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos

    enemy_rect=enemy.get_rect()
    enemy_rect.left=enemy_x_pos
    enemy_rect.top=enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running=False




    screen.blit(background, (0,0))     # 배경 그리기
    
    screen.blit(character,(character_x_pos,character_y_pos))  # 캐릭터 그리기

    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))  # 적그리기
    
    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time=(pygame.time.get_ticks()-start_ticks)/1000 
    # 경과 시간(ms)을 1000으로 나누어서 초 단위로 표시

    timer=game_font.render(str(int(total_time-elapsed_time)),True,(255,255,255))  #render: 실제로 이제 글자를 그리는 것 # int: 초로 표시했을 때 뒤에 나오는 소수점은 모두 없애기 위해. str: render뒤에 문자가 들어올 수 있도록 하기 위함.
    # render뒤에 들어가는 정보 = 출력할 글자, True, 글자 색상

    screen.blit(timer,(10,10))
    # 만약 시간이 0이하이면 게임 종료
    if total_time-elapsed_time<=0:
        print("Game Over")
        running=False

    pygame.display.update()            # 게임화면을 다시 그리기. (반드시 호출해야하는 것)  # pygame에서는 화면의 프레임을 계속 업데이트해줘야 함.

# 잠시 대기
pygame.time.delay(2000)  # 2초 정도 대기(ms)

# pygame 종료
pygame.quit()