import arcade

screen_width = 600
screen_length = 600
arcade.open_window(screen_width, screen_length, "212418")
arcade.set_background_color(arcade.color.AMAZON)

arcade.start_render()

#grid
x= 0
for i in range(3):
    arcade.draw_line(x, 0, x, 600, arcade.color.BLACK)
    x += 200
y = 0
for i in range(3):
    arcade.draw_line(0, y, 600, y, arcade.color.BLACK)
    y += 200

#first box - orange square
arcade.draw_rectangle_filled(100, 500, 60, 60, arcade.color.NEON_CARROT)
arcade.draw_rectangle_outline(100, 500, 60, 60, arcade.color.BLACK, 2)

#second box - turquoise circle
arcade.draw_circle_filled(300, 500, 50, arcade.color.BRIGHT_TURQUOISE)

#third box - pacman
arcade.draw_arc_filled(500, 500, 50, 50, arcade.color.YELLOW, 120, 420, 90)

#fourth box - tilted square
point_list = ((100, 200),
              (0, 300),
              (100, 400),
              (200, 300))
arcade.draw_polygon_filled(point_list,arcade.color.BARBIE_PINK)

#fifth box - diagonal lines
for i in range(200, 400, 20):
    arcade.draw_line(200, i, i, 200, arcade.color.BLACK)
for i in range(400, 180, -20):
    arcade.draw_line(400, i, i, 400, arcade.color.BLACK)


#sixth box - Flag
y_offset = 210
for i in range(5):
    arcade.draw_rectangle_filled(500, y_offset, 200, 20, arcade.color.WHITE)
    y_offset += 40
y_offset = 230
for i in range(5):
    arcade.draw_rectangle_filled(500, y_offset, 200, 20, arcade.color.RED)
    y_offset += 40
arcade.draw_rectangle_filled(450, 350, 100, 100, arcade.color.NAVY_BLUE)

#seventh box - repeating circles
x_offset = 20
for i in range(5):
    arcade.draw_circle_filled(x_offset, 100, 20, arcade.color.BLUEBERRY)
    x_offset += 40

#eighth box - dots
x_offset = 210
y_offset = 190
for i in range(19):
    for i in range(19):
        arcade.draw_point(x_offset, y_offset, arcade.color.NEON_GREEN, 2)
        x_offset += 10
    x_offset = 210
    y_offset -= 10

#ninth box - name
arcade.draw_text("Tommy Ngo", 460, 100, arcade.color.BLACK, 12)

arcade.finish_render()
arcade.run()