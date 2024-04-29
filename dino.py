import pygame
from sys import exit
import random

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'score {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(900, 50))
    screen.blit(score_surf, score_rect)

pygame.init()
screen = pygame.display.set_mode((1000, 550))
pygame.display.set_caption("CHROME DINO")
clock = pygame.time.Clock()
FPS = 60
game_active = True
start_time = 0

ground = pygame.image.load("chrome dino/Track.png").convert_alpha()

cloud1 = pygame.image.load("chrome dino/Cloud.png").convert_alpha()
cloud2 = pygame.image.load("chrome dino/Cloud.png").convert_alpha()
cloud3 = pygame.image.load("chrome dino/Cloud.png").convert_alpha()
cloud4 = pygame.image.load("chrome dino/Cloud.png").convert_alpha()
cloud5 = pygame.image.load("chrome dino/Cloud.png").convert_alpha()

dino = pygame.image.load("chrome dino/DinoJump.png").convert_alpha()
bird = pygame.image.load("chrome dino/Bird2.png").convert_alpha()
gameover = pygame.image.load("chrome dino/GameOver.png").convert_alpha()

test_font = pygame.font.Font(size=50)
text = test_font.render("Press space to continue", False, (64, 64, 64))

score_surface = test_font.render("10", False, "Black")
score_rect = score_surface.get_rect(center=(10, 10))

dino_rect = dino.get_rect(midbottom=(100, 420))
gravity = 0

cloud_rect1 = cloud1.get_rect(bottomright=(900, 170))
cloud_rect2 = cloud2.get_rect(midbottom=(1000, 120))
cloud_rect3 = cloud3.get_rect(midbottom=(1100, 150))
cloud_rect4 = cloud4.get_rect(midbottom=(1200, 160))
cloud_rect5 = cloud5.get_rect(midbottom=(1200, 200))
bird_rect = bird.get_rect(bottomright=(2200, 300))

cactus1 = pygame.image.load("chrome dino/LargeCactus1.png").convert_alpha()
cactus2 = pygame.image.load("chrome dino/LargeCactus2.png").convert_alpha()
cactus3 = pygame.image.load("chrome dino/LargeCactus3.png").convert_alpha()
cactus4 = pygame.image.load("chrome dino/SmallCactus1.png").convert_alpha()
cactus5 = pygame.image.load("chrome dino/SmallCactus2.png").convert_alpha()
cactus6 = pygame.image.load("chrome dino/SmallCactus3.png").convert_alpha()

cactus1_rect1 = cactus1.get_rect(bottomright = (0, 425))
cactus1_rect2 = cactus2.get_rect(bottomright = (0, 425))
cactus1_rect3 = cactus3.get_rect(bottomright = (0, 425))
cactus1_rect4 = cactus4.get_rect(bottomright = (0, 425))
cactus1_rect5 = cactus5.get_rect(bottomright = (0, 425))



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dino_rect.collidepoint(event.pos):
                    gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and dino_rect.bottom >= 300:
                    gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                bird_rect.left = random.randint(3000,10000)
                cactus1_rect1.left = random.randint(3000,10000)
                cactus1_rect2.left = random.randint(3000,10000)
                cactus1_rect3.left = random.randint(3000,10000)
                cactus1_rect4.left = random.randint(3000,10000)
                cactus1_rect5.left = random.randint(3000,10000)



                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.fill("White")
        screen.blit(ground, (0, 400))
        screen.blit(dino, dino_rect)
        display_score()

        cloud_rect1.x -= 3
        if cloud_rect1.right <= 0:
            cloud_rect1.left = 900
        screen.blit(cloud1, cloud_rect1)

        cloud_rect2.x -= 3
        if cloud_rect2.right <= 0:
            cloud_rect2.left = 1100
        screen.blit(cloud2, cloud_rect2)

        cloud_rect3.x -= 3
        if cloud_rect3.right <= 0:
            cloud_rect3.left = 1150
        screen.blit(cloud3, cloud_rect3)

        cloud_rect4.x -= 3
        if cloud_rect4.right <= 0:
            cloud_rect4.left = 1200
        screen.blit(cloud4, cloud_rect4)

        cloud_rect5.x -= 3
        if cloud_rect5.right <= 0:
            cloud_rect5.left = 1000
        screen.blit(cloud1, cloud_rect5)
# DINO

        gravity += 1
        dino_rect.y += gravity
        if dino_rect.bottom >= 420:
            dino_rect.bottom = 420
        screen.blit(dino, dino_rect)

# BIRD
        bird_rect.x -= 8
        if bird_rect.right <= 0:
            bird_rect.left = random.randint(10000,15000)
        screen.blit(bird, bird_rect)
# CACTUS
        cactus1_rect1.x -= 10
        if cactus1_rect1.right <= 0:
            cactus1_rect1.left = random.randint(1500, 10000)
        screen.blit(cactus1,cactus1_rect1)

        cactus1_rect2.x -= 10
        if cactus1_rect2.right <= 0:
            cactus1_rect2.left = random.randint(1500, 10000)
        screen.blit(cactus2, cactus1_rect2)

        cactus1_rect3.x -= 10
        if cactus1_rect3.right <= 0:
            cactus1_rect3.left = random.randint(1500, 10000)
        screen.blit(cactus3, cactus1_rect3)

        cactus1_rect4.x -= 10
        if cactus1_rect4.right <= 0:
            cactus1_rect4.left = random.randint(1500, 10000)
        screen.blit(cactus4, cactus1_rect4)

        cactus1_rect5.x -= 10
        if cactus1_rect5.right <= 0:
            cactus1_rect5.left = random.randint(1500, 10000)
        screen.blit(cactus5, cactus1_rect5)

# COLLISIONS
        if bird_rect.colliderect(dino_rect):
            game_active = False

        if cactus1_rect1.colliderect(dino_rect):
            game_active = False

        if cactus1_rect2.colliderect(dino_rect):
            game_active = False

        if cactus1_rect3.colliderect(dino_rect):
            game_active = False

        if cactus1_rect4.colliderect(dino_rect):
            game_active = False

        if cactus1_rect5.colliderect(dino_rect):
            game_active = False

    else:
        screen.fill("Black")
        screen.blit(gameover, (305, 260))
        screen.blit(text, (300, 350))
    pygame.display.update()
    clock.tick(FPS)
