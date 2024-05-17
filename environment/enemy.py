import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, start_pos, path):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        self.speed = 2
        self.direction_x = 0
        self.direction_y = 0

    def update(self, player, walls):
        self.move_towards_player(player)
        self.check_collision(walls)
        self.check_player_collision(player)

    def move_towards_player(self, player):
        player_pos = player.rect.center
        enemy_pos = self.rect.center

        self.direction_x = player_pos[0] - enemy_pos[0]
        self.direction_y = player_pos[1] - enemy_pos[1]

        distance = (self.direction_x**2 + self.direction_y**2)**0.5

        if distance != 0:
            self.direction_x /= distance
            self.direction_y /= distance

        self.rect.x += int(self.direction_x * self.speed)
        self.rect.y += int(self.direction_y * self.speed)

    def check_collision(self, walls):
        for wall in walls:
            if self.rect.colliderect(wall):
                self.rect.x -= int(self.direction_x * self.speed)
                self.rect.y -= int(self.direction_y * self.speed)

    def check_player_collision(self, player):
        if self.rect.colliderect(player.rect):
            print("Player has been caught by the enemy!")
            pygame.quit()
            quit()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
