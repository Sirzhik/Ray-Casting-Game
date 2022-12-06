from ray_casting import *

pygame.init()

pygame.display.set_caption('Ray Casting Game')
img = pygame.image.load('files/img.png')
pygame.display.set_icon(img)

draw = Drawing(sc, sc2)
clock = pygame.time.Clock()
player = Player()

def start():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            #if event.type == pygame.MOUSEMOTION:
            #    print(event.rel)
        pygame.display.update()
        player.movement()
        sc.fill(black)

        pygame.draw.rect(sc, darkgray, (0, 0, w, h1))
        pygame.draw.rect(sc, darkgray, (0, h1, w, h1))

        ray_casting(sc, player.pos, player.angle)

        draw.mini_map(player)

        pygame.display.flip()
        clock.tick(fps)

if __name__ == '__main__':
    start()
