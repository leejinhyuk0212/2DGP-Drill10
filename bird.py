from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (1.0/0.03)

class Bird:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 10):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.velocity = velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):

        self.x += (self.velocity * game_framework.frame_time * PIXEL_PER_METER)

        if self.x < 0 or self.x >600:
            pass


