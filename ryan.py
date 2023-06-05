# Libraries
import pygame
from pygame.locals import *
import pickle
from os import path
import math
#import time

# Var Setup
yvel = 25
xvel = 10
FALL_RATE = 1

timevar = 1
first = True
squarechar = 30

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
SURFACE_COLOR = (245,234,164) #(248, 242, 180)
WIDTH = 1000
HEIGHT = 600#750
  
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

# Text
def text():
    #pygame.init()
    #screen = pygame.display.set_mode((480, 360))
    text = ""
    COLOR = (252,199,134)
    screen.fill(COLOR)
    font = pygame.font.Font(None, 50)
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isdigit():
                    text += evt.unicode
                    screen.fill(COLOR)
                elif evt.key == K_BACKSPACE:
                    text = text[:-1]
                    screen.fill(COLOR)
                elif evt.key == K_RETURN:
                    text = int(text)
                    screen.fill(COLOR)
                    return text
            elif evt.type == QUIT:
                text = ""
                return

        #screen.fill((0, 0, 0))
        block = font.render(text, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.flip()
"""
def write(text):
  font = pygame.font.Font(None,50)
  block = font.render(text,1,(255,255,255,))
  screen.blit(block,(20,20))
  pygame.display.update()
"""
pygame.init()
  
RED = (255, 0, 0)
  
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Launch Game")
  
all_sprites_list = pygame.sprite.Group()

# SPRITE CREATION
character_ = Sprite((240,128,128), squarechar, squarechar)
character_.rect.x = 100
character_.rect.y = HEIGHT/3 * 2 - squarechar - 1

cloud_ = Sprite((240,243,243), 80, 110)
cloud_.rect.x = 300
cloud_.rect.y = 200


ground_ = Sprite((252,199,134), HEIGHT/3, WIDTH) #fix scaling
ground_.rect.x = 0
ground_.rect.y = HEIGHT/3 * 2

all_sprites_list.add(ground_)
all_sprites_list.add(cloud_)
all_sprites_list.add(character_)

# WINDOW CLOSING
exit = True
clock = pygame.time.Clock()

# Text Input
print("Y speed? ")
#write("Y speed? ")
yvel = text()
while yvel > 25:
  print("\nToo big, try again!\nY speed? ")
  yvel = text()

print("X speed? ")
xvel = text()
while xvel > 50:
  print("\nToo big, try again!\nX speed? ")
  xvel = text()
xvel /= 3

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

    yvel -= FALL_RATE
    character_.moveY(-yvel)
    character_.moveX(xvel)


    """
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
              character_.moveX(10)
            elif event.key == pygame.K_LEFT:
              character_.moveX(-10)
            else:
              character_.moveX(0)
    """

    # Sprite Position Check
    charcenterX, charcenterY = character_.rect.center
    floortopLeftX, floortopLeftY = ground_.rect.topleft

    if charcenterY >= (HEIGHT/3) * 2:
        #character_.moveY(-squarechar/2 + 15)
        yvel = FALL_RATE
        xvel = 0
        print(charcenterX)

pygame.quit()