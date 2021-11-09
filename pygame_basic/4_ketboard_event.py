import pygame

pygame.init() # 초기화 (반드시 필요) pygame을 import하면 init은 무조건 해준다.

# 화면 크기 설정
screen_width=480  # 가로크기
screen_height=640
screen=pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Yeom Game")  # 게임이름


# 배경 이미지 불러오기
background=pygame.image.load("C:\\Users\\johny\\Desktop\\pythonworkplace\\pygame_basic\\background.png")


# 캐릭터(스프라이트) 불러오기
character=pygame.image.load("C:\\Users\\johny\\Desktop\\pythonworkplace\\pygame_basic\\character.png")
character_size=character.get_rect().size    # 이미지의 크기를 구해옴.
character_width=character_size[0]  # 캐릭터의 가로 크기
character_height=character_size[1]  # 캐릭터의 세로 크기
character_x_pos=screen_width/2-(character_width/2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos=screen_height-character_height  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x=0
to_y=0


# 이벤트 루프: 프로그램이 종료되지 않도록 계속 대기하는 것.
# 중간에 사용자가 키보드를 입력하는 지, 마우스로 클릭을 하는 지 체크를 한다.
running=True   # 게임이 진행중인가?
while running:
    for event in pygame.event.get():   # pygame을 하려면 무조건 적어야 하는 코드 (깊게 몰라도 된다.) # 어떤 이벤트가 발생했는가?
        if event.type==pygame.QUIT:    # 창이 닫히는 이벤트가 발생했는가?
            running=False

        if event.type==pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key==pygame.K_LEFT:
                to_x-=1   
            if event.key==pygame.K_RIGHT:
                to_x+=1
            if event.key==pygame.K_UP:
                to_y-=1
            if event.key==pygame.K_DOWN:
                to_y+=1

        if event.type==pygame.KEYUP:    # 방향키를 떼면 멈춤
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0
            elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                to_y=0
             
    character_x_pos+=to_x
    character_y_pos+=to_y


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

    screen.blit(background, (0,0))     # 배경 그리기
    
    screen.blit(character,(character_x_pos,character_y_pos))  # 캐릭터 그리기


    pygame.display.update()            # 게임화면을 다시 그리기. (반드시 호출해야하는 것)  # pygame에서는 화면의 프레임을 계속 업데이트해줘야 함.
# pygame 종료
pygame.quit()