import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *
import numpy






pygame.init()  # Begin pygame

# Declaring variables to be used through the program
vec = pygame.math.Vector2
HEIGHT = 1080
WIDTH = 1920
ACC = 0.3
FRIC = -0.10
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0


# light shade of the button
color_light = (170,170,170)
color_dark = (100,100,100)
color_white = (255,255,255)

# defining a font
headingfont = pygame.font.SysFont("Verdana", 40)
regularfont = pygame.font.SysFont('Corbel',25)
smallerfont = pygame.font.SysFont('Corbel',16)
text = regularfont.render('LOAD' , True , color_light)

resolution = (WIDTH,HEIGHT)


flags = FULLSCREEN | DOUBLEBUF
displaysurface = pygame.display.set_mode(resolution, flags, 16)




hit_cooldown = pygame.USEREVENT + 1


ducking_ani_R = [pygame.image.load("./RESOURCES/HERO/Hero1.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero1_ducking_R.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero1_ducking_R.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero1_ducking_R.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero1_ducking_R.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero1_ducking_R.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero1_ducking_R.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero1.png").convert_alpha()]

ducking_ani_L = [pygame.image.load("./RESOURCES/HERO/Hero1_L.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero1_ducking_L.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero1_ducking_L.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero1_ducking_L.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero1_ducking_L.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero1_ducking_L.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero1_ducking_L.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero1_L.png").convert_alpha()]

run_ani_R = [pygame.image.load("./RESOURCES/HERO/Hero1.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_move1.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero_move1.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_move1.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero_move1.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_move2.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero_move2.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_move2.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero_move2.png").convert_alpha()]

run_ani_L = [pygame.image.load("./RESOURCES/HERO/Hero1_L.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_move1_L.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero_move1_L.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_move1_L.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero_move1_L.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_move2_L.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero_move2_L.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_move2_L.png").convert_alpha(),pygame.image.load("./RESOURCES/HERO/Hero_move2_L.png").convert_alpha()]


attack_ani_R = [pygame.image.load("./RESOURCES/HERO/Hero1.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_swing.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_swing.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_swing.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_swing.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_swing.png").convert_alpha()]

attack_ani_L = [pygame.image.load("./RESOURCES/HERO/Hero1_L.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_swing_L.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_swing_L.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_swing_L.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_swing_L.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_swing_L.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/Hero_swing_L.png").convert_alpha()]

health_ani = [pygame.image.load("./RESOURCES/HERO/tire0.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/tire1.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/tire2.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/tire3.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/tire4.png").convert_alpha(), pygame.image.load("./RESOURCES/HERO/tire5.png").convert_alpha()]

















#displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Carrer")

class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.bgimage = pygame.image.load("./RESOURCES/BACKGROUND/wallpaper.png").convert_alpha()
            self.bgY = 0
            self.bgX = 0
      def render(self):
          displaysurface.blit(self.bgimage, (self.bgX, self.bgY))

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./RESOURCES/GROUND/ground.png").convert_alpha()
        self.rect = self.image.get_rect(center = (400, 600))

    def render(self):
        displaysurface.blit(self.image, (self.rect.x, self.rect.y))



class Castle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hide = False
        self.image = pygame.image.load("./RESOURCES/GAMEOBJECTS/Castle.png").convert_alpha()

    def update(self):
        if self.hide == False:
            displaysurface.blit(self.image, (400,270))




