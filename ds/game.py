import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 800)) 
pygame.display.set_caption("DON'T STOP!!!") 
clock = pygame.time.Clock() 

background = pygame.image.load("C:/Users/student/Documents/ds/assets/universe.jpg").convert()
background = pygame.transform.scale(background, (1000, 800))

player_img = pygame.image.load("C:/Users/student/Documents/ds/assets/mario.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (100, 100))
player_rect = player_img.get_rect(midbottom=(500, 450)) 

enemy_img = pygame.image.load("C:/Users/student/Documents/ds/assets/fireball.png").convert_alpha()
enemy_img = pygame.transform.scale(enemy_img, (50, 50))
enemy_rect = enemy_img.get_rect(center=(950, 430))
enemy_speed = [-5,0] 

player_y_velocity = 0
gravity = 1
is_jumping = False
floor_level = 450

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                player_y_velocity = -20

    keys = pygame.key.get_pressed()
    speed = 10
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed

    if is_jumping or player_rect.bottom < floor_level:
        player_y_velocity += gravity
        player_rect.y += player_y_velocity
        

        if player_rect.bottom >= floor_level:
            player_rect.bottom = floor_level
            is_jumping = False
            player_y_velocity = 0

    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > 1000:
        player_rect.right = 1000
    if player_rect.top < 0:
        player_rect.top = 0

    enemy_rect.x += enemy_speed[0]
    enemy_rect.y += enemy_speed[1]
    
    if enemy_rect.right < 0:
        enemy_rect.left = 1000

    screen.blit(background, (0, 0)) 
    screen.blit(player_img, player_rect)
    screen.blit(enemy_img, enemy_rect)


    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
