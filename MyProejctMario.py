import pygame 

clocl = pygame.time.Clock()

pygame.init() #начало
screen = pygame.display.set_mode((1280, 720))         
pygame.display.set_caption("Mario+")   
fon = pygame.image.load('images copy/icoon.webp') 
player = pygame.image.load('images copy/player.left/1646038128_1-www-funnyart-club-p-spraiti-personazhei-piksel-art-art-1-fotor-2024071715349.png').convert_alpha() 
                                                                                                                                                                                                     
mpnstr = pygame.image.load('images copy/555.png').convert_alpha() 
mpnstr = pygame.transform.scale(mpnstr, (160, 160))
walk_left = [
    pygame.image.load('images copy/player.left/1646038128_1-www-funnyart-club-p-spraiti-personazhei-piksel-art-art-1-fotor-2024071715349.png').convert_alpha(),
    pygame.image.load('images copy/player.left/1646038128_1-www-funnyart-club-p-spraiti-personazhei-piksel-art-art-1-fotor-20240717153340.png').convert_alpha(),
    pygame.image.load('images copy/player.left/1646038128_1-www-funnyart-club-p-spraiti-personazhei-piksel-art-art-1-fotor-20240717153436.png').convert_alpha(),
    pygame.image.load('images copy/player.left/1646038128_1-www-funnyart-club-p-spraiti-personazhei-piksel-art-art-1-fotor-20240717153514.png').convert_alpha(),
] 

walk_richt = [
    pygame.image.load('images copy/player.ricght/1646038128_1-www-funnyart-club-p-spraiti-personazhei-piksel-art-art-1-fotor-2024071715191.png').convert_alpha(),
    pygame.image.load('images copy/player.ricght/1646038128_1-www-funnyart-club-p-spraiti-personazhei-piksel-art-art-1-fotor-20240717151758.png').convert_alpha(),
    pygame.image.load('images copy/player.ricght/1646038128_1-www-funnyart-club-p-spraiti-personazhei-piksel-art-art-1-fotor-20240717151838.png').convert_alpha(),
    pygame.image.load('images copy/player.ricght/1646038128_1-www-funnyart-club-p-spraiti-personazhei-piksel-art-art-1-fotor-20240717152737.png').convert_alpha(),
] 

player = 1

fon_x = 0
player_anim = 0
player_speed = 23
player_x = 150
player_y = 360

is_jump = False 
is_count = 12

sagi = pygame.mixer.Sound('music/-shagi-begom-po-lesu (1).mp3') 
sagi.play(-1)

monstrlistgame = []

monster_time = pygame.USEREVENT + 1 
pygame.time.set_timer(monster_time, 5000)

label = pygame.font.Font('images copy/text/ofont.ru_Impact.ttf', 60)

loselabel = label.render('Вы проиграли. Попробуйте снова!', False ,(193, 196,196))
restart = label.render('Играть заново!', False ,(222,194,166))
recrestart = restart.get_rect(topleft= (400, 450))
gemplay = True


running = True
while running:
    clocl.tick(16)
    screen.blit(fon, (fon_x, 0)) 
    screen.blit(fon, (fon_x + 1280, 0)) 


    if gemplay:
        player_rec = walk_left[0].get_rect(topleft=(player_x, player_y))

        if monstrlistgame:
            for (i, el) in enumerate(monstrlistgame):
                screen.blit(mpnstr, el)
                el.x -= 50


                if el.x < -10:
                    monstrlistgame.pop(i)
                if player_rec.colliderect(el):
                    gemplay = False

        keus = pygame.key.get_pressed()  

        if keus[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim], (player_x, player_y))  
        else:
            screen.blit(walk_richt[player_anim], (player_x, player_y))  

        keus = pygame.key.get_pressed()

        if keus[pygame.K_LEFT] and player_x > 150:  
            player_x -= player_speed
        elif keus[pygame.K_RIGHT] and player_x < 800:
            player_x += player_speed

        if not is_jump: 
            if keus[pygame.K_SPACE]:
                is_jump = True
        else:
            if is_count >= -12:
                if is_count >= 0:
                    player_y -= (is_count ** 2) / 2
                else:
                    player_y += (is_count ** 2) / 2
                is_count -= 1
            else:
                is_jump = False
                is_count = 12

        if player_anim == 3:
            player_anim = 0
        else:
            player_anim += 1

            fon_x -= 2
            if fon_x == -1280:
                fon_x = 0
    else:
        screen.fill((46, 41, 44))
        screen.blit(loselabel, (140, 190))
        screen.blit(restart, recrestart)
        mouse2 = pygame.mouse.get_pos()

        if recrestart.collidepoint(mouse2) and pygame.mouse.get_pressed()[0]:
            gemplay = True
            player_x = 150
            monstrlistgame.clear()


    pygame.display.update() 

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False 
            pygame.quit() 

        if event.type == monster_time:
            monstrlistgame.append(mpnstr.get_rect(topleft = (1400, 450)))


    clocl.tick(30)


