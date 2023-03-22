from pygame import *
class GameSprite (sprite.Sprite):
    def __init__(self ,x, y, w, h, picturename):
        super().__init__()
        self.image = transform.scale(image.load(picturename), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset (self):
        window.blit(self.image, (self.rect.x,self.rect.y ))
class Humanatack(GameSprite):           
    def __init__ (self ,x, y, w, h, picturename, name, health, damage, cost):    
        GameSprite.__init__(self, x, y, w, h, picturename)     
        self.name = name         
        self.health = health         
        self.damage = damage         
        self.cost = cost 
class Humanmoney():     
    def __init__ (self, name, health, money, cost):         
        self.name = name         
        self.health = health         
        self.money = money         
        self.cost = cost 
class Humandef():     
    def __init__ (self, name, health, money, cost):         
        self.name = name         
        self.health = health         
        self.cost = cost
     
class Vrag ():
    def __init__(self, x, y, w, h, picturename, speed):
        GameSprite.__init__(self, x, y, w, h, picturename)
        self.speed = speed
        self.direction = 'left'
    def update(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if self.rect.x >= 650:
            self.direction = 'left'
        elif self.rect.x <=560:
            self.direction = 'RIGHT'
turrel = Humanatack (120, 60, 50, 50,'turrel.png', 'Защитная турель', 150, 20, 120)
humanmoney = ('Денежная машина', 120, 40, 60) 
humandef = ('Стена', 700, 80)

window = display.set_mode((700, 500))
display.set_caption('Окно')
picture = transform.scale(image.load('level_1.png'), (700, 500))

run = True
while run:
    for e in event.get():
       if e.type == QUIT:
           run = False

    window.blit(picture, (0, 0))
    turell.reset()
    display.update()
    time.delay(1)