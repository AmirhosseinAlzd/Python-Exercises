import arcade
MARGIN = 120
DISTANCE = 18

arcade.open_window(400, 400, 'Red_Blue_Screen')
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()   #logical to show
for row in range(10):
    for column in range(10):
        x = column * DISTANCE + MARGIN
        y = row * DISTANCE + MARGIN
        if (row+column) % 2 != 0:
            arcade.draw_rectangle_filled(x, y, 10, 20, arcade.color.BLUE, 45)
        else:
            arcade.draw_rectangle_filled(x, y, 10, 10, arcade.color.RED, 45)
arcade.finish_render()
arcade.run()