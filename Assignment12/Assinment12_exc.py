import math
import arcade
from random import randint
from time import time


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Spaceship(arcade.Sprite):
    def __init__(self ):
        super().__init__(':resources:images/space_shooter/playerShip2_orange.png')
        self.width = 48
        self.height = 48
        self.score = 0
        self.center_x = SCREEN_WIDTH//2
        self.center_y = 48
        self.angle = 0
        self.change_angle = 0
        self.bullet_list = []
        self.speed = 4
        self.health = 3

    def fire(self):
        self.bullet_list.append(Bullet(self))
    
    def rotate(self):
        self.angle += self.change_angle * self.speed


class Enemy(arcade.Sprite):
    def __init__(self,speed_limit = 4):
        super().__init__(':resources:images/space_shooter/playerShip1_blue.png')
        self.width = 48
        self.height = 48
        self.center_x = randint(0, SCREEN_WIDTH)
        self.center_y = SCREEN_HEIGHT + SCREEN_HEIGHT//2  #24
        self.angle = 180
        self.speed = speed_limit
        

    def hit_sound(self):
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/hit1.wav'))

    def move(self):
        self.center_y -= self.speed


class Bullet(arcade.Sprite):
    def __init__(self,host):
        super().__init__(':resources:images/space_shooter/laserRed01.png')
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.speed = 6
        self.angle = host.angle
        
    def move(self):
        angle = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(angle)
        self.center_y += self.speed * math.cos(angle)

    def laser_sound(self):
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/laser4.wav'), 0.2)


class Game(arcade.Window):
    def __init__(self):
        self.w = 800
        self.h = 600
        super().__init__(self.w, self.h, title='Interstellar GAME !')
        self.background_image = arcade.load_texture(':resources:images/backgrounds/stars.png')
        self.health_image = arcade.load_texture(':resources:images/topdown_tanks/treeBrown_small.png')
        self.me = Spaceship()
        self.enemy = Enemy()
        self.enemy_list = []
        self.next_enemy_time = randint(2, 5)
        self.game_start_time = time()
        self.start_time = time()
        

    def on_draw(self):
        arcade.start_render()
        if self.me.health > 0:
            arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.background_image)
            self.me.draw()
            for i in range(len(self.me.bullet_list)):
                self.me.bullet_list[i].draw()
            for i in range(len(self.enemy_list)):
                self.enemy_list[i].draw()
            for i in range(self.me.health):
                arcade.draw_lrwh_rectangle_textured(10+i*35, 10, 30, 30, self.health_image)
            arcade.draw_text('Score: ' + str(self.me.score), SCREEN_WIDTH-130, 10, arcade.color.WHITE, 20, width=200)
        else:
            arcade.draw_text('Game Over', SCREEN_WIDTH//2-200, SCREEN_HEIGHT//2, arcade.color.WHITE, 20, width=400, align='center')

            
    def on_update(self, delta_time):
        self.end_time = time()
        if self.end_time - self.start_time > self.next_enemy_time:
            self.next_enemy_time = randint(4, 6)
            self.enemy_list.append(Enemy(int(3+(self.end_time-self.game_start_time)//24)))
            self.start_time = time()
        self.me.rotate()
        for i in range(len(self.me.bullet_list)):
            self.me.bullet_list[i].move()
        for i in range(len(self.enemy_list)):
            self.enemy_list[i].move()
        for enemy in self.enemy_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(bullet, enemy):
                    enemy.hit_sound()
                    self.me.bullet_list.remove(bullet)
                    self.enemy_list.remove(enemy)
                    self.me.score += 1
        for enemy in self.enemy_list:
            if enemy.center_y < 0:
                self.me.health -= 1
                self.enemy_list.remove(enemy)
        for bullet in self.me.bullet_list:
            if bullet.center_y > self.height or bullet.center_x < 0 or bullet.center_x > self.width:
                self.me.bullet_list.remove(bullet)

    def on_key_press(self,  symbol, modifiers):
        if  symbol == arcade.key.SPACE:
            self.me.fire()
            self.me.bullet_list[-1].laser_sound()
        elif symbol == arcade.key.LEFT :
            self.me.change_angle = 1
        elif symbol == arcade.key.RIGHT:
            self.me.change_angle = -1

    def on_key_release(self, key, modifiers):
        self.me.change_angle = 0


game = Game()
arcade.run()
