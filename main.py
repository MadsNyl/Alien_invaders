import pygame as pg
from random import randint
from alien import Alien
from settings import *
from ship import Ship

pg.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

player = Ship(WIDTH / 2, HEIGHT - 40)

def draw_text(text, size, x, y):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

run = True
while run:
    screen.fill(BLACK)
    clock.tick(FPS)

    all_sprites.draw(screen)
    all_sprites.update()

    draw_text(f'Lives: {lives}', 20, 40, 0)
    draw_text(f'Score: {score}', 20, 40, 25)


    if len(aliens) < 10:
        Alien(randint(40, WIDTH - 40), randint(-500, 0))
    
    for alien in aliens:
        if alien.rect.bottom >= HEIGHT:
            alien.kill()
            lives -= 1
    
    hits = pg.sprite.groupcollide(aliens, bullets, False, True)
    for hit in hits:
        score += 50
        hit.kill()
    
    hits = pg.sprite.spritecollide(player, aliens, True)
    for hit in hits:
        lives -= 1

    if lives == 0:
        run = False

    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False

    pg.display.flip()

pg.quit()