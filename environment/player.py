import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load images for right and left directions
        self.images = {
            'RIGHT': [
                pygame.transform.scale(pygame.image.load("assets/pecboy_0.png").convert_alpha(), (30, 30)),
                pygame.transform.scale(pygame.image.load("assets/pecboy_1.png").convert_alpha(), (30, 30)),
                pygame.transform.scale(pygame.image.load("assets/pecboy_2.png").convert_alpha(), (30, 30))
            ],
            'LEFT': [
                pygame.transform.flip(pygame.transform.scale(pygame.image.load("assets/pecboy_0.png").convert_alpha(), (30, 30)), True, False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load("assets/pecboy_1.png").convert_alpha(), (30, 30)), True, False),
                pygame.transform.flip(pygame.transform.scale(pygame.image.load("assets/pecboy_2.png").convert_alpha(), (30, 30)), True, False)
            ],
            'UP': [
                pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/pecboy_0.png").convert_alpha(), (30, 30)), 90),
                pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/pecboy_1.png").convert_alpha(), (30, 30)), 90),
                pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/pecboy_2.png").convert_alpha(), (30, 30)), 90)
            ],
            'DOWN': [
                pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/pecboy_0.png").convert_alpha(), (30, 30)), -90),
                pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/pecboy_1.png").convert_alpha(), (30, 30)), -90),
                pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/pecboy_2.png").convert_alpha(), (30, 30)), -90)
            ]
        }
        self.image_index = 0
        self.direction = 'RIGHT'
        self.image = self.images[self.direction][self.image_index]
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)  # Initial position of the player
        self.speed = 5  # Adjust the speed as necessary
        self.current_image = 0  # For animation

    def update_position(self, walls):
        keys = pygame.key.get_pressed()
        previous_position = self.rect.topleft  # Store previous position for collision rollback
        
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.check_collision(walls):
                self.rect.topleft = previous_position  # Undo move if collision detected
            else:
                self.direction = 'LEFT'
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if self.check_collision(walls):
                self.rect.topleft = previous_position  # Undo move if collision detected
            else:
                self.direction = 'RIGHT'
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            if self.check_collision(walls):
                self.rect.topleft = previous_position  # Undo move if collision detected
            else:
                self.direction = 'UP'
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            if self.check_collision(walls):
                self.rect.topleft = previous_position  # Undo move if collision detected
            else:
                self.direction = 'DOWN'

        # Update the image for animation
        self.image_index = (self.image_index + 1) % len(self.images[self.direction])
        self.image = self.images[self.direction][self.image_index]

    def check_collision(self, walls):
        # Check for collision with each wall
        for wall in walls:
            if self.rect.colliderect(wall):
                return True
        return False

    def update(self, walls):
        self.update_position(walls)

        # Update animation
        self.current_image += 1
        if self.current_image >= len(self.images[self.direction]):
            self.current_image = 0
        self.image = self.images[self.direction][self.current_image]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
