# Libraries
import pygame
from pygame.locals import *
import pickle
from os import path
import math
#import time

# Var Setup
yvel = 25 #init testing
xvel = 10 #init testing
FALL_RATE = 1

#timevar = 1
#first = True
squarechar = 30

pygame.init()

# Serialization
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
def textdig(caption):
    #pygame.init()
    #screen = pygame.display.set_mode((480, 360))
    text = ""
    COLOR = (252,199,134)
    screen.fill(COLOR)
    font = pygame.font.Font(None, 50)
    textfont = pygame.font.Font(None,50)
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

        #Caption
        textblock = textfont.render(caption, True, (255,255,255))
        textrect = textblock.get_rect()
        textrect.center = (screen.get_rect().center[0],200)
        screen.blit(textblock,textrect)
        pygame.display.flip()

def textalp(caption):
    #pygame.init()
    #screen = pygame.display.set_mode((480, 360))
    text = ""
    COLOR = (252,199,134)
    #screen.fill(COLOR)
    font = pygame.font.Font(None, 50)
    textfont = pygame.font.Font(None,50)
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    text += evt.unicode
                    screen.fill(COLOR)
                elif evt.key == K_BACKSPACE:
                    text = text[:-1]
                    screen.fill(COLOR)
                elif evt.key == K_RETURN:
                    text = text
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

        #Caption
        textblock = textfont.render(caption, True, (255,255,255))
        textrect = textblock.get_rect()
        textrect.center = (screen.get_rect().center[0],125)
        screen.blit(textblock,textrect)
        pygame.display.flip()

def write(text):
  textfont = pygame.font.Font(None,50)
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    textblock = textfont.render(text, True, (255,255,255))
    textrect = textblock.get_rect()
    textrect.center = (screen.get_rect().center[0],200)
    screen.blit(textblock,textrect)
    pygame.display.flip()
  
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Launch Game")
  
all_sprites_list = pygame.sprite.Group()

# SPRITE CREATION
character_ = Sprite((240,128,128), squarechar, squarechar)
character_.rect.x = 100
character_.rect.y = HEIGHT/3 * 2 - squarechar - 1

cloud_1 = Sprite((240,243,243), 80, 110)
cloud_1.rect.x = 235
cloud_1.rect.y = 200

cloud_2 = Sprite((240,243,243), 80, 110)
cloud_2.rect.x = 675
cloud_2.rect.y = 100

ground_ = Sprite((252,199,134), HEIGHT/3, WIDTH) #fix scaling
ground_.rect.x = 0
ground_.rect.y = HEIGHT/3 * 2

all_sprites_list.add(ground_)
all_sprites_list.add(cloud_1)
all_sprites_list.add(cloud_2)
all_sprites_list.add(character_)

# WINDOW CLOSING
exit = True
clock = pygame.time.Clock()

# Text Input
#print("Y speed? ")
#write("word")

yvel = textdig("Y Velocity? (Max 25)")
while yvel > 25:
  #print("\nToo big, try again!\nY speed? ")
  yvel = textdig("Too big! Y Velocity? (Max 25)")

#print("X speed? ")
xvel = textdig("X Velocity? (Max 50)")
while xvel > 50:
  #print("\nToo big, try again!\nX speed? ")
  xvel = textdig("Too big! X Velocity? (Max 50)")
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

    # Sprite Position Check
    charcenterX, charcenterY = character_.rect.center
    floortopLeftX, floortopLeftY = ground_.rect.topleft

    if charcenterY >= (HEIGHT/3) * 2:
        #character_.moveY(-squarechar/2 + 15) #floor collision attempt
        yvel = FALL_RATE
        xvel = 0
        #print(charcenterX)
        #input("Press Enter to continue. ")
        #print("Initials for score save? ")
        name = textalp("Initials?").upper()
        while len(name) > 3:
          name = textalp("Too long! Initials?").upper()
        else: 
          if name == "ZZZ":
            data = {}
          else:
            data[name] = charcenterX

          break

#print(data)
listdata = "Scores: " + str(data)
write(listdata)
store(data, FILE)

pygame.quit()