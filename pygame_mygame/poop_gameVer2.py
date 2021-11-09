 import pygame
import random

pygame.init()

screen_width=640
screen_height=480
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
poop_x_pos=random.randint(0,screen_width-poop_width) # random.randint(0,screen_width-poop_width)
poop_y_pos=0


poop2=pygame.image.load("C:\\Users\\johny\\Desktop\\pythonworkplace\\pygame_basic\\dodging_poop_poop.png")
poop2_size=poop2.get_rect().size
poop2_width=poop2_size[0]
poop2_height=poop2_size[1]
poop2_x_pos=random.randint(0,screen_width-poop2_width) # random.randint(0,screen_width-poop_width)
poop2_y_pos=0



to_x=0
to_y=0
to_po_x=0
t0_po2_x=0

character_speed=0.7
poop_speed=20
poop2_speed=10


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
            if event.key==pygame.K_UP:
                to_y-=character_speed
            if event.key==pygame.K_DOWN:
                to_y+=character_speed    
            

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                to_y=0

    
    character_x_pos+=to_x*dt
    #character_y_pos+=to_y*dt

    poop_y_pos+=poop_speed
    poop2_y_pos+=poop2_speed
    
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width

    '''if character_y_pos<0:
        character_y_pos=0
    elif character_y_pos>screen_height-character_height:
        character_y_pos=screen_height-character_height'''


    if poop_x_pos<0:
        poop_x_pos=0
    elif poop_x_pos>screen_width-poop_width:
        poop_x_pos=screen_width-poop_width
    
    if poop_y_pos>screen_height:
        poop_y_pos=0
        poop_x_pos=random.randint(0,screen_width-poop_width)

    if poop2_x_pos<0:
            poop2_x_pos=0
    elif poop2_x_pos>screen_width-poop2_width:
        poop2_x_pos=screen_width-poop2_width
    
    if poop2_y_pos>screen_height:
        poop2_y_pos=0
        poop2_x_pos=random.randint(0,screen_width-poop2_width)
    

    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos

    poop_rect=poop.get_rect()
    poop_rect.left=poop_x_pos
    poop_rect.top=poop_y_pos
    
    poop2_rect=poop2.get_rect()
    poop2_rect.left=poop2_x_pos
    poop2_rect.top=poop2_y_pos
    

    if character_rect.colliderect(poop_rect):
        print("충돌했습니다!")
        running=False

    if character_rect.colliderect(poop2_rect):
        print("충돌했습니다!")
        running=False
    

    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(poop,(poop_x_pos,poop_y_pos))
    screen.blit(poop2,(poop2_x_pos,poop2_y_pos))

    pygame.display.update()
    
pygame.quit()

        