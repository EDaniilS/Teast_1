from pygame import *
from random import *
from time import time as timer

window = display.set_mode((700, 500))
display.set_caption('Шутер')

background = transform.scale(image.load('ggg.jpg'), (700, 500))
clock = time.Clock()
FPS = 60
