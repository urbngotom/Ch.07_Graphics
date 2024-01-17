'''
PYCASSO PROJECT (4pts)
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Upload both your code and a screenshot of your art.
'''
#night cityscape
import arcade
arcade.open_window(600, 500, "Tommy Ngo")
arcade.set_background_color((88, 62, 189))
arcade.start_render()

foreground_color = (55, 55, 55)
background_color1 = (40, 40, 40)
background_color2 = (45, 45, 45)

#stars
x_stars = 30
y_stars = 450
for i in range(6):
    for i in range(10):
        arcade.draw_text("*", x_stars, y_stars, arcade.color.WHITE, 20)
        x_stars += 100
    x_stars = 30
    y_stars -= 100

x_stars = 80
y_stars = 400
for i in range(5):
    for i in range(9):
        arcade.draw_text("*", x_stars, y_stars, arcade.color.WHITE, 20)
        x_stars += 100
    x_stars = 80
    y_stars -= 100

#rectangular building background 1
bg1_offset = 90
for i in range(3):
    arcade.draw_rectangle_filled(bg1_offset, 50, 90, 300, background_color1)
    bg1_offset += 180

#rectangular building background 1 windows
xwindow_offset = 200
for i in range(2):
    if i == 0:
        xwindow_offset = 450
        ywindow_offset = 160
        for i in range(3):
            arcade.draw_rectangle_filled(xwindow_offset, ywindow_offset, 30, 50, (178, 175, 143))
            arcade.draw_line(xwindow_offset-15, ywindow_offset, xwindow_offset+15, ywindow_offset, arcade.color.BLACK)
            arcade.draw_line(xwindow_offset, ywindow_offset-25, xwindow_offset, ywindow_offset+25, arcade.color.BLACK)
            ywindow_offset -= 80
    else:
        xwindow_offset = 260
        ywindow_offset = 160
        for i in range(3):
            arcade.draw_rectangle_filled(xwindow_offset, ywindow_offset, 30, 50, (178, 175, 143))
            arcade.draw_line(xwindow_offset-15, ywindow_offset, xwindow_offset+15, ywindow_offset, arcade.color.BLACK)
            arcade.draw_line(xwindow_offset, ywindow_offset-25, xwindow_offset, ywindow_offset+25, arcade.color.BLACK)
            ywindow_offset -= 80

#rectangular building background 2
bg2_offset = 120
for i in range(2):
    arcade.draw_rectangle_filled(bg2_offset, 30, 90, 300, background_color2)
    bg2_offset += 100

#rectangular building background 2 windows
bg2_xwindow_offset = 200
for i in range(2):
    if i == 0:
        bg2_xwindow_offset = 110
        bg2_ywindow_offset = 120
        for i in range(3):
            arcade.draw_rectangle_filled(bg2_xwindow_offset, bg2_ywindow_offset, 30, 50, (214, 211, 172))
            arcade.draw_line(bg2_xwindow_offset-15, bg2_ywindow_offset, bg2_xwindow_offset+15, bg2_ywindow_offset, arcade.color.BLACK)
            arcade.draw_line(bg2_xwindow_offset, bg2_ywindow_offset-25, bg2_xwindow_offset, bg2_ywindow_offset+25, arcade.color.BLACK)
            bg2_ywindow_offset -= 80
    else:
        bg2_xwindow_offset = 210
        bg2_ywindow_offset = 120
        for i in range(3):
            arcade.draw_rectangle_filled(bg2_xwindow_offset, bg2_ywindow_offset, 30, 50, (214, 211, 172))
            arcade.draw_line(bg2_xwindow_offset-15, bg2_ywindow_offset, bg2_xwindow_offset+15, bg2_ywindow_offset, arcade.color.BLACK)
            arcade.draw_line(bg2_xwindow_offset, bg2_ywindow_offset-25, bg2_xwindow_offset, bg2_ywindow_offset+25, arcade.color.BLACK)
            bg2_ywindow_offset -= 80

#rectangular building foreground
arcade.draw_rectangle_filled(40, 100, 90, 300, foreground_color)

#rectangular building foreground windows
xwindow_offset = 20
for i in range(2):
    ywindow_offset = 200
    for i in range(3):
        arcade.draw_rectangle_filled(xwindow_offset, ywindow_offset, 30, 50, (230, 231, 161))
        arcade.draw_line(xwindow_offset-15, ywindow_offset, xwindow_offset+15, ywindow_offset, arcade.color.BLACK)
        arcade.draw_line(xwindow_offset, ywindow_offset-25, xwindow_offset, ywindow_offset+25, arcade.color.BLACK)
        ywindow_offset -= 80
    xwindow_offset += 40


