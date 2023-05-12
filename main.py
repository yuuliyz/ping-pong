from pygame import *
init()
font.init()

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('image.jpg'), (win_width, win_height))

FPS = 60
game = True
update = True

clock = time.Clock()
score1 = 0
score2 = 0

start_x = win_width / 2
start_y = win_height / 2

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_width, sprite_height, sprite_speed):
        super().__init__()
        self.speed_x = sprite_speed
        self.speed_y = sprite_speed
        self.width = sprite_width
        self.height = sprite_height
        self.image = transform.scale(image.load(sprite_image), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys[K_DOWN] and self.rect.y < win_height - self.height:
            self.rect.y += self.speed_y

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys[K_s] and self.rect.y < win_height - self.height:
            self.rect.y += self.speed_y


class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y > win_height - self.height:
            self.speed_y *= -1
            
        if self.rect.y < 0:
            self.speed_y *= -1

    def move(self):
        self.speed_x *= -1


    

platform_1 = Player1('image2.jpg', 0, 0, 30, 100, 10)
platform_2 = Player2('image2.jpg', 670, 0, 30, 100, 10)
ball = Ball('image4.jpg', 350, 250, 50, 50, 3)



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

    if sprite.collide_rect(platform_1, ball) or sprite.collide_rect(platform_2, ball):
        ball.move()
    if ball.rect.x < 0:
        score2 += 1
        ball.rect.x = start_x
        ball.rect.y = start_y

    if score1 > 5:
        update = False
        window.blit(font.SysFont("Arial", 60).render('Игрок 1 победил', True, (255, 255, 255)))
    if score2 > 5:
        update = False
        window.blit(font.SysFont('Arial', 60).render('Игрок 2 победил', True, (255, 255, 255)))
    
        
        
        
    display.update()
    clock.tick(FPS)
