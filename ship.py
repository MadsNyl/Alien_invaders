import pygame as pg
from settings import *
from bullet import Bullet

class Ship(pg.sprite.Sprite):
    def __init__(self, x, y):
        self.groups = all_sprites, ships
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = PLAYER_IMG.convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.last_shot = 0
    
    def update(self):
        self.get_keys()
        self.pos += self.vel
        self.rect.center = self.pos
        self.wall_collision()

    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.vel.x = PLAYER_SPEED
        if keys[pg.K_SPACE]:
            now = pg.time.get_ticks()
            if now - self.last_shot > 400:
                self.shoot()
                self.last_shot = now
    
    def shoot(self):
        Bullet(self.pos, (0, -BULLET_SPEED))
    
    def wall_collision(self):
        self.rect.center = self.pos
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        