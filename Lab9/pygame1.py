import pygame, datetime

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
mickey = pygame.transform.scale(pygame.image.load(r'C:\pp2\week7\pygame\main-clock.png'), size)
seconds = pygame.transform.smoothscale(pygame.image.load(r'C:\pp2\week7\pygame\left_hand.png'), size)
minutes = pygame.transform.smoothscale(pygame.image.load(r'C:\pp2\week7\pygame\right_hand.png'), size)

clock = pygame.time.Clock()


def r_center(s, image, angle, x, y):
    r_image = pygame.transform.rotate(image, angle)
    n_rect = r_image.get_rect(center=image.get_rect(center=(x, y)).center)
    s.blit(r_image, n_rect)


running = True
while running:
    screen.blit(mickey, (0, 0))
    time = datetime.datetime.now()
    clock.tick(30)
    r_center(screen, seconds, -time.second * 6, 400, 300)
    r_center(screen, minutes, -time.minute * 6 - 42, 400, 300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()