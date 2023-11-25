import pygame
import time
import random

pygame.init()

snake_green = (9, 121, 105)
background_color = (175, 225, 175)
red = (199, 0, 57)
orange = (228, 208, 10)

width, height = 600, 400

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont("ubuntu", 30)
score_font = pygame.font.SysFont("ubuntu", 25)

def draw_score(score):
    text = score_font.render(f"Score: {str(score)}", True, red)
    game_display.blit(text, [0,0])
    
def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, snake_green, [pixel[0], pixel[1], snake_size, snake_size])
        
def run_game():
    
    game_over = False
    game_close = False
    
    x = width/2
    y = height/2
    
    x_speed = 0
    y_speed = 0
    
    snake_pixels = []
    snake_length = 1
    
    target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
    
    while not game_over:
        
        while game_close:
            game_display.fill(background_color)
            game_over_messege = message_font.render("Game Over!", True, red)
            game_display.blit(game_over_messege, [width/3, height/3])
            draw_score(snake_length - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_speed != snake_size:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT and x_speed != -snake_size:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP and y_speed != snake_size:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN and y_speed != -snake_size:
                    x_speed = 0
                    y_speed = snake_size
                    
        if x >= width or  x < 0 or y >= height or y < 0:
            game_close = True
            
        x += x_speed
        y += y_speed
        
        game_display.fill(background_color)
        pygame.draw.rect(game_display, orange, [target_x, target_y, snake_size, snake_size])
        
        snake_pixels.append([x,y])
        
        if len(snake_pixels) > snake_length:
            del snake_pixels[0]
        
        for pixel in snake_pixels[:-1]:
            if pixel == [x,y]:
                game_close = True
         
        draw_snake(snake_size, snake_pixels)
        draw_score(snake_length - 1)
        
        pygame.display.update()
        
        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1
        
        clock.tick(snake_speed)
        
    pygame.quit()
    quit()

run_game()