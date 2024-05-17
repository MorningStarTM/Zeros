import pygame
import math
import random

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []  # List to store all the rectangles of the environment objects

    def outline(self, screen):
        wall_color = (66, 106, 166)  # Wall color
        wall_thickness = 3
        top_wall = pygame.Rect(8, 7, self.width-8-8, wall_thickness)
        left_wall = pygame.Rect(8, 8, wall_thickness, (self.height // 2)-50)
        right_wall = pygame.Rect(self.width - wall_thickness-8, 8, wall_thickness, (self.height // 2)-50)
        pygame.draw.rect(screen, wall_color, top_wall)
        pygame.draw.rect(screen, wall_color, left_wall)
        pygame.draw.rect(screen, wall_color, right_wall)
        # Add walls to the list
        self.walls.extend([top_wall, left_wall, right_wall])

    def outline_rotated(self, screen):
        wall_color = (66, 106, 166)  # Wall color
        wall_thickness = 3
        bottom_wall = pygame.Rect(8, self.height - 10, self.width-16, wall_thickness)
        left_wall = pygame.Rect(8, (self.height // 2) + 50, wall_thickness, (self.height // 2) - 58)
        right_wall = pygame.Rect(self.width - wall_thickness - 8, self.height // 2 + 50, wall_thickness, (self.height // 2) - 58)
        pygame.draw.rect(screen, wall_color, bottom_wall)
        pygame.draw.rect(screen, wall_color, left_wall)
        pygame.draw.rect(screen, wall_color, right_wall)
        # Add walls to the list
        self.walls.extend([bottom_wall, left_wall, right_wall])

    def T_component(self, pos, angle, size, screen):
        t_color = (66, 106, 166)  # Blue color
        t_thickness = 3
        x, y = pos
        t_width = size
        t_height = size * 2
        if angle == 90:
            horizontal_bar = pygame.Rect(x, y, t_thickness, t_height)
            vertical_bar = pygame.Rect(x, y + t_height // 2, t_width, t_thickness)
        elif angle == 180:
            horizontal_bar = pygame.Rect(x, y, t_width, t_thickness)
            vertical_bar = pygame.Rect(x + t_width // 2 - (t_thickness // 2), y, t_thickness, t_height)
        elif angle == 270:
            horizontal_bar = pygame.Rect(x, y + t_height, t_thickness, t_height)
            vertical_bar = pygame.Rect(x - t_width // 2, y + t_height, t_width, t_thickness)
        elif angle == 360:
            horizontal_bar = pygame.Rect(x, y, t_width, t_thickness)
            vertical_bar = pygame.Rect(x + t_width // 2 - (t_thickness // 2), y - t_height, t_thickness, t_height)
        pygame.draw.rect(screen, t_color, horizontal_bar)
        pygame.draw.rect(screen, t_color, vertical_bar)
        # Add components to the list
        self.walls.extend([horizontal_bar, vertical_bar])

    def box(self, size, pos, screen):
        box_color = (66, 106, 166)  # Blue color
        box_thickness = 5
        x, y = pos
        width, height = size
        top_side = pygame.Rect(x, y, width, box_thickness)
        bottom_side = pygame.Rect(x, y + height - box_thickness, width, box_thickness)
        left_side = pygame.Rect(x, y, box_thickness, height)
        right_side = pygame.Rect(x + width - box_thickness, y, box_thickness, height)
        pygame.draw.rect(screen, box_color, top_side)
        pygame.draw.rect(screen, box_color, bottom_side)
        pygame.draw.rect(screen, box_color, left_side)
        pygame.draw.rect(screen, box_color, right_side)
        # Add components to the list
        self.walls.extend([top_side, bottom_side, left_side, right_side])

    def create_line(self, length, status, pos, screen):
        line_color = (66, 106, 166)  # Blue color
        line_thickness = 5
        x, y = pos
        if status == 'horizontal':
            line = pygame.Rect(x, y, length, line_thickness)
        elif status == 'vertical':
            line = pygame.Rect(x, y, line_thickness, length)
        pygame.draw.rect(screen, line_color, line)
        # Add line to the list
        self.walls.append(line)

    def L_component(self, size, pos, angle, flip, screen):
        l_color = (66, 106, 166)  # Blue color
        l_thickness = 5
        x, y = pos
        if angle == 90:
            if not flip:
                vertical_bar = pygame.Rect(x, y, l_thickness, size)
                horizontal_bar = pygame.Rect(x, y + size - l_thickness, size, l_thickness)
            else:
                horizontal_bar = pygame.Rect(x, y + size - l_thickness, size, l_thickness)
                vertical_bar = pygame.Rect(x + size - l_thickness, y, l_thickness, size)
        elif angle == 180:
            if not flip:
                horizontal_bar = pygame.Rect(x, y, size, l_thickness)
                vertical_bar = pygame.Rect(x + size - l_thickness, y, l_thickness, size)
            else:
                horizontal_bar = pygame.Rect(x, y, size, l_thickness)
                vertical_bar = pygame.Rect(x, y, l_thickness, size)
        elif angle == 270:
            if not flip:
                vertical_bar = pygame.Rect(x, y, l_thickness, size)
                horizontal_bar = pygame.Rect(x, y, size, l_thickness)
            else:
                vertical_bar = pygame.Rect(x, y, l_thickness, size)
                horizontal_bar = pygame.Rect(x, y + size - l_thickness, size, l_thickness)
        elif angle == 360:
            if not flip:
                vertical_bar = pygame.Rect(x, y, l_thickness, size)
                horizontal_bar = pygame.Rect(x, y, size, l_thickness)
            else:
                vertical_bar = pygame.Rect(x, y, l_thickness, size)
                horizontal_bar = pygame.Rect(x, y, size, l_thickness)
        pygame.draw.rect(screen, l_color, vertical_bar)
        pygame.draw.rect(screen, l_color, horizontal_bar)
        # Add components to the list
        self.walls.extend([vertical_bar, horizontal_bar])

    def enemy_home(self, screen):
        home_color = (66, 106, 166)  # Red color
        line_thickness = 2
        center_x = self.width // 2
        center_y = self.height // 2
        horizontal_line_length = 100
        vertical_line_length = 50
        top_line = pygame.Rect(650, 500, 200, line_thickness)
        left_line = pygame.Rect(center_x - horizontal_line_length, center_y - vertical_line_length, line_thickness, vertical_line_length * 2)
        right_line = pygame.Rect(center_x + horizontal_line_length, center_y - vertical_line_length, line_thickness, vertical_line_length * 2)
        left_opening = pygame.Rect(center_x - horizontal_line_length, center_y - vertical_line_length, 65, line_thickness)
        right_opening = pygame.Rect(785, 400, 65, line_thickness)
        pygame.draw.rect(screen, home_color, top_line)
        pygame.draw.rect(screen, home_color, left_line)
        pygame.draw.rect(screen, home_color, right_line)
        pygame.draw.rect(screen, home_color, left_opening)
        pygame.draw.rect(screen, home_color, right_opening)
        # Add components to the list
        self.walls.extend([top_line, left_line, right_line, left_opening, right_opening])

    def draw_environment(self, screen):
        self.walls = []  # Clear the list of walls before drawing
        self.outline(screen)
        self.outline_rotated(screen)
        self.create_line(100, "vertical", [250, 8], screen)
        self.create_line(120, "horizontal", [8, 175], screen)
        self.L_component(240, [8, 170], 90, flip=True, screen=screen)
        self.create_line(100, "vertical", [250, 900-108], screen)
        self.create_line(120, "horizontal", [8, 725], screen)
        self.L_component(240, [8, 500], 180, flip=False, screen=screen)
        self.create_line(100, "vertical", [1250, 8], screen)
        self.create_line(120, "horizontal", [1500-128, 175], screen)
        self.L_component(240, [1500-248, 170], 90, flip=False, screen=screen)
        self.create_line(100, "vertical", [1250, 900-108], screen)
        self.create_line(120, "horizontal", [1500-128, 725], screen)
        self.L_component(240, [1500-248, 500], 180, flip=True, screen=screen)
        self.enemy_home(screen)
        self.T_component([500, 900-100], angle=360, size=80, screen=screen)
        self.T_component([1000, 900-100], angle=360, size=80, screen=screen)
        self.T_component([530, -50], angle=270, size=80, screen=screen)
        self.T_component([1030, -50], angle=270, size=80, screen=screen)
        self.box(size=[150, 80], pos=[710, 670], screen=screen)
        self.box(size=[150, 80], pos=[710, 150], screen=screen)
        self.create_line(220, "vertical", [400, 355], screen=screen)
        self.create_line(100, "horizontal", [400, 355], screen=screen)
        self.create_line(100, "horizontal", [400, 575], screen=screen)
        self.create_line(220, "vertical", [1150, 355], screen=screen)
        self.create_line(100, "horizontal", [1050, 355], screen=screen)
        self.create_line(100, "horizontal", [1050, 575], screen=screen)
