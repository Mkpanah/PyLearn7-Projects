import random
import arcade


class Spaceship(arcade.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = random.randint(0, game.width)
        self.center_y = 80
        self.width = 48
        self.height = 48
        self.speed = 8


class Enemy(arcade.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0, game.width)
        self.center_y = 300
        self.angle = 180
        self.width = 48
        self.height = 48
        self.speed = 2


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=500, title="Interstellar Game 2023")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Spaceship(self)
        self.enemy = Enemy(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()
        self.enemy.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 97:
            self.me.center_x = self.me.center_x - self.me.speed
        elif symbol == 100:
            self.me.center_x = self.me.center_x + self.me.speed

    def on_update(self, delta_time: float):
        self.enemy.center_y -= self.enemy.speed


window = Game()
# me = Spaceship()
arcade.run()
