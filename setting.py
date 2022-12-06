import math
from sounds import *

#win
w = 1410
h = 1010
fps = 60
tile = 50
w1 = w // 2
h1 = h // 2

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
darkblue = (0, 0, 45)
gray = (100, 100, 100)
darkgray = (50, 50, 50)

#graphic
shad = 0.00015
fov = math.pi / 3.5  # 2.4
pi = math.pi * 1.9

half_fov = fov / 2
num_r = 350
max_d = 800
delta_a = fov / num_r
dist = num_r / (2 * math.tan(half_fov))
proj_c = 3 * dist * tile
scale = w // num_r

#mini map
map = 5
map_tile = tile // map
map_position = (70, h - h // 1.7)

#sc
sc = pygame.display.set_mode((w, h))
sc2 = pygame.Surface((w // map, h // map))

#player
teleport_pos = (w1, h1)
player_pos = (w1, h1)
player_angle = 0
player_speed = 3.7
player_speed_2 = player_speed * 2.5


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.ver_a = 0
        self.delta = 0

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.x += player_speed_2 * cos_a
            self.y += player_speed_2 * sin_a
            mp()
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
        if keys[pygame.K_o]:
            self.angle -= 0.0455
        if keys[pygame.K_p]:
            self.angle += 0.0455
        if keys[pygame.K_r]:
            self.x = w1
            self.y = h1
        if keys[pygame.K_ESCAPE]:
            quit()