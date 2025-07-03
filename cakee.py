import pygame
import random
import sys


pygame.init()


WIDTH, HEIGHT = 480, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Velvet Oven")


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

WHITE = (255, 255, 255)
BROWN = (139, 69, 19)


girl_img = pygame.image.load("C:/Users/me/Downloads/cake/girl.png") 
cake_img = pygame.image.load("C:/Users/me/Downloads/cake/cake.png")  
background = pygame.image.load("C:/Users/me/Downloads/cakebackg.jpeg")  


girl_img = pygame.transform.scale(girl_img, (70, 120))
cake_img = pygame.transform.scale(cake_img, (40, 40))


girl_x = WIDTH // 2
girl_y = HEIGHT - 140
girl_speed = 7


cake_list = []
cake_fall_speed = 5
total_cakes = 25
caught_cakes = 0


def start_screen():
    screen.fill(WHITE)
    title_text = font.render("Velvet Oven", True, BROWN)
    start_text = font.render("Press SPACE to Start", True, BROWN)
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, HEIGHT//2 - 60))
    screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, HEIGHT//2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False


def end_screen(caught):
    screen.fill(WHITE)
    if caught == total_cakes:
        msg = "🎉 You got all 25 cakes! Congrats!"
    else:
        msg = f"Oops! You caught {caught}/{total_cakes} cakes."
    result_text = font.render(msg, True, BROWN)
    screen.blit(result_text, (WIDTH//2 - result_text.get_width()//2, HEIGHT//2))
    pygame.display.flip()
    pygame.time.wait(4000)

def game_loop():
    global girl_x, caught_cakes
    girl_x = WIDTH // 2
    caught_cakes = 0
    cake_list.clear()
    dropped_cakes = 0

    while True:
        screen.blit(background, (0, 0))  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and girl_x > 0:
            girl_x -= girl_speed
        if keys[pygame.K_RIGHT] and girl_x < WIDTH - 70:
            girl_x += girl_speed

    
        if dropped_cakes < total_cakes:
            if random.randint(1, 20) == 1:
                cake_x = random.randint(0, WIDTH - 40)
                cake_list.append([cake_x, -40])
                dropped_cakes += 1

    
        for cake in cake_list:
            cake[1] += cake_fall_speed

    
        for cake in cake_list[:]:
            if (girl_x < cake[0] < girl_x + 70) and (girl_y < cake[1] < girl_y + 120):
                cake_list.remove(cake)
                caught_cakes += 1

                
                if caught_cakes >= total_cakes:
                    pygame.time.wait(1000)
                    end_screen(caught_cakes)
                    return

        
        screen.blit(girl_img, (girl_x, girl_y))

        
        for cake in cake_list:
            screen.blit(cake_img, (cake[0], cake[1]))

    
        score_text = font.render(f"{caught_cakes}/{total_cakes}", True, BROWN)
        screen.blit(score_text, (10, 10))

        
        if dropped_cakes == total_cakes and all(c[1] > HEIGHT for c in cake_list):
            pygame.time.wait(1000)
            end_screen(caught_cakes)
            return

        pygame.display.flip()
        clock.tick(60)


start_screen()
game_loop()
