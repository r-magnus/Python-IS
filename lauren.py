# Libraries
import pygame
import pickle
from os import path
#import time

# Var Setup
xvel = 0
yvel = 0
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
HEIGHT = 500
  
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

cloud_ = Sprite((240,243,243), 30, 60)
cloud_.rect.x = 300
cloud_.rect.y = 200

all_sprites_list.add(cloud_)
 

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
    
    #timevar += 1
    #xvel = 1/timevar+1
    while timevar <= 50:
        timevar += 1
        yvel = -(1/timevar)*5
    else:
        if first:
            fall = timevar
            first = False
        yvel = (timevar/fall)*5

    # Sprite Movement
    character_.moveX(xvel)
    character_.moveY(yvel)

pygame.quit()