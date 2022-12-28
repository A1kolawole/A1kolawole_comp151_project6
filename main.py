import arcade
import random
import math

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ENEMY_SPEED = 3
SHOT_SPEED = 8
MAX_SHOTS = 5
TARGET_SCORE = 20
LIVE_COUNT = 3

# Assets
player_texture = "assets/player.png"
enemy_texture = "assets/enemy.png"
shot_texture = "assets/shot.png"
player_hit_sound = "assets/player_hit.wav"
player_shoot_sound = "assets/player_shoot.wav"
enemy_hit_sound = "assets/enemy_hit.wav"
win_sound = "assets/win.wav"
lose_sound = "assets/lose.wav"

class Player:
    def __init__(self):
        self.texture = arcade.load_texture(player_texture)
        self.x = SCREEN_WIDTH / 2
        self.y = 50
        self.speed = 5
        self.shots = []

    def draw(self):
        arcade.draw_texture_rectangle(self.x, self.y, self.texture.width, self.texture.height, self.texture, 0)
        for shot in self.shots:
            shot.draw()

    def update(self):
        for shot in self.shots:
            shot.update()

    def move_left(self):
        self.x -= self.speed
        if self.x < self.texture.width / 2:
            self.x = self.texture.width / 2

    def move_right(self):
        self.x += self.speed
        if self.x > SCREEN_WIDTH - self.texture.width / 2:
            self.x = SCREEN_WIDTH - self.texture.width / 2

    def shoot(self):
        if len(self.shots) < MAX_SHOTS:
            arcade.play_sound(player_shoot_sound)
            self.shots.append(Shot(self.x, self.y + self.texture.height / 2))

class Enemy:
    def __init__(self):
        self.texture = arcade.load_texture(enemy_texture)
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = SCREEN_HEIGHT
        self.speed = ENEMY_SPEED

    def draw(self):
        arcade.draw_texture_rectangle(self.x, self.y, self.texture.width, self.texture.height, self.texture, 0)

    def update(self):
        self.y -= self.speed
        if self.y < 0:
            self.remove_from_sprite_lists()

class Shot:
    def __init__(self, x, y):
        self.texture = arcade.load_texture(shot_texture)
        self.x = x
        self.y = y
        self.speed = SHOT_SPEED

    def draw(self):
        arcade.draw_texture_rectangle(self.x, self.y)

