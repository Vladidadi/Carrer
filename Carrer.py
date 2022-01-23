import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *

pygame.init()  # Begin pygame

# Declaring variables to be used through the program
vec = pygame.math.Vector2
HEIGHT = 600
WIDTH = 800
ACC = 0.3
FRIC = -0.10
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0


hit_cooldown = pygame.USEREVENT + 1

run_ani_R = [pygame.image.load("Hero1.png"), pygame.image.load("Hero_move1.png"),pygame.image.load("Hero_move1.png"), pygame.image.load("Hero_move1.png"),pygame.image.load("Hero_move1.png"), pygame.image.load("Hero_move2.png"),pygame.image.load("Hero_move2.png"), pygame.image.load("Hero_move2.png"),pygame.image.load("Hero_move2.png")]

run_ani_L = [pygame.image.load("Hero1.png"), pygame.image.load("Hero_move1.png"),pygame.image.load("Hero_move1.png"), pygame.image.load("Hero_move1.png"),pygame.image.load("Hero_move1.png"), pygame.image.load("Hero_move2.png"),pygame.image.load("Hero_move2.png"), pygame.image.load("Hero_move2.png"),pygame.image.load("Hero_move2.png")]


attack_ani_R = [pygame.image.load("Hero1.png"), pygame.image.load("Hero_swing.png"), pygame.image.load("Hero_swing.png"), pygame.image.load("Hero_swing.png"), pygame.image.load("Hero_swing.png"), pygame.image.load("Hero_swing.png")]

attack_ani_L = [pygame.image.load("Hero1.png"), pygame.image.load("Hero_swing.png"), pygame.image.load("Hero_swing.png"), pygame.image.load("Hero_swing.png"), pygame.image.load("Hero_swing.png"), pygame.image.load("Hero_swing.png"), pygame.image.load("Hero_swing.png")]


displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Carrer")

class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.bgimage = pygame.image.load("wallpaper.png")
            self.bgY = 0
            self.bgX = 0
      def render(self):
          displaysurface.blit(self.bgimage, (self.bgX, self.bgY))

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ground.png")
        self.rect = self.image.get_rect(center = (400, 600))

    def render(self):
        displaysurface.blit(self.image, (self.rect.x, self.rect.y))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Hero1.png")
        self.rect = self.image.get_rect()

        #position and direction
        self.vx=0
        self.pos = vec (( 100,400))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.direction = "RIGHT"
        self.jumping = False
        self.running = False
        self.move_frame = 0
        self.attacking = False
        self.attack_frame = 0


    def move(self):
      #will set to slow if player is slowed down
      self.acc = vec(0,0.5)    ###tutorial says use vel instead of vec
      if abs(self.vel.x) > .3:
          self.running = True
      else:
          self.runnign = False
      pressed_keys = pygame.key.get_pressed()

      if pressed_keys[K_a]:
          self.acc.x = -ACC
      if pressed_keys[K_d]:
          self.acc.x = ACC

      self.acc.x += self.vel.x * FRIC
      self.vel += self.acc
      self.pos += self.vel + 0.5 * self.acc

      if self.pos.x > WIDTH:
          self.pos.x = 0
      if self.pos.x < 0:
          self.pos.x = WIDTH

      self.rect.midbottom = self.pos
    def update(self):
        pass

    def attack(self):
        pass

    def jump(self):
        self.rect.x +=1

        #check for contact with ground
        hits = pygame.sprite.spritecollide(self,ground_group, False)

        self.rect.x -=1

        #if touching ground and not jumping jump
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -12


    def gravity_check(self):
        hits = pygame.sprite.spritecollide(player,ground_group, False)
        if self.vel.y > 0:
            if hits:
                lowest = hits[0]
                if self.pos.y < lowest.rect.bottom:
                    self.pos.y = lowest.rect.top + 1
                    self.vel.y = 0
                    self.jumping = False



    def update(self):
        if self.move_frame > 6 :
            self.move_frame = 0
            return

        if self.jumping == False and self.running == True:
            if self.vel.x > 0:
                self.image = run_ani_R[self.move_frame]
                self.direction = "RIGHT"
            else:
                self.image = run_ani_L[self.move_frame]
                self.direction = "LEFT"
            self.move_frame +=1
        #return postition if incorrect move_frameif
        if abs (self.vel.x) <.4 and self.move_frame !=0:
            self.move_frame = 0
            if self.direction == "RIGHT":
                self.image = run_ani_R[self.move_frame]
            elif self.direction == "LEFT":
                self.image = run_ani_L[self.move_frame]


    def attack(self):
        #if atk frame ends return normal player
        if self.attack_frame > 5:
            self.attack_frame = 0
            self.attacking = False

        #check direction
        if self.direction == "RIGHT":
            self.image = attack_ani_R[self.attack_frame]
        elif self.direction =="LEFT":
        #    self.correction()
            self.image = attack_ani_L[self.attack_frame]

        self.attack_frame += 1
























class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("frog.png")
        self.rect = self.image.get_rect()
        self.pos = vec(0,0)
        self.vel = vec(0,0)

        self.direction = random.randint(0,1) #0 for right 1 for left
        self.vel.x = random.randint(2,6) /2  #rand velocity

        #initial position
        if self.direction == 0:
            self.pos.x = 0
            self.pos.y =235
        if self.direction == 1:
            self.pos.x = 900
            self.pos.y = 235


    def move(self):
        #change directions at end of map
        if self.pos.x >= (WIDTH - 20):
            self.direction = 1
        elif self.pos.x <= 0:
            self.direction = 0

    #update with new values
        if self.direction == 0:
            self.pos.x += self.vel.x
        if self.direction == 1:
            self.pos.x -= self.vel.x

        self.rect.center = self.pos #updates rect

    def render(self):
        # Displayed the enemy on screen
        displaysurface.blit(self.image, (self.pos.x, self.pos.y))

enemy = Enemy()



background = Background()
ground = Ground()
player=Player()

ground_group = pygame.sprite.Group()
ground_group.add(ground)
















while True:
    player.gravity_check()
    for event in pygame.event.get():
        # Will run when the close window button is clicked
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # For events that occur upon clicking the mouse (left click)
        if event.type == pygame.MOUSEBUTTONDOWN:
              pass

        # Event handling for a range of different key presses
        if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_w:
                  player.jump()
              if event.key == pygame.K_j:
                  if player.attacking == False:
                      player.attack()
                      player.attacking = True



    # Render Functions ------
    player.update()
    if player.attacking == True:
        player.attack()
    player.move()
    background.render()
    ground.render()
    enemy.render()
    enemy.move()
    displaysurface.blit(player.image, player.rect)

    pygame.display.update()
    FPS_CLOCK.tick(FPS)