class EventHandler():
    def __init__(self):
        self.enemy_count = 0
        self.battle = False
        self.enemy_generation = pygame.USEREVENT + 2
        self.enemy_generation2 = pygame.USEREVENT + 3
        self.stage = 1
        self.dead_enemy_count = 0
        self.levelcomplete = False
        self.world = 0

        self.stage_enemies = []
        for x in range(1,21):
            self.stage_enemies.append(int((x ** 2 / 2) + 1))

    def next_stage(self):
        button.imgdisp = 1
        self.stage += 1
        self.enemy_count = 0
        print("Stage: " + str(self.stage))
        pygame.time.set_timer(self.enemy_generation, 1500 - (50 * self.stage))
        self.dead_enemy_count = 0

        if self.world == 1:
            pygame.time.set_timer(self.enemy_generation, 1500 - (50 * self.stage))
        if self.world == 2:
            pygame.time.set_timer(self.enemy_generation2, 1500 - (50 * self.stage))


    def stage_handler(self):
        #tkinter stage selection
        self.root = Tk()
        self.root.geometry('300x270')

        button1 = Button(self.root, text = "O'Rielys Dungeon", width = 18, height = 2, command = self.world1)

        button2 = Button(self.root, text = "Advance Auto Parts Dungeon" , width = 18, height = 2, command = self.world2)

        button3 = Button(self.root, text = "Autozone Dungeon", width = 18, height = 2 , command = self.world3)
        button1.place(x = 40, y = 15)
        button2.place(x = 40, y = 65)
        button3.place(x = 40, y = 115)

        self.root.eval('tk::PlaceWindow . center')
        self.root.mainloop()


    def world1(self):
        self.root.destroy()
        pygame.time.set_timer(self.enemy_generation, 2000)
        button.imgdisp = 1
        castle.hide = True
        self.battle = True
        background.bgimage = pygame.image.load("./BACKRESOURCES/GROUND/Background_world1.jpeg").convert_alpha()
        ground.image = pygame.image.load("./RESOURCES/GROUND/ground_world1.png").convert_alpha()


    def world2(self):
        self.root.destroy()
        background.bgimage = pygame.image.load("./BACKRESOURCES/GROUND/background_world2.jpg").convert_alpha()
        ground.image = pygame.image.load("./RESOURCES/GROUND/ground_world2.png").convert_alpha()

        pygame.time.set_timer(self.enemy_generation2, 2500)

        self.world = 2
        castle.hide = True
        self.battle = True
        button.imgdisp = 1

    def world3(self):
        self.battle = True
        button.imgdisp = 1
    def update(self):
        if self.dead_enemy_count == self.stage_enemies[self.stage -1]:
            self.dead_enemy_count = 0
            stage_display.clear = True
            stage_display.stage_clear()
            self.levelcomplete = True

    def home(self):
        #reset battle code
        pygame.time.set_timer(self.enemy_generation, 0)
        pygame.time.set_timer(self.enemy_generation2, 0 )

        self.battle = False
        self.enemy_count = 0
        self.dead_enemy_count = 0
        self.stage = 0
        self.world = 0
        health.image = pygame.image.load("./RESOURCES/HERO/tire5.png").convert_alpha()
        player.health = 5

        #destroy enemites and items
        for group in Enemies, Items:
            for entity in group:
                entity.kill()

        #normalize background
        castle.hide = False
        background.bgimage = pygame.image.load("./BACKRESOURCES/GROUND/wallpaper.png").convert_alpha()
        ground.image = pygame.image.load("./RESOURCES/GROUND/ground.png").convert_alpha()


class HealthBar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./RESOURCES/HERO/tire5.png").convert_alpha()

    def render(self):
        displaysurface.blit(self.image, (10,10))




