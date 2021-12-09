from random import randint
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
APPLE_IMG = 'H:\Project\PYTHON\Assighnment10\Red-Apple.png'
POOP_IMG = 'H:\Project\PYTHON\Assighnment10\poop_img.png'


class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 10
        self.height = 10
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2
        self.color = arcade.color.BLUE_GREEN
        self.speed = 5
        self.length = []
        self.direction = 'up'

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, 5, self.color)

    def move(self):
        for i in range(len(self.length) - 1, 0, -1):
            self.length[i].center_x = self.length[i - 1].center_x
            self.length[i].center_y = self.length[i - 1].center_y
        if self.direction == 'up':
            self.center_y += self.speed
        elif self.direction == 'right':
            self.center_x += self.speed
        elif self.direction == 'down':
            self.center_y -= self.speed
        elif self.direction == 'left':
            self.center_x -= self.speed

###🍎🍎🍎
class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = randint(10, SCREEN_WIDTH - 10)
        self.center_y = randint(10, SCREEN_HEIGHT - 10)
        self.texture = arcade.load_texture(APPLE_IMG)
        self.scale = 0.05

    def draw(self):
        arcade.draw_texture_rectangle(self.center_x, self.center_y, 40, 40, self.texture)

### 💩
class Poop(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = randint(10, SCREEN_WIDTH - 10)
        self.center_y = randint(10, SCREEN_HEIGHT - 10)
        self.texture = arcade.load_texture(POOP_IMG)
        self.scale = 0.05
    def draw(self):
        arcade.draw_texture_rectangle(self.center_x, self.center_y, 38, 38, self.texture)


class Game(arcade.Window):
    def __init__(self):
        super().__init__(title='Snake Game')
        arcade.set_background_color(arcade.color.BLUE_BELL)
        self.snake = Snake()
        self.apple = Apple()
        self.poop = Poop()
        self.running = True
        self.score = 1
        self.snake.color = arcade.color.SAND
        self.snake.length.append(self.snake)
        self.on_length_update()

    def on_draw(self):
        arcade.start_render()
        for i in self.snake.length:
            i.draw()
        self.apple.draw()
        self.poop.draw()
        arcade.draw_text('Score: ' + str(self.score), 5, SCREEN_HEIGHT - 25, arcade.color.BLUE, 15)
        if not self.running:
            arcade.draw_text('Game Over', SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT / 2, arcade.color.RED, 30)

    def on_update(self, delta_time):
        if self.snake.center_x >= SCREEN_WIDTH or self.snake.center_x <= 0 or self.snake.center_y >= SCREEN_HEIGHT \
                or self.snake.center_y <= 0 or self.score == 0:
            self.running = False
        for i in range(10, len(self.snake.length) - 1):
            if arcade.check_for_collision(self.snake, self.snake.length[i]):
                self.running = False
        if not self.running:
            return
        if arcade.check_for_collision(self.snake, self.apple):
            self.score += 1
            self.apple.center_x = randint(10, SCREEN_WIDTH - 10)
            self.apple.center_y = randint(10, SCREEN_HEIGHT - 10)
            self.on_length_update()
        if arcade.check_for_collision(self.snake, self.poop):
            self.score -= 1
            self.poop.center_x = randint(10, SCREEN_WIDTH - 10)
            self.poop.center_y = randint(10, SCREEN_HEIGHT - 10)
        self.snake.move()
    
    def on_length_update(self):
        for i in range(0, 10):
            growing_snake = Snake()
            growing_snake.center_x = self.snake.length[-1].center_x
            growing_snake.center_y = self.snake.length[-1].center_y
            self.snake.length.append(growing_snake)
            self.on_draw()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.DOWN and self.snake.direction != 'up':
            self.snake.direction = 'down'
        elif key == arcade.key.LEFT and self.snake.direction != 'right':
            self.snake.direction = 'left'
        elif key == arcade.key.UP and self.snake.direction != 'down':
            self.snake.direction = 'up'
        elif key == arcade.key.RIGHT and self.snake.direction != 'left':
            self.snake.direction = 'right'




my_game = Game()
arcade.run()