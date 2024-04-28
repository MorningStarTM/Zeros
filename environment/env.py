import pygame
import math
import random


class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def outline(self, screen):
        # Define the colors for the walls
        wall_color = (66, 106, 166)  # White color for walls

        # Define the thickness of the walls
        wall_thickness = 3

        # Define the coordinates for the walls
        # Let's assume the walls are along the edges of the screen
        # and are half the screen's width or height in thickness
        top_wall = pygame.Rect(8, 7, self.width-8-8, wall_thickness)
        #bottom_wall = pygame.Rect(0, self.height - wall_thickness-8, self.width, wall_thickness)
        left_wall = pygame.Rect(8, 8, wall_thickness, (self.height // 2)-50)
        right_wall = pygame.Rect(self.width - wall_thickness-8, 8, wall_thickness, (self.height // 2)-50)

        # Draw the walls on the screen
        pygame.draw.rect(screen, wall_color, top_wall)
        #pygame.draw.rect(screen, wall_color, bottom_wall)
        pygame.draw.rect(screen, wall_color, left_wall)
        pygame.draw.rect(screen, wall_color, right_wall)


    def outline_rotated(self, screen):
        # Define the colors for the walls
        wall_color = (66, 106, 166)  # Wall color

        # Define the thickness of the walls
        wall_thickness = 3

        # Define the coordinates for the rotated walls
        #top_wall = pygame.Rect(8, self.height // 2 + 50, self.width - 8 - 8, wall_thickness)
        bottom_wall = pygame.Rect(8, self.height - 10, self.width-16, wall_thickness)
        left_wall = pygame.Rect(8, (self.height // 2) + 50, wall_thickness, (self.height // 2) - 58)
        right_wall = pygame.Rect(self.width - wall_thickness - 8, self.height // 2 + 50, wall_thickness, (self.height // 2) - 58)

        # Draw the rotated walls on the screen
        #pygame.draw.rect(screen, wall_color, top_wall)
        pygame.draw.rect(screen, wall_color, bottom_wall)
        pygame.draw.rect(screen, wall_color, left_wall)
        pygame.draw.rect(screen, wall_color, right_wall)

    def T_component(self, pos, angle, size, screen):
        # Define the color for the T component
        t_color = (66, 106, 166)  # Blue color

        # Define the thickness of the T component
        t_thickness = 3

        # Define the coordinates for the T component
        x, y = pos

        # Adjust the size of the T component
        t_width = size
        t_height = size * 2

        # Draw the T component based on the angle
        if angle == 90:
            horizontal_bar = pygame.Rect(x, y, t_thickness, t_height)
            vertical_bar = pygame.Rect(x, y + t_height//2, t_width, t_thickness)
        elif angle == 180:
            horizontal_bar = pygame.Rect(x, y, t_width, t_thickness)
            vertical_bar = pygame.Rect(x + t_width//2 - (t_thickness // 2), y, t_thickness, t_height)
        elif angle == 270:
            horizontal_bar = pygame.Rect(x, y + t_height, t_thickness, t_height)
            vertical_bar = pygame.Rect(x - t_width//2, y + t_height, t_width, t_thickness)
        elif angle == 360:
            # Draw the T component at 360 degrees (same as 90 degrees)
            horizontal_bar = pygame.Rect(x, y, t_width, t_thickness)
            vertical_bar = pygame.Rect(x + t_width//2 - (t_thickness // 2), y - t_height, t_thickness, t_height)

        # Draw the T component on the screen
        pygame.draw.rect(screen, t_color, horizontal_bar)
        pygame.draw.rect(screen, t_color, vertical_bar)


    def box(self, size:list, pos:list, screen):
        box_color = (66, 106, 166)  # Blue color

        # Define the thickness of the box outline
        box_thickness = 5

        # Define the coordinates for the box
        x, y = pos
        width, height = size

        # Define the rectangles for the four sides of the box
        top_side = pygame.Rect(x, y, width, box_thickness)
        bottom_side = pygame.Rect(x, y + height - box_thickness, width, box_thickness)
        left_side = pygame.Rect(x, y, box_thickness, height)
        right_side = pygame.Rect(x + width - box_thickness, y, box_thickness, height)

        # Draw the box outline on the screen
        pygame.draw.rect(screen, box_color, top_side)
        pygame.draw.rect(screen, box_color, bottom_side)
        pygame.draw.rect(screen, box_color, left_side)
        pygame.draw.rect(screen, box_color, right_side)

    
    def create_line(self, length, status:str, pos:list, screen):
        line_color = (66, 106, 166)  # Blue color

        # Define the thickness of the line
        line_thickness = 5

        # Define the coordinates for the line
        x, y = pos

        if status == 'horizontal':
            # Draw a horizontal line
            pygame.draw.line(screen, line_color, (x, y), (x + length, y), line_thickness)
        elif status == 'vertical':
            # Draw a vertical line
            pygame.draw.line(screen, line_color, (x, y), (x, y + length), line_thickness)

    
    def L_component(self, size:int, pos:list, angle:int, flip:bool, screen):
        l_color = (66, 106, 166)  # Blue color

        # Define the thickness of the L component
        l_thickness = 5

        # Define the coordinates for the L component
        x, y = pos
        
        if angle == 90:
            if not flip:
                # Draw the L component at 90 degrees (normal)
                pygame.draw.rect(screen, l_color, pygame.Rect(x, y, l_thickness, size), 0)  # Vertical bar
                pygame.draw.rect(screen, l_color, pygame.Rect(x, y + size - l_thickness, size, l_thickness), 0)  # Horizontal bar
            else:
                # Draw the L component at 90 degrees (flipped)
                pygame.draw.rect(screen, l_color, pygame.Rect(x, y + size - l_thickness, size, l_thickness), 0)  # Horizontal bar
                pygame.draw.rect(screen, l_color, pygame.Rect(x + size - l_thickness, y, l_thickness, size), 0)  # Vertical bar
        elif angle == 180:
            if not flip:
                # Draw the L component at 180 degrees (normal)
                pygame.draw.rect(screen, l_color, pygame.Rect(x, y, size, l_thickness), 0)  # Horizontal bar
                pygame.draw.rect(screen, l_color, pygame.Rect(x + size - l_thickness, y, l_thickness, size), 0)  # Vertical bar
            else:
                # Draw the L component at 180 degrees (flipped)
                pygame.draw.rect(screen, l_color, pygame.Rect(x, y, size, l_thickness), 0)  # Horizontal bar
                pygame.draw.rect(screen, l_color, pygame.Rect(x, y, l_thickness, size), 0)  # Vertical bar
        elif angle == 270:
            if not flip:
                # Draw the L component at 270 degrees (normal)
                pygame.draw.rect(screen, l_color, pygame.Rect(x, y, l_thickness, size), 0)  # Vertical bar
                pygame.draw.rect(screen, l_color, pygame.Rect(x, y, size, l_thickness), 0)
            else:
                # Draw the L component at 270 degrees (flipped)
                pygame.draw.rect(screen, l_color, pygame.Rect(x, y, l_thickness, size), 0)  # Vertical bar
                pygame.draw.rect(screen, l_color, pygame.Rect(x, y + size - l_thickness, size, l_thickness), 0)  # Horizontal bar
        elif angle == 360:
            if not flip:
                # Draw the L component at 360 degrees (normal)
                pygame.draw.rect(screen, l_color, pygame.Rect(x, y, l_thickness, size), 0)  # Vertical bar
                pygame.draw.rect(screen, l_color, pygame.Rect(x, y, size, l_thickness), 0)  # Horizontal bar
            else:
                # Draw the L component at 360 degrees (flipped, same as 90 degrees)
                pygame.draw.rect(screen, l_color, pygame.Rect(x, y, l_thickness, size), 0)  # Vertical bar
                pygame.draw.rect(screen, l_color, pygame.Rect(x, y, size, l_thickness), 0)  # Horizontal bar


    def enemy_home(self, screen):
        # Define the color for the enemy home
        home_color = (66, 106, 166)  # Red color

        # Define the thickness of the lines
        line_thickness = 2

        # Get the center coordinates of the screen
        center_x = self.width // 2
        center_y = self.height // 2

        # Define the length of the lines
        horizontal_line_length = 100
        vertical_line_length = 50

        # Draw the lines to form the enemy home
        # Top line
        #pygame.draw.line(screen, home_color, (center_x - horizontal_line_length, center_y - vertical_line_length+100), (center_x + horizontal_line_length, center_y - vertical_line_length+100), line_thickness)
        pygame.draw.line(screen, home_color, (650, 500), (850, 500), line_thickness)

        # Left line
        pygame.draw.line(screen, home_color, (center_x - horizontal_line_length, center_y - vertical_line_length), (center_x - horizontal_line_length, center_y + vertical_line_length), line_thickness)

        # Right line
        pygame.draw.line(screen, home_color, (center_x + horizontal_line_length, center_y - vertical_line_length), (center_x + horizontal_line_length, center_y + vertical_line_length), line_thickness)

        pygame.draw.line(screen,home_color, (center_x - horizontal_line_length, center_y - vertical_line_length), (715, center_y - vertical_line_length), line_thickness)
        pygame.draw.line(screen,home_color, (795, 400), (850, 400), line_thickness)

    

    def draw_environment(self, screen):
        self.outline(screen)
        self.outline_rotated(screen)

        #left side
        #up
        self.create_line(100, "vertical", [250, 8], screen)
        self.create_line(120, "horizontal", [8, 175], screen)
        self.L_component(240, [8, 170], 90, flip=True, screen=screen)
        
        # down
        self.create_line(100, "vertical", [250, 900-108], screen)
        self.create_line(120, "horizontal", [8, 725], screen)
        self.L_component(240, [8, 500], 180, flip=False, screen=screen)

        ################################################################################################################################

        #right side
        #up
        self.create_line(100, "vertical", [1250, 8], screen)
        self.create_line(120, "horizontal", [1500-128, 175], screen)
        self.L_component(240, [1500-248, 170], 90, flip=False, screen=screen)

        #down
        self.create_line(100, "vertical", [1250, 900-108], screen)
        self.create_line(120, "horizontal", [1500-128, 725], screen)
        self.L_component(240, [1500-248, 500], 180, flip=True, screen=screen)

        self.enemy_home(screen)

        self.T_component([500, 900-100], angle=360, size=80, screen=screen)
        self.T_component([1000, 900-100], angle=360, size=80, screen=screen)

        self.T_component([530, -50], angle=270, size=80, screen=screen)
        self.T_component([1030, -50], angle=270, size=80, screen=screen)

        self.box(size=[150,80], pos=[710, 670], screen=screen)
        self.box(size=[150,80], pos=[710, 150], screen=screen)


        self.create_line(220, "vertical", [400, 355], screen=screen)
        self.create_line(100, "horizontal", [400, 355], screen=screen)
        self.create_line(100, "horizontal", [400, 575], screen=screen)

        self.create_line(220, "vertical", [1150, 355], screen=screen)
        self.create_line(100, "horizontal", [1050, 355], screen=screen)
        self.create_line(100, "horizontal", [1050, 575], screen=screen)