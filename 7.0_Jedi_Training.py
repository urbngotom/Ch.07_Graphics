# 7.0 Jedi Training (20pts)  Name: Tommy Ngo
import arcade
'''
1. TEST PICTURE  (10pts)
------------------------
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
Upload your code and a screenshot of your picture.
'''
# screen_width = 500
# screen_length = 400
# arcade.open_window(screen_width, screen_length, "Test Picture")
# arcade.set_background_color(arcade.color.ALMOND)
#
# arcade.start_render()
#
# x = 0
# for i in range(25):
#     arcade.draw_line(x, 0, x, 400, arcade.color.BLACK)
#     x += 20
# y = 0
# for i in range(25):
#     arcade.draw_line(0, y, 500, y, arcade.color.BLACK)
#     y += 20
# arcade.draw_rectangle_filled(50, 370, 60, 20, arcade.color.PHLOX)
# arcade.draw_circle_filled(250, 200, 40, arcade.color.WISTERIA)
# arcade.draw_text("I love you. I know.", 20, 160, arcade.color.BRICK_RED, 20)
# arcade.draw_ellipse_filled(100, 100, 120, 40, arcade.color.AMBER)
# arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE)
# arcade.draw_rectangle_filled(200, 260, 40, 20, arcade.color.BLUSH, -45)
# arcade.draw_arc_filled(400, 320, 120, 120, arcade.color.YELLOW, 120, 420, -90)
#
# arcade.finish_render()
# arcade.run()

'''
2. FLAG CREATION  (10pts)
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
Can you use <20 lines of code?
CHALLENGE: Can you make the entire flag parametrically? This means if I change the hoist to 520px the flag will resize accordingly.
Upload your code and a screenshot of your flag.
'''
# #Could have used functions to reduce the amount of lines for the stars
# hoist= 260
# fly = 1.9*hoist
# arcade.open_window(fly, hoist, "The Stars and Stripes")
# arcade.set_background_color(arcade.color.WHITE)
# arcade.start_render()
#
# #stripes
# y = 0.5*(hoist*(1/13))
# for i in range(7):
#     arcade.draw_rectangle_filled(fly/2, y, fly, hoist*(1/13), (191, 10, 48))
#     y += 2*(hoist*(1/13))
#
# #blue corner
# arcade.draw_lrtb_rectangle_filled(0, (0.76*hoist), hoist, (hoist-(hoist*(7/13))), (0, 40, 104))
#
# #set of 6 stars
# x = fly*0.0308
# y = (hoist*(6/13)+(hoist*0.0135))
# for i in range(5):
#     for i in range(6):
#         arcade.draw_text("*", x, y, arcade.color.WHITE, hoist/13) #260/13=20: used hoist/13 ratio to keep font size parametric
#         x += fly*0.063
#     x = fly*0.0308
#     y += hoist*0.054*2
#
# #set of 5 stars
# x = fly*0.0308*2
# y = (hoist*(6/13)+(hoist*0.0135*5))
# for i in range(4):
#     for i in range(5):
#         arcade.draw_text("*", x, y, arcade.color.WHITE, hoist/13) #260/13=20: used hoist/13 ratio to keep font size parametric
#         x += fly*0.063
#     x = fly*0.0308*2
#     y += hoist*0.054*2
#
# arcade.finish_render()
# arcade.run()