#red light building background 2
arcade.draw_rectangle_filled(400, 5, 70, 400, background_color2)
arcade.draw_rectangle_filled(400, 200, 50, 80, background_color2)
arcade.draw_line(400, 200, 400, 300, background_color2)
arcade.draw_point(400, 300, arcade.color.RED, 2)

#red light building window background 2
red_bgwindow_xoffset = 400
red_bgwindow_yoffset = 180
for i in range(3):
    arcade.draw_rectangle_filled(400, red_bgwindow_yoffset, 30, 50, (214, 211, 172)) #194, 195, 167 - old color
    arcade.draw_line(red_bgwindow_xoffset-15, red_bgwindow_yoffset, red_bgwindow_xoffset+15, red_bgwindow_yoffset, arcade.color.BLACK)
    arcade.draw_line(red_bgwindow_xoffset, red_bgwindow_yoffset-25, red_bgwindow_xoffset, red_bgwindow_yoffset+25, arcade.color.BLACK)
    red_bgwindow_yoffset -= 80

#red light building foreground
arcade.draw_rectangle_filled(150, 100, 70, 400, foreground_color)
arcade.draw_rectangle_filled(150, 300, 50, 80, foreground_color)
arcade.draw_line(150, 200, 150, 400, foreground_color)
arcade.draw_point(150, 400, arcade.color.RED, 2)


#red light building foreground windows
red_xwindow_offset = 150
red_ywindow_offset = 280
for i in range(4):
    arcade.draw_rectangle_filled(150, red_ywindow_offset, 30, 50, (230, 231, 161))
    arcade.draw_line(red_xwindow_offset-15, red_ywindow_offset, red_xwindow_offset+15, red_ywindow_offset, arcade.color.BLACK)
    arcade.draw_line(red_xwindow_offset, red_ywindow_offset-25, red_xwindow_offset, red_ywindow_offset+25, arcade.color.BLACK)
    red_ywindow_offset -= 80


#half cut building
point_list1 = ((300, 0),
              (300, 280),
              (370, 210),
              (370, 0))
arcade.draw_polygon_filled(point_list1, foreground_color)

#half cut building windows
half_xwindow_offset = 335
half_ywindow_offset = 180
for i in range(3):
    arcade.draw_rectangle_filled(335, half_ywindow_offset, 30, 50, (230, 231, 161))
    arcade.draw_line(half_xwindow_offset-15, half_ywindow_offset, half_xwindow_offset+15, half_ywindow_offset, arcade.color.BLACK)
    arcade.draw_line(half_xwindow_offset, half_ywindow_offset-25, half_xwindow_offset, half_ywindow_offset+25, arcade.color.BLACK)
    half_ywindow_offset -= 80

#penthouse
point_list = ((490, 0),
               (490, 200),
               (540, 200),
               (540, 300),
               (570, 350),
               (600, 300),
               (600, 0))
arcade.draw_polygon_filled(point_list, foreground_color)
balcony_x = 491
for i in range(5):
    arcade.draw_line(balcony_x, 200, balcony_x, 220, foreground_color)
    balcony_x += 10
arcade.draw_line(490, 220, 570, 220, foreground_color)

#penthouse windows
arcade.draw_rectangle_filled(570, 250, 30, 50, (230, 231, 161))
arcade.draw_line(555, 250, 585, 250, arcade.color.BLACK)
arcade.draw_line(570, 225, 570, 275, arcade.color.BLACK)

pent_xwindow_offset = 515
for i in range(2):
    pent_ywindow_offset = 130
    for i in range(2):
        arcade.draw_rectangle_filled(pent_xwindow_offset, pent_ywindow_offset, 30, 50, (230, 231, 161))
        arcade.draw_line(pent_xwindow_offset-15, pent_ywindow_offset, pent_xwindow_offset+15, pent_ywindow_offset, arcade.color.BLACK)
        arcade.draw_line(pent_xwindow_offset, pent_ywindow_offset-25, pent_xwindow_offset, pent_ywindow_offset+25, arcade.color.BLACK)
        pent_ywindow_offset -= 80
    pent_xwindow_offset += 55

arcade.finish_render()
arcade.run()