class StageDisplay(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.text = headingfont.render("STAGE: " + str(handler.stage), True, color_dark)
        self.rect = self.text.get_rect()
        self.posx = -100
        self.posy = 100
        self.display = False
        self.clear = False

    def stage_clear(self):
        self.text = headingfont.render("STAGE CLEAR!", True, color_dark)
        button.imgdisp = 0
        if self.posx < 800:
            self.posx += 10
            displaysurface.blit(self.text, (self.posx, self.posy))
        else:
            self.clear = False
            self.posx = -100
            self.posy = 100


    def move_display(self):
        self.text = headingfont.render("STAGE: " + str(handler.stage), True, color_dark)
        if self.posx < 800:
            self.posx += 5
            displaysurface.blit(self.text, (self.posx, self.posy))
        else:
            self.display = False
            self.posx = -100
            self.posy = 100



class StatusBar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((90,66))
        self.rect = self.surf.get_rect(center = (500,10))
        self.xp = player.xp
    def update_draw(self):
        #create text
        text1 = smallerfont.render("STAGE: " + str(handler.stage), True, color_white)
        text2 = smallerfont.render("EXP: " + str(player.xp), True, color_white)
        text3 = smallerfont.render("MANA: " + str(player.mana), True, color_white)
        text4 = smallerfont.render("FPS: " + str(int(FPS_CLOCK.get_fps())), True, color_white)
        text5 = smallerfont.render("SOULS OF FALLEN FOES: " + str(player.souls), True, color_white)

        #draws text to status StatusBar
        displaysurface.blit(text1, (595,7))
        displaysurface.blit(text2, (595,22))
        displaysurface.blit(text3, (595,37))
        displaysurface.blit(text4, (595,52))
        displaysurface.blit(text5, (595,67))




class Item(pygame.sprite.Sprite):
    def __init__(self,itemtype):
        super().__init__()
        if itemtype == 1: self.image = pygame.image.load("./RESOURCES/HERO/tire1.png").convert_alpha()
        elif itemtype == 2: self.image = pygame.image.load("./RESOURCES/ENEMY/soul.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.type = itemtype
        self.posx = 0
        self.posy = 0

    def render(self):
        self.rect.x = self.posx
        self.rect.y = self.posy
        displaysurface.blit(self.image, self.rect)

    def update(self):
        hits = pygame.sprite.spritecollide(self, playergroup, False)
        #code to be activated if item comes in conectact with pklayer
        if hits:
            if player.health < 5 and self.type == 1:
                player.health += 1
                health.image = health_ani[player.health]
                self.kill()
            if self.type == 2:
                player.souls += 1
                self.kill()



class PButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.vec = vec(620, 300)
        self.imgdisp = 0

    def render(self, num):
        if (num == 0):
            self.image = pygame.image.load("./RESOURCES/BUTTON/home.png").convert_alpha()
        elif (num == 1):
            if cursor.wait == 0:
                self.image = pygame.image.load("./RESOURCES/BUTTON/pause.png").convert_alpha()
            else:
                self.image = pygame.image.load("./RESOURCES/BUTTON/play.png").convert_alpha()

        displaysurface.blit(self.image, self.vec)


class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./RESOURCES/BUTTON/cursor.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.wait = 0

    def pause(self):
        if self.wait == 1:
            self.wait = 0
        else:
            self.wait = 1

    def hover(self):
        if 620 <= mouse[0] <= 670 and 300 <= mouse[1] <= 345:
            pygame.mouse.set_visible(False)
            cursor.rect.center = pygame.mouse.get_pos()  # update mouse
            displaysurface.blit(cursor.image, cursor.rect)
        else:
            pygame.mouse.set_visible(True)



class FireBall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.direction = player.direction
        if self.direction == "RIGHT":
            self.image = pygame.image.load("./RESOURCES/PROJECTILE/fireball_R.png").convert_alpha()
        else:
            self.image = pygame.image.load("./RESOURCES/PROJECTILE/fireball_L.png").convert_alpha()
        self.rect = self.image.get_rect(center = player.pos)
        self.rect.x = player.pos.x
        self.rect.y = player.pos.y - 40

    def fire(self):
        player.magic_cooldown = 0
        #runs while on screen
        if -10 < self.rect.x < 710:
            if self.direction == "RIGHT":
                self.image = pygame.image.load("./RESOURCES/PROJECTILE/fireball_R.png").convert_alpha()
                displaysurface.blit(self.image, self.rect)
            else:
                self.image = pygame.image.load("./RESOURCES/PROJECTILE/fireball_L.png").convert_alpha()
                displaysurface.blit(self.image, self.rect)

            if self.direction == "RIGHT":


                self.rect.move_ip(6,0)
                if self.rect.x - abs(player.pos.x) > 100:
                    self.rect.move_ip(12,0)

            else:
                self.rect.move_ip(-12,0)

        else:
            self.kill()
            player.magic_cooldown = 1
            player.attacking = False


























class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./RESOURCES/HERO/Hero1.png").convert_alpha()
        self.rect = self.image.get_rect()
        #Combat
        self.attacking = False
        self.cooldown = False
        self.attack_frame = 0
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
        self.ducking = False
        self.lasttime = pygame.time.get_ticks()
        self.health = 5
        self.mana = 0
        self.xp = 0
        self.souls = 0


    def move(self):
      if cursor.wait ==1: return
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
      if pressed_keys[K_SPACE]:
          if self.direction == "RIGHT":
              self.acc.x += 2
          if self.direction == "LEFT":
              self.acc.x -=2

      self.acc.x += self.vel.x * FRIC
      self.vel += self.acc
      self.pos += self.vel + 0.5 * self.acc

      if self.pos.x > WIDTH:
          self.pos.x = 0
      if self.pos.x < 0:
          self.pos.x = WIDTH

      self.rect.midbottom = self.pos

    def jump(self):
        self.rect.x +=1

        #check for contact with ground
        hits = pygame.sprite.spritecollide(self,ground_group, False)

        self.rect.x -=1

        #if touching ground and not jumping jump
        if hits and not self.jumping:

            self.jumping = True
            self.vel.y = -18
    def duck(self):
        self.ducking = True
        now = pygame.time.get_ticks()
       # print("now:",now,"cooldown",self.cooldown,"lasttime:",self.lasttime)
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_s]:
            self.ducking = True
        else:
            self.ducking = False


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
        if cursor.wait == 1: return
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

        if self.ducking == True and self.jumping == False:
            if self.direction == "LEFT":
                self.image = ducking_ani_L[self.move_frame]
                self.move_frame += 1
            else:
                self.image = ducking_ani_R[self.move_frame]
                self.move_frame += 1


        now = pygame.time.get_ticks()
        if now - self.lasttime >= 1000 :
            self.lasttime = now
            self.ducking = False


        if self.ducking and self.move_frame != 0:
            self.move_frame = 0






        #return postition if incorrect move_frameif
        if abs (self.vel.x) <.4 and self.move_frame !=0:
            self.move_frame = 0
            if self.direction == "RIGHT":
                self.image = run_ani_R[self.move_frame]
            elif self.direction == "LEFT":
                self.image = run_ani_L[self.move_frame]


    def attack(self):
        if cursor.wait == 1: return
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


    def player_hit(self):
        if self.cooldown == False:
            self.cooldown = True #enables cooldown
            pygame.time.set_timer(hit_cooldown, 1000) #resets cooldown

            print("hit")

            self.health = self.health -1
            health.image = health_ani[self.health]

            if self.health <= 0:
                self.kill()
            pygame.display.update()























class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./RESOURCES/ENEMY/frog2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = vec(0,0)
        self.vel = vec(0,0)

        self.direction = random.randint(0,1) #0 for right 1 for left
        self.vel.x = random.randint(2,6) /2  #rand velocity
        self.mana = random.randint(1,3)
        #initial position
        if self.direction == 0:
            self.pos.x = 0
            self.pos.y =400
        if self.direction == 1:
            self.pos.x = 900
            self.pos.y = 400


    def move(self):
        if cursor.wait == 1: return
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





    def update(self):
        #checks collision
        hits = pygame.sprite.spritecollide(self, playergroup, False)

        #checks fireball collision
        f_hits = pygame.sprite.spritecollide(self, Fireballs, False)

        if hits and player.attacking == True or f_hits:
            print("Enemy killed")
            if player.mana < 100: player.mana += self.mana
            player.xp += 1
            self.kill()

            rand_num = numpy.random.uniform(0,100)
            item_no = 0
            if rand_num >=0 and rand_num <=5:           #one in twenty
                item_no = 1
            elif rand_num > 5 and rand_num <= 15:       #one in ten
                item_no = 2
            if item_no != 0:
                #add item to items group
                item = Item(item_no)
                Items.add(item)
                #set location to killed enemy
                item.posx = self.pos.x
                item.posy = self.pos.y





            handler.dead_enemy_count += 1


        elif hits and player.attacking == False:
            if cursor.wait == 0: pass
            player.player_hit()


class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = vec(0,0)
        self.vel = vec(0,0)
        self.wait = 0
        self.wait_status = False
        self.turning = 0

        self.direction = random.randint(0,1)    #0 for right
        self.vel.x = random.randint(2,6) / 3    # random velocity
        self.mana = random.randint(2,3)         #random mana

        if self.direction == 0: self.image =                    pygame.image.load("./RESOURCES/ENEMY/waluigi.png").convert_alpha()
        if self.direction == 1: self.image = pygame.image.load("./RESOURCES/ENEMY/waluigi_L.png").convert_alpha()
        self.rect = self.image.get_rect()

        #sets initial position of enemy
        if self.direction == 0:
            self.pos.x = 0
            self.pos.y = 250
        if self.direction == 1:
            self.pos.x = 700
            self.pos.y = 250


    def move(self):
        if cursor.wait ==1: return

        #causes enemy to change directions when reaching wall
        if self.pos.x >= (WIDTH-20):
            self.direction = 1
        elif self.pos.x <= 0:
            self.direction = 0


        #updates position with new values
        if self.wait > 50:
            self.wait_status = True
        elif int(self.wait) <= 0:
            self.wait_status = False

        if self.direction_check():
            self.turn()
            self.wait = 90
            self.turning = 1

        if self.wait_status == True:
            rand_num = numpy.random.uniform(0,50)
            if int(rand_num) == 25:
                bolt = Bolt(self.pos.x, self.pos.y, self.direction)
                Bolts.add(bolt)
            self.wait -= 1

        elif self.direction == 0:
            self.pos.x += self.vel.x
            self.wait += self.vel.x
        elif self.direction == 1:
            self.pos.x -= self.vel.x
            self.wait += self.vel.x

        self.rect.topleft = self.pos # updates rect

    def update(self):
        #checks collision with player
        hits = pygame.sprite.spritecollide(self, playergroup, False)
        #checks fireballs
        f_hits = pygame.sprite.spritecollide(self, Fireballs, False)

        #if either of the above is true
        if hits and player.attacking == True or f_hits:
            self.kill()
            handler.dead_enemy_count += 1

            if player.mana < 100: player.mana += self.mana
            player.xp += 1

            rand_num = numpy.random.uniform(0, 100)
            item_no = 0
            if rand_num >= 0 and rand_num <= 5:     #1/20 chance
                item_no = 1
            elif rand_num > 5 and rand_num <= 15:
                item_no = 2

            if item_no != 0:
                #add item to items group
                item = Item(item_no)
                Items.add(item)
                #sets item location to dead enemy
                item.posx = self.pos.x
                item.posy = self.pos.y


    def render(self):
        #display on screen
        displaysurface.blit(self.image, self.rect)

    def direction_check(self):
        if (player.pos.x - self.pos.x < 0 and self.direction == 0):
            return 1
        elif (player.pos.x - self.pos.x > 0 and self.direction == 1):
            return 1
        else:
            return 0


    def turn(self):
        if self.wait > 0:
            self.wait -= 1
            return
        elif int(self.wait) <= 0:
            self.turning = 0

        if (self.direction):
            self.direction = 0
            self.image = pygame.image.load("./RESOURCES/ENEMY/waluigi.png").convert_alpha()
        else:
            self.direction = 1
            self.image = pygame.image.load("./RESOURCES/ENEMY/waluigi2.png").convert_alpha()


class Bolt(pygame.sprite.Sprite):
    def __init__(self, x, y ,d):
        super().__init__()
        self.image = pygame.image.load("./RESOURCES/PROJECTILE/bolt.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x + 15
        self.rect.y = y + 20
        self.direction = d

    def fire(self):
        #runs while bolt is within the screen
        if -10 < self.rect.x < 710:
            if self.direction == 0:
                self.image = pygame.image.load("./PROJECTILEbolt.png").convert_alpha()
                displaysurface.blit(self.image, self.rect)
            else:
                self.image = pygame.image.load("./PROJECTILEbolt_L.png").convert_alpha()
                displaysurface.blit(self.image, self.rect)

            if self.direction == 0:
                self.rect.move_ip(12, 0)
            else:
                self.rect.move_ip(-12, 0)

        else:
            self.kill()

        #checks collision
        hits = pygame.sprite.spritecollide(self, playergroup, False)
        if hits:
            player.player_hit()
            self.kill()



















background = Background()
ground = Ground()
player=Player()
playergroup = pygame.sprite.Group()
playergroup.add(player)
ground_group = pygame.sprite.Group()
ground_group.add(ground)

Fireballs = pygame.sprite.Group()

castle = Castle()
handler = EventHandler()

Enemies = pygame.sprite.Group()


health = HealthBar()


status_bar = StatusBar()


stage_display = StageDisplay()

Items = pygame.sprite.Group()

button = PButton()

cursor = Cursor()

Bolts = pygame.sprite.Group()








while True:
    player.gravity_check()
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # Will run when the close window button is clicked
        if event.type == hit_cooldown:
            player.cooldown = False
            pygame.time.set_timer(hit_cooldown, 0)

        if event.type == handler.enemy_generation:
            print("count: ", handler.enemy_count, "  stage enemies: ",  handler.stage_enemies[handler.stage -1])
            while handler.enemy_count < handler.stage_enemies[handler.stage -1]:
                enemy = Enemy()
                Enemies.add(enemy)
                handler.enemy_count +=  1#handler.stage_enemies[handler.stage -1] - handler.enemy_count

        if event.type == handler.enemy_generation2:
            if handler.enemy_count < handler.stage_enemies[handler.stage -1]:
                enemy = Enemy2()
                Enemies.add(enemy)
                handler.enemy_count += 1


        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # For events that occur upon clicking the mouse (left click)
        if event.type == pygame.MOUSEBUTTONDOWN:
              if 620 <= mouse[0] <= 670 and 300 <= mouse[1] <= 345:
                  if button.imgdisp == 1:
                      cursor.pause()
                  elif button.imgdisp == 0:
                        handler.home()

        # Event handling for a range of different key presses
        if event.type == pygame.KEYDOWN and cursor.wait == 0:
              if event.key == pygame.K_k and 350 < player.rect.x < 550 and castle.hide == False:
                  print("open castle")
                  handler.stage_handler()
              if event.key == pygame.K_w:
                  player.jump()
              if event.key == pygame.K_j:
                  if player.attacking == False:
                      player.attack()
                      player.attacking = True
              if event.key == pygame.K_s:
                  player.duck()
              if event.key == pygame.K_m:
                  print("stage enemies[handler.stage -1] " ,handler.stage_enemies[handler.stage -1] , " dead_enemy_count " , handler.dead_enemy_count, "levelcomplete ", handler.levelcomplete, "enemy count ", handler.enemy_count)
                  #print( "stage enemies " , handler.stage_enemies ,"genration ", handler.enemy_generation, "Enemies ", Enemies)
              if event.key == pygame.K_n:

                  if handler.battle == True and handler.levelcomplete == True:
                      handler.next_stage()
                      stage_display = StageDisplay()
                      stage_display.display = True
                      handler.levelcomplete = False

              if event.key == pygame.K_l: # and player.magic_cooldown == 1
       #           if player.mana >= 6:
        #              player.mana -= 6
                      player.attacking = True
                      fireball = FireBall()
                      Fireballs.add(fireball)




    background.render()
    ground.render()
    button.render(button.imgdisp)
    cursor.hover()
    castle.update()

    player.update()

    if player.attacking == True:
        player.attack()
    player.move()


    if player.health > 0:
          displaysurface.blit(player.image, player.rect)
    health.render()
    for ball in Fireballs:
        ball.fire()
    for bolt in Bolts:
        bolt.fire()

    for entity in Enemies:
            entity.update()
            entity.move()
            entity.render()

    # Render stage display
    if stage_display.display == True:
        stage_display.move_display()
    if stage_display.clear == True:
        stage_display.stage_clear()


    for i in Items:
        i.render()
        i.update()



    # Status bar update and render
   # print(dir(EventHandler))
    #print(dir(status_bar))
    displaysurface.blit(status_bar.surf, (580, 5))
    status_bar.update_draw()
    handler.update()



    pygame.display.update()
    FPS_CLOCK.tick(FPS)
