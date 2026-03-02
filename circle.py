import pygame
import sys
import random
import math
import cool

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Country Spin Wheel")
clock = pygame.time.Clock()

PALETTE = [
    (255, 99, 71),
    (60, 179, 113),
    (255, 215, 0),
    (100, 149, 237),
    (255, 105, 180),
    (210, 105, 30),
    (138, 43, 226),
    (0, 206, 209),
    (255, 165, 0),
    (112, 128, 144)
]

WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
RED = (255, 50, 50)

Ang = 0
tAng = 0
Fr = 0.99
Wgt = 0
CX = WIDTH // 2
CY = HEIGHT // 2
Rad = 200
my_countries = cool.get_countries()
countries = random.sample(my_countries, 10)

def get_new_board():
    return random.sample(my_countries, 10)

temp = len(countries)
slices = 360 / temp

pygame.font.init()
font = pygame.font.SysFont(None, 48)

running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                Wgt = random.randrange(20, 40)
            elif event.key == pygame.K_SPACE:
                countries = get_new_board()

    if Wgt > 0:
        Ang = (Ang + Wgt) % 360
        Wgt = Wgt * Fr
    
        if Wgt < 0.1:
            Wgt = 0


    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (CX, CY), Rad)
    tAng = Ang

    for i in range(temp):
        draw_angle = (Ang + (i * slices)) % 360
        current_color = PALETTE[i % len(PALETTE)]
        points = [(CX, CY)]
        for angle_step in range(int(slices) + 1):
            temp_rad = math.radians((draw_angle + angle_step) % 360)
            px = CX + Rad * math.cos(temp_rad)
            py = CY + Rad * math.sin(temp_rad)
            points.append((px, py))
            
        pygame.draw.polygon(screen, current_color, points)
        pygame.draw.polygon(screen, (0, 0, 0), points, 2)
    legend_start_y = 50
    legend_x = 20

    small_font = pygame.font.SysFont(None, 32)
    really_small_font = pygame.font.SysFont(None, 20)
    space = really_small_font.render("Spsce bar to randomize countries", True, (0, 0 ,0))
    enter = really_small_font.render("Enter key to spin the wheel", True, (0, 0, 0))
    screen.blit(space, (575, 50))
    screen.blit(enter, (575, 75))

    
    for i in range(temp):
        current_color = PALETTE[i % len(PALETTE)]
        country_name = countries[i]
        box_y = legend_start_y + (i * 45)
        pygame.draw.rect(screen, current_color, (legend_x, box_y, 20, 20))
        pygame.draw.rect(screen, (0, 0, 0), (legend_x, box_y, 20, 20), 2)
        text_surface = small_font.render(country_name, True, (0, 0, 0))
        screen.blit(text_surface, (legend_x + 30, box_y))

    if Wgt == 0:
        winning_index = int(((360 - Ang) % 360) // slices)
        winner_name = countries[winning_index]
        text_surface = font.render(f"Winner: {winner_name}", True, (0, 0, 0))
        screen.blit(text_surface, (20, 20))

    pygame.draw.line(screen, (0, 255, 0), (CX, CY), (CX + Rad + 20, CY), 3)

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
sys.exit()