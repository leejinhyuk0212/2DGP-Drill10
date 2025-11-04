from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (1.0/0.03)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0/ TIME_PER_ACTION
FRAME_PER_ACTION = 5
FRAME_PER_SECOND = FRAME_PER_ACTION * ACTION_PER_TIME

class Bird:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 0):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.velocity = velocity
        self.frame = 0.0

    def draw(self):
        self.image.clip_draw(int(self.frame) * 184, 340, 184, 169, self.x, self.y)

    def update(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x += (self.velocity * game_framework.frame_time * PIXEL_PER_METER)

        if self.x < 0 or self.x >600:
            pass


