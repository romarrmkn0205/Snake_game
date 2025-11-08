from pygame import *
# інші імпорти


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500


WHITE = (255, 255, 255)


init()
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("НАЗВА ГРИ")


running = True
while running:
   screen.fill(WHITE)


   for e in event.get():
       if e.type == QUIT:
           running = False




   display.flip()