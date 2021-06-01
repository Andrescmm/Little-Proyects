import pygame
from pygame.locals import*
import random

pygame.init()
screen = pygame.display.set_mode((1366,768), pygame.FULLSCREEN)
background=pygame.Surface((1440,900))
font=pygame.font.Font(None,30)
pygame.mouse.set_visible(False)
red=(255,0,0)
white=(255,255,255)
blue=(0,0,255)
black=(0,0,0)
yellow=(255,255,0)
purple=(125,0,125)
clock = pygame.time.Clock()

snakecont =0
slithercont=0
snakecont=0
speed=4
applex=random.randint(100,1200)
appley=random.randint(100,700)
obstaculo1=pygame.Rect(630,75,100,100)
obstaculo2=pygame.Rect(630,675,100,100)
obstaculo3=pygame.Rect(285,350,100,100)
obstaculo4=pygame.Rect(1005,350,100,100)





snake_positions=[(0,0),(0,-40)]
slither_positions=[(1440,900),(1000,500)]
snakeh = pygame.Rect(200, 200, 30, 30)
slitherh=pygame.Rect(1200,600,30,30)
snakeb=pygame.Rect(snake_positions[1][0], snake_positions[1][1], 30, 30)
slitherb=pygame.Rect(slither_positions[1][0], slither_positions[1][1], 30, 30)
apple = pygame.Rect(applex, appley, 30,30)
lenght=2
lenghtr=2
slitherscore=0
snakescore=0
redwon=False
bluewon=False
bluewonp=False
redwonp=False
redwons=False
bluewons=False
bothlost=False
direction="right"
directionr="left"

level1=False
level2=False
level3=False


menu_screen=True
game=True
g_overscreen=False


while game:


    '''------------------------------------MAIN MENU------------------'''
    if menu_screen==True:
                    
                    font_ms_t=pygame.font.Font(None,150)
                    font_ms_s=pygame.font.Font(None,60)
                    menu_t=font_ms_t.render("Snake!", 1, black, white)
                    menu_level1=font_ms_s.render("level 1!     (las paredes te matan)", 1, white)
                    menu_level2=font_ms_s.render("level 2!     (atraviesas paredes)",1 ,white)
                    menu_level3=font_ms_s.render("level 3!     (hay obstaculos) ", 1, white)
                   
                    menu_quit=font_ms_s.render("salir :(", 1 , white)


                    box_menu_level1_xz, box_menu_level1_yz = font_ms_s.size("level 1!")
                    box_menu_level2_xz, box_menu_level2_yz = font_ms_s.size("level 2!")
                    box_menu_level3_xz, box_menu_level3_yz = font_ms_s.size("level 2!")
                    
                    box_menu_quit_xz, box_menu_quit_yz = font_ms_s.size("salir :(")
                    
                    
                    


                    while menu_screen==True:

                        mousex, mousey=pygame.mouse.get_pos()
                        box_menu_level1= pygame.Rect(200,300,box_menu_level1_xz, box_menu_level1_yz)
                        box_menu_level2= pygame.Rect(200,500,box_menu_level2_xz,box_menu_level2_yz)
                        box_menu_level3= pygame.Rect(200,700,box_menu_level3_xz,box_menu_level3_yz)
                        
                        box_menu_quit= pygame.Rect(1100,600,box_menu_quit_xz, box_menu_quit_yz)

                            
                        
                        mousehb= pygame.Rect(mousex-15, mousey-15, 30, 30)
                        

                        for event in pygame.event.get(): 
                            mousebuttons=pygame.mouse.get_pressed()                           
                            if mousebuttons[0]==True and box_menu_level1.colliderect(mousehb)==True:
                                level1=True
                                level2=False
                                level3=False
                                game=True
                                menu_screen=False
                            if mousebuttons[0]==True and box_menu_level2.colliderect(mousehb)==True:
                                level2=True
                                level1=False
                                level3=False
                                game=True
                                menu_screen=False
                            if mousebuttons[0]==True and box_menu_level3.colliderect(mousehb)==True:
                                level3=True
                                level2=False
                                level1=False
                                game=True
                                menu_screen=False
                                                        
                            if mousebuttons[0]==True and box_menu_quit.colliderect(mousehb)==True:
                                pygame.quit()
                                
                        
                        background.fill(black)
                        screen.blit(background, (0,0))
                        screen.blit(menu_level1, (200, 300))
                        screen.blit(menu_level2, (200, 500))
                        screen.blit(menu_level3, (200, 700)) 
                        screen.blit(menu_t, (500,100)) 
                        
                        screen.blit(menu_quit, (1100, 600))  
                        
                        pygame.draw.polygon(screen, yellow, [(mousex-15, mousey+15),(mousex+15,mousey+15),(mousex, mousey-10)])
                        clock.tick(120)
                        
                        pygame.display.flip()






                        '''---------------------------GAME------------------------'''




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        
    
    keys_pressed = pygame.key.get_pressed()

    
    
    if direction=="left":
        snakeh.x-=speed
        if keys_pressed[pygame.K_UP]:
            direction="up"
        elif keys_pressed[pygame.K_DOWN]:
            direction="down"
    elif direction=="right":
        if keys_pressed[pygame.K_UP]:
            direction="up"
        elif keys_pressed[pygame.K_DOWN]:
            direction="down"
        
        snakeh.x+=speed
    elif direction=="up":
        if keys_pressed[pygame.K_LEFT]:
            direction="left"
        elif keys_pressed[pygame.K_RIGHT]:
            direction="right"
        snakeh.y-=speed
    elif direction=="down":
        if keys_pressed[pygame.K_LEFT]:
            direction="left"
        elif keys_pressed[pygame.K_RIGHT]:
            direction="right"
        snakeh.y+=speed



    
    
    
    if directionr=="left":
        if keys_pressed[pygame.K_w]:
            directionr="up"
        elif keys_pressed[pygame.K_s]:
            directionr="down"
        slitherh.x-=speed
    elif directionr=="right":
        if keys_pressed[pygame.K_w]:
            directionr="up"
        elif keys_pressed[pygame.K_s]:
            directionr="down"
        slitherh.x+=speed
    elif directionr=="up":
        if keys_pressed[pygame.K_a]:
            directionr="left"
        elif keys_pressed[pygame.K_d]:
            directionr="right"
        slitherh.y-=speed
    elif directionr=="down":
        if keys_pressed[pygame.K_a]:
            directionr="left"
        elif keys_pressed[pygame.K_d]:
            directionr="right"
        slitherh.y+=speed

    if snakeh.colliderect(apple):
        for i in range(5):
            snake_positions.append((apple.x,apple.y))   
        apple.x=random.randint(100,1200)
        apple.y=random.randint(100,700)
        lenght+=5
        snakescore+=10
    

    if slitherh.colliderect(apple):
        for i in range(5):
            slither_positions.append((apple.x,apple.y))   
        apple.x=random.randint(100,1200)
        apple.y=random.randint(100,700)
        lenghtr+=5
        slitherscore+=10
    if level1==True:
        if snakeh.x >1366:
            game=False
            bluewons=True
        if snakeh.x< 0:
            game=False
            bluewons=True
        if snakeh.y > 768:
            game=False
            bluewons=True
        if snakeh.y < 0:
            game=False
            bluewons=True
            

        if slitherh.x > 1366:
            game=False
            redwons=True
        if slitherh.x < 0:
            game=False
            redwons=True
        if slitherh.y > 768:
            game=False
            redwons=True
        if slitherh.y < 0:
            game=False
            redwons=True
    elif level2 == True or level3 == True:
        if snakeh.x >1366:
            snakeh.x-=1366
        if snakeh.x<0:
            snakeh.x+=1366
        if snakeh.y>768:
            snakeh.y-=768
        if snakeh.y<0:
            snakeh.y+=768

        if slitherh.x >1366:
            slitherh.x-=1366
        if slitherh.x<0:
            slitherh.x+=1366
        if slitherh.y>768:
            slitherh.y-=768
        if slitherh.y<0:
            slitherh.y+=768
    
    
    if level3==True:
        if snakeh.colliderect(obstaculo1) or snakeh.colliderect(obstaculo2) or snakeh.colliderect(obstaculo3) or snakeh.colliderect(obstaculo4):
            bluewons=True
            game=False
        if slitherh.colliderect(obstaculo1) or slitherh.colliderect(obstaculo2) or slitherh.colliderect(obstaculo3) or slitherh.colliderect(obstaculo4):
            redwons=True
            game=False


    
    snake_positions.append((snakeh.x,snakeh.y)) 
    snake_positions.pop(0)  

    slither_positions.append((slitherh.x,slitherh.y))
    slither_positions.pop(0) 


    snakescoret=font.render("red score:"+ str(snakescore), 1, white)
    slitherscoret=font.render("blue score:"+ str(slitherscore), 1,white) 
    background.fill(black)
    screen.blit(background, (0,0))
    pygame.draw.rect(screen,red,snakeh)
    for i in range (1,lenght):         
        snakeb=pygame.Rect(snake_positions[i][0], snake_positions[i][1], 30, 30)        
        if snakeh.contains(snakeb):
            snakecont+=1    
        pygame.draw.rect(screen,red,snakeb)
        
        if slitherh.colliderect(snakeb):
            slithercont+=1
    

    pygame.draw.rect(screen, blue, slitherh)
    
    for i in range (1,lenghtr):         
        slitherb=pygame.Rect(slither_positions[i][0], slither_positions[i][1], 30, 30)        
        if slitherh.contains(slitherb):
            slithercont+=1
        if snakeh.colliderect(slitherb):
            snakecont+=1
        pygame.draw.rect(screen,blue,slitherb)
    if snakecont>1:
        game=False
    
        bluewon=True 
        g_overscreen=True
    if slitherscore==500:
        game=False
        bluewonp=True     
        g_overscreen=True
    if slithercont>1:
        game=False
    
        redwon = True  
        g_overscreen=True   
    if snakescore==500:
        game=False
        redwonp=True
        g_overscreen=True
    if bluewon==True and redwon==True:
        
        bothlost=True
        
        
    slithercont=0   
    snakecont=0    
    pygame.draw.rect(screen, white, apple)
    screen.blit(snakescoret,(10,10))
    screen.blit(slitherscoret, (1200, 10))

    if level3==True:
            pygame.draw.rect(screen,purple,obstaculo1)
            pygame.draw.rect(screen,purple,obstaculo2)
            pygame.draw.rect(screen,purple,obstaculo3)
            pygame.draw.rect(screen,purple,obstaculo4)   
    clock.tick(120)
    pygame.display.flip()







    


    '''--------------------------------------GAME OVER SCREEN--------------------------------'''



    if game==False:
        g_overscreen=True
    if g_overscreen==True:
                font_egs_t=pygame.font.Font(None,100)
                font_egs_s=pygame.font.Font(None,60)
                egs_std=font_egs_s.render("clickeaame para reiniciar!", 1, white)
                egs_std_q=font_egs_s.render("o a mi para salir", 1, white)
                box_egs_xz, box_egs_yz = font_egs_s.size("clickeeame para reiniciar!")
                box_egs_q_xz, box_egs_q_yz= font_egs_s.size("o a mi para salir")
                egs_std_m=font_egs_s.render("o a mi para volver al menu principal", 1, white)
                box_egs_m_xz, box_egs_m_yz= font_egs_s.size("o a mi para volver al menu principal")
                


                while g_overscreen==True:
                    mousex, mousey=pygame.mouse.get_pos()
                    
                    if bothlost==True:
                        egs_t=font_egs_t.render("los dos perdieron!", 1, white)
                        egs_s=font_egs_s.render("chocando sus cabezas", 1, white)
                    elif bluewon==True:
                        egs_t=font_egs_t.render("Blue ganó!", 1, blue)
                        egs_s=font_egs_s.render("haciendo que red se estrelle contra el", 1, white)
                    elif bluewonp==True:
                        egs_t=font_egs_t.render("Blue ganó!", 1, blue)
                        egs_s=font_egs_s.render("acumulando 500 puntos!", 1, white)
                    elif redwon==True:
                        egs_t=font_egs_t.render("Red ganó!", 1, red)
                        egs_s=font_egs_s.render("haciendo que blue se estrelle contra el", 1, white)
                    elif redwonp==True:
                        egs_t=font_egs_t.render("Red ganó!", 1, red)
                        egs_s=font_egs_s.render("acumulando 500 puntos!", 1, white)
                    elif redwons==True:
                        egs_t=font_egs_t.render("Red ganó!", 1, red)
                        egs_s=font_egs_s.render("blue se fue contra la pared", 1, white)
                    elif bluewons==True:
                        egs_t=font_egs_t.render("Blue ganó!", 1, blue)
                        egs_s=font_egs_s.render("red se fue contra la pared", 1, white)
                        
                    box_egs= pygame.Rect(600,500,box_egs_xz, box_egs_yz)
                    mousehb= pygame.Rect(mousex, mousey, 30, 30)
                    box_egs_q= pygame.Rect(600,600,box_egs_q_xz, box_egs_q_yz )
                    box_egs_m=pygame.Rect(600,700, box_egs_m_xz, box_egs_m_yz)

                    for event in pygame.event.get(): 
                        mousebuttons=pygame.mouse.get_pressed()
                        if mousebuttons[0]==True and box_egs.colliderect(mousehb)==True:  
                            snake_positions=[(0,0),(0,-40)]
                            slither_positions=[(1440,900),(1000,500)]
                            snakeh = pygame.Rect(200, 200, 30, 30)
                            slitherh=pygame.Rect(1200,600,30,30)
                            snakeb=pygame.Rect(snake_positions[1][0], snake_positions[1][1], 30, 30)
                            slitherb=pygame.Rect(slither_positions[1][0], slither_positions[1][1], 30, 30)
                            apple = pygame.Rect(applex, appley, 30,30)
                            lenght=2
                            lenghtr=2
                            slitherscore=0
                            snakescore=0
                            redwon=False
                            bluewon=False
                            bluewonp=False
                            redwonp=False
                            redwons=False
                            bluewons=False
                            bothlost=False
                            direction="right"
                            directionr="left"  
                            game=True
                            g_overscreen=False                      
                            
                        if mousebuttons[0]==True and box_egs_m.colliderect(mousehb)==True:
                            g_overscreen=False
                            menu_screen=True
                            game=True
                        if mousebuttons[0]==True and box_egs_q.colliderect(mousehb)==True:
                            pygame.quit()
                            
                    

                    background.fill(black)
                    screen.blit(background, (0,0))
                    screen.blit(egs_t, (500, 150))
                    screen.blit(egs_s, (550, 300))
                    screen.blit(egs_std, (600, 500)) 
                    screen.blit(egs_std_q, (600,600))  
                    screen.blit(egs_std_m,(600,700))         
                    pygame.draw.polygon(screen, yellow, [(mousex-15, mousey+15),(mousex+15,mousey+15),(mousex, mousey-10)])
                    clock.tick(120)
                    
                    pygame.display.flip()

                #--------------------reset.....................
