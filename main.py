from pygame import *
init()

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
    pass

class Ball(GameSprite):
    pass
