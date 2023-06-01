# Libraries
import pygame
import pickle
from os import path
import math
#import time

# Var Setup
yvel = 25
xvel = yvel*(1/8)
timevar = 1
first = True

"""
def store(item,file):
  with open(file,"wb") as f:
    pickle.dump(item,f)

def collect(file):
  if path.exists(file):
    with open(file,"rb") as f:
      return pickle.load(f)
  return None

FILE = "data.pkl"
data = collect(FILE)
if data is None:
  data = {}

# Edit data here
# https://replit.com/@RyanMagnus/Serialization#main.py

store(data, FILE)
"""

# GLOBAL VARIABLES
COLOR = (255, 100, 98)
SURFACE_COLOR = (248, 242, 180)
WIDTH = 1000
HEIGHT = 400
  
# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
  
        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)
  
        pygame.draw.rect(self.image,
                         color,
                         pygame.Rect(0, 0, width, height))
  
        self.rect = self.image.get_rect()

    # Movement
    def moveX(self, pixels):
        self.rect.x += pixels
    def moveY(self, pixels):
        self.rect.y += pixels

pygame.init()
  
RED = (255, 0, 0)
  
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")
  
all_sprites_list = pygame.sprite.Group()

# SPRITE CREATION
character_ = Sprite((240,128,128), 30, 30)
character_.rect.x = 100
character_.rect.y = 400

all_sprites_list.add(character_)

cloud_ = Sprite((240,243,243), 80, 110)
cloud_.rect.x = 300
cloud_.rect.y = 200

all_sprites_list.add(cloud_)

ground_ = Sprite((255,204,153), HEIGHT/3, WIDTH)
ground_.rect.x = 0
ground_.rect.y = HEIGHT/3 * 2

all_sprites_list.add(ground_)
 

# WINDOW CLOSING
exit = True
clock = pygame.time.Clock()
  
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
  
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    
    # Sprite Movement

    #accel = 3
    #hypvel = math.sqrt(xvel*xvel + yvel*yvel)
    #timetofall = ((2*hypvel*math.sin(45))/accel)

    yvel -= 1
    xvel -= 1
    character_.moveY(-yvel)
    character_.moveX(-xvel)

pygame.quit()