from pygame import *
init()

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('image.png'), (win_width, win_height))

FPS = 60
game = True
update = True

score1 = 0
score2 = 0

start_x = 350
start_y = 250

class GameSprite(sprite.Sprite):
    def init(self, sprite_image, sprite_x, sprite_y, sprite_width, sprite_height, sprite_speed):
        super().__init__()
        self.speed = sprite_speed
        self.width = sprite_width
        self.height = sprite_height
        self.image = transform.scale(image.load(sprite_image), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
    def reset(self):
        scene.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win.height - self.height:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed
        if self.rect.x < 0:
            score2 += 1
            self.rect.x = start_x
            self.rect.y = start_y
            
        if self.rect.x > win_width - self.width:
            score1 += 1
            self.rect.x = start_x
            self.rect.y = start_y

    def move(self):
        self.speed * -1

    

platform_1 = Player('image2.png', 0, 0, 30, 100, 10)
platform_2 = Player('image3.png', 670, 0, 30, 100, 10)
ball = Ball('image4.png', start_x, start_y, 50, 50, 3)



while game:
    for e in event.get():
        if e.type == QUIT:
            game == False
    
    
    if update:
        window.blit(background, (0, 0))
        platform_1.update()
        platform_1.reset()
        platform_2.update()
        platform_2.reset()
        ball.update()
        ball.reset()
        window.blit(font.Font(None, 40).render('Oчки:'+str(lost), True, (255, 255, 255)), (10, 10))
        window.blit(font.Font(None, 40).render('Очки:'+str(lost), True, (255, 255, 255)), (650, 10))

    if sprite.collide_rect(platform_1, ball) or sprite.collide_rect(platform_2, ball):
        ball.move()

    if score1 > 5:
        update = False
        window.blit(font.Font(None, 60).render('Игрок 1 победил', True, (255, 255, 255)), (win_width//2-150, win_height//2))
    if score2 > 5:
        update = False
        window.blit(font.Font(None, 60).render('Игрок 2 победил', True, (255, 255, 255)), (win_width//2-150, win_height//2))
    
        
        
        
display.update()
clock.tick(FPS)
        
