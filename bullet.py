import pygame as pg
from settings import *

class Bullet(pg.sprite.Sprite):
    def __init__(self, pos, vel):
        self.groups = all_sprites, bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = BULLET_IMG.convert_alpha()
        self.rect = self.image.get_rect(center=(pos))
        self.vel = vec(vel)
        self.pos = vec(pos)
    
    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        self.kill_bullet()
    
    def kill_bullet(self):
        if self.rect.top < 0:
            self.kill()