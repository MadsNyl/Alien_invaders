import pygame as pg
from random import choice
from settings import *

class Alien(pg.sprite.Sprite):
    def __init__(self, x, y):
        self.groups = all_sprites, aliens
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = choice(ALIEN_IMG).convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
        self.vel = vec(0, ALIEN_SPEED)
        self.pos = vec(x, y)
    
    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos