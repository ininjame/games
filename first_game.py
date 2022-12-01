import pygame
import os

width, height = 1000, 700
window = pygame.display.set_mode((width,height))
fps = 60
vel = 5 #velocity

white = (255,255,255)
ball_w = 50
ball_h = 50

red_ball_img = pygame.image.load(os.path.join("assets","red_ball.png"))
red_ball = pygame.transform.rotate(pygame.transform.scale(red_ball_img, (ball_w,ball_h)),360) #just to practice rotate

blue_ball_img = pygame.image.load(os.path.join("assets","blue_ball.png"))
blue_ball = pygame.transform.rotate(pygame.transform.scale(blue_ball_img, (ball_w,ball_h)),180)

def draw_window(red, blue):
    window.fill(white)
    
    #use blit to draw surfaces to screen (in pygame everything are surfaces)
    window.blit(red_ball, (red.x, red.y))
    window.blit(blue_ball, (blue.x, blue.y))
    
    pygame.display.update()

def move_red(keys_pressed, red):
    if keys_pressed[pygame.K_a]: #LEFT
        red.x -= vel
    if keys_pressed[pygame.K_d]: #RIGHT
        red.x += vel
    if keys_pressed[pygame.K_w]: #UP
        red.y -= vel
    if keys_pressed[pygame.K_s]: #DOWN
        red.y += vel

def main():
    clock = pygame.time.Clock()
    run = True

    red = pygame.Rect(width*0.25-ball_w, height*0.5-ball_h, ball_w, ball_h)
    blue = pygame.Rect(width*0.75-ball_w, height*0.5-ball_h, ball_w, ball_h)

    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        draw_window(red, blue)
        
        keys_pressed = pygame.key.get_pressed()
        move_red(keys_pressed, red)
        
        
    pygame.quit()

if __name__ == "__main__":
    main()