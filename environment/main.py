import pygame
from env import Environment
from player import Player
from enemy import Enemy
from pathfinding.finder import a_star
import numpy as np


# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1500
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pac-Man")


matrix = np.load("matrix.npy").tolist()

# Create an instance of the Environment class
environment = Environment(screen_width, screen_height, matrix)
player = Player()
enemy = Enemy(start_pos=(screen_width // 2, screen_height // 2), path="assets/ghost_blue.png")

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)


clock = pygame.time.Clock() 
# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            environment.create_path(enemy_pos=enemy.rect.center)
    # Fill the screen with a background color (optional)
    screen.fill((0, 0, 0))  # Black background
    environment.draw_environment(screen)
    

    walls = environment.walls
    #matrix = environment.generate_matrix()
    #np.save("matrix.npy", np.array(matrix))
    #break
    
    player.update(walls)
    enemy.update(player=player, walls=walls)

    environment.update(screen)

    enemy.draw(screen)
    player.draw(screen)

    # Update the display
    pygame.display.flip()
    clock.tick(40)  

# Quit Pygame
pygame.quit()
