from setting import *

#map
map_ = 'files/map.rcgf'
text_map = open(map_, 'r')

world_map = set()
mini_map = set()
for j, string in enumerate(text_map):
    for i, char in enumerate(string):
        if char == 'm':
            world_map.add((i * tile, j * tile))
            mini_map.add((i * map_tile, j * map_tile))

#ray_casting

def mapping(a, b):
    return (a // tile) * tile, (b // tile) * tile


def ray_casting(sc, player_pos, player_angle):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - half_fov

    for ray in range(num_r):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001
        #verticals and horizontals

        x, dx = (xm + tile, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, w, tile):
            depth_v = (x - ox) / cos_a
            y = oy + depth_v * sin_a
            if mapping(x + dx, y) in world_map:
                break
            x += dx * tile
        y, dy = (ym + tile, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, h, tile):
            depth_h = (y - oy) / sin_a
            x = ox + depth_h * cos_a
            if mapping(x, y + dy) in world_map:
                break
            y += dy * tile

        #projection
        depth = depth_v if depth_v < depth_h else depth_h
        depth *= math.cos(player_angle - cur_angle)
        proj_height = proj_c / depth
        wall = 200 / (1+(depth ** 2) * shad)
        wall_color = (wall, wall // 2, wall // 4)
        pygame.draw.rect(sc, wall_color, (ray * scale, h1 - proj_height // 2, scale, proj_height))
        cur_angle += delta_a

class Drawing:
    def __init__(self, sc, sc2):
        self.sc = sc
        self.sc2 = sc2

    def mini_map(self, player):
        self.sc2.fill(darkblue)
        map_x, map_y = player.x // map, player.y // map
        map_pos = (map_x, map_y)
        #pygame.draw.line(self.sc2, RED, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
        #                                         map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.line(self.sc2, blue, map_pos, (map_x + w * math.cos(player.angle),
                                                 map_y + w * math.sin(player.angle)), 2)

        pygame.draw.circle(self.sc2, red, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.sc2, gray, (x, y, map_tile, map_tile), 3)

        self.sc.blit(self.sc2, map_position)
