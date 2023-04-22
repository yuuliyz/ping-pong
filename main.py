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
    pass

while game:
    for e in event.get():
        if e.type == QUIT:
            game == False
    
    
    if update:
        window.blit(background, (0, 0))
        
        
        
display.update()
clock.tick(FPS)
        
