from pygame import *

init()
class GameSprite (sprite.Sprite):
    def __init__(self ,x, y, w, h, picturename):
        super().__init__()
        self.image = transform.scale(image.load(picturename), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def reset (self):
        window.blit(self.image, (self.rect.x,self.rect.y ))
        
        
class Player(GameSprite):
    def __init__(self, x, y, w, h, picturename, player_x_speed, player_y_speed):
        GameSprite.__init__(self, x, y, w, h, picturename)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
        
    def fire (self):
        bullet = Bullet(self.rect.right, self.rect.centery, 40, 40, 'bomb.png', 3)
        bullets.add(bullet)
        
    def update(self):
        self.rect.x += self.x_speed
        platforms_toched = sprite.spritecollide(self, walls, False)
        if self.x_speed > 0:
            for p in platforms_toched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_toched:
                self.rect.left = max(self.rect.left, p.rect.right)
        self.rect.y += self.y_speed
        platforms_toched = sprite.spritecollide(self, walls, False)
        if self.y_speed > 0:
            for p in platforms_toched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_toched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
        if packman.rect.x < 0:
           self.rect.x = 0
        elif packman.rect.right > 700:
           self.rect.right = 700 
        elif packman.rect.y < 0:
           self.rect.y = 0
        elif packman.rect.bottom > 500:
            self.rect.bottom = 500
            
            
class Vrag (GameSprite):
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
        elif sprite.spritecollide(self, walls, False):
            self.direction = 'RIGHT'
            
            
class Bullet (GameSprite):
    def __init__(self, x, y, w, h, picturename, speed):
        GameSprite.__init__(self, x, y, w, h, picturename)
        self.speed = speed
        
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 700:
            self.kill()
            
            
window = display.set_mode((700, 500))
display.set_caption('Окно')
run = True
picture = transform.scale(image.load('Фон для програмирования.jpg'), (700, 500))
packman = Player (50, 50, 50, 50, 'pac-2.png', 0, 0)
wall = GameSprite (300, 200, 50, 300, 'wall.png')
wall2 = GameSprite (300, 200, 190, 50, 'wall.png')
wall3 = GameSprite (350, 0, 50, 120, 'wall.png')
wall4 = GameSprite (480, 50, 50, 200, 'wall.png')
final = GameSprite (410, 320, 50, 50, 'final.png')
monster = Vrag (610, 190, 50, 50, 'bomb-4.png', 1)
monster2 = Vrag (440, 320, 50, 50, 'bomb-4.png', 1)
walls = sprite.Group()
bullets = sprite.Group()
monsters = sprite.Group()
monsters.add(monster)
monsters.add(monster2)
walls.add(wall)
walls.add(wall2)
walls.add(wall4)
walls.add(wall3)
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -2
            elif e.key == K_RIGHT:
                packman.x_speed = 2
            elif e.key == K_UP:
                packman.y_speed = -2
            elif e.key == K_DOWN:
                packman.y_speed = 2
            elif e.key == K_SPACE:
                packman.fire()
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed = 0
            elif e.key == K_UP:
                packman.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0
    if finish == False:
        window.blit(picture, (0, 0))
        packman.update()
        packman.reset()
        final.reset()
        walls.draw(window)
        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)
        if sprite.collide_rect(final, packman):
            win = transform.scale(image.load('thumb_1.jpg'), (700, 500))
            window.blit(win, (0, 0))
            finish = True
        if sprite.spritecollide(packman, monsters, True):
            loose = transform.scale(image.load('loose.jpg'), (700, 500))
            window.blit(loose, (0, 0))
            finish = True
        sprite.groupcollide(bullets, walls, True, False)
        sprite.groupcollide(bullets, monsters, True, True)
    display.update()
    time.delay(3)
