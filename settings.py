import pygame as pg
vec = pg.math.Vector2

# display settings
WIDTH = 480
HEIGHT = 540
FPS = 60
font_name = pg.font.match_font('arial')


# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# groups
all_sprites = pg.sprite.Group()
ships = pg.sprite.Group()
aliens = pg.sprite.Group()
bullets = pg.sprite.Group()

# player settings
PLAYER_SPEED = 5
PLAYER_IMG = pg.image.load('img/ship.png')
lives = 3
score = 0

# alien settings
ALIEN_SPEED = 1
ALIEN_IMG = [pg.image.load('img/monster1.png'),
            pg.image.load('img/monster2.png'),
            pg.image.load('img/monster3.png'),
            pg.image.load('img/monster4.png'),
            pg.image.load('img/monster5.png')]

# bullet settings
BULLET_SPEED = 10
BULLET_IMG = pg.image.load('img/bullet.png')
