'''하늘에서 떨어지는 똥 피하기 게임

[게임 조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
4. 캐릭터가 똥과 충돌하면 게임 종료
5. FPS는 30으로 고정

[게임 이미지]
1. 배경: 640*480(세로 가로) - background.png
2. 캐릭터: 70*70 - character.png
3. 똥: 70*70 - enemy.png'''

# import random
import pygame
from random import*

pygame.init()

screen_width=900
screen_height=900
screen=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Dodging Poops!")

clock=pygame.time.Clock()

background=pygame.image.load("C:\\Users\\johny\\Desktop\\pythonworkplace\\pygame_basic\\design-space-paper-textured-background.jpg")

character=pygame.image.load("C:\\Users\\johny\\Desktop\\pythonworkplace\\pygame_basic\\among_poops2.jpg")
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=screen_width/2-(character_width/2)
character_y_pos=screen_height-character_height


poop=pygame.image.load("C:\\Users\\johny\\Desktop\\pythonworkplace\\pygame_basic\\dodging_poop_poop.png")
poop_size=poop.get_rect().size
poop_width=poop_size[0]
poop_height=poop_size[1]
poop_x_pos=randrange(0,411) # random.randint(0,screen_width-poop_width)
poop_y_pos=0


to_x=0

to_po_x=0

character_speed=0.7
poop_speed=15


running=True
while running:
    dt=clock.tick(30)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                to_x-=character_speed
            if event.key==pygame.K_RIGHT:
                to_x+=character_speed
            

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0

    
    character_x_pos+=to_x*dt
    
    poop_y_pos+=poop_speed
    
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width


    if poop_x_pos<0:
        poop_x_pos=0
    elif poop_x_pos>screen_width-poop_width:
        poop_x_pos=screen_width-poop_width
    
    if poop_y_pos>screen_height:
        poop_y_pos=0
        poop_x_pos=randrange(0,411)
    

    
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos

    poop_rect=poop.get_rect()
    poop_rect.left=poop_x_pos
    poop_rect.top=poop_y_pos
    
    

    if character_rect.colliderect(poop_rect):
        print("충돌했습니다!")
        running=False


    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(poop,(poop_x_pos,poop_y_pos))

    

    pygame.display.update()
    
pygame.quit()

        