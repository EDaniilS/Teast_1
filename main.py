from pygame import *
from random import *
from time import time as timer

window = display.set_mode((700, 500))
display.set_caption('Шутер')

background = transform.scale(image.load('ggg.jpg'), (700, 500))
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('space.ogg')
mixer.music.set_volume(0.2)
mixer.music.play()

fire = mixer.Sound('fire.ogg')

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, x, y, widht, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (widht, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 'l'
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
