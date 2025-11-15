from pygame import *
from random import randint
# інші імпорти


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

WHITE = (255, 255, 255)

init()
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Snake_game")

#картинки
snake_body_left = image.load("images/snake/snake_body_left.png")
snake_body_up = image.load("images/snake/snake_body_up.png")
snake_head_left = image.load("images/snake/snake_head_left.png")
snake_head_right = image.load("images/snake/snake_head_right.png")
snake_head_up = image.load("images/snake/snake_head_up.png")
snake_head_down = image.load("images/snake/snake_head_down.png")
snake_tail_left = image.load("images/snake/snake_tail_left.png")
snake_tail_right = image.load("images/snake/snake_tail_right.png")
snake_tail_up = image.load("images/snake/snake_tail_up.png")
snake_tail_down = image.load("images/snake/snake_tail_down.png")
appel = image.load("images/appel.png")
background = image.load("images/background.jpg")

#звуки
mixer.music.load("music/music_game.wav")
mixer.music.set_volume(0.5)
mixer.music.play(-1)

lvl_up = mixer.Sound("music/lvl_up.aif")
lvl_up.set_volume(0.7)

game_over = mixer.Sound("music/game_over.flac")
game_over.set_volume(2)


# ігрові класи
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,
                 size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        screen.blit(self.image,(self.rect.x, self.rect.y))




class SnakePart(GameSprite):
    def __init__(self, player_x, player_y,
                 size_x, size_y):
        super().__init__(snake_body_left, player_x, player_y,
                 size_x, size_y)










running = True
while running:
   screen.fill(WHITE)


   for e in event.get():
       if e.type == QUIT:
           running = False




   display.flip()
