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




# 이벤트 루프: 프로그램이 종료되지 않도록 계속 대기하는 것.
# 중간에 사용자가 키보드를 입력하는 지, 마우스로 클릭을 하는 지 체크를 한다.
running=True   # 게임이 진행중인가?
while running:
    for event in pygame.event.get():   # pygame을 하려면 무조건 적어야 하는 코드 (깊게 몰라도 된다.) # 어떤 이벤트가 발생했는가?
        if event.type==pygame.QUIT:    # 창이 닫히는 이벤트가 발생했는가?
            running=False

    screen.blit(background, (0,0))     # 배경 그리기
    # screen.fill((0,0,255))  # r,g,b 0~255  -> 파란색 배경화면 형성
    
    pygame.display.update()            # 게임화면을 다시 그리기. (반드시 호출해야하는 것)  # pygame에서는 화면의 프레임을 계속 업데이트해줘야 함.
# pygame 종료
pygame.quit()