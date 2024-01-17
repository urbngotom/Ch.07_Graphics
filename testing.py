import arcade
arcade.open_window(600, 600, "Snowman")

arcade.start_render()

arcade.draw_rectangle_outline(300, 300, 100, 200, arcade.color.WHITE, 5)
# radius=50; y=50
#
# for i in range(10):
#
#      arcade.draw_circle_filled(100, y, radius, arcade.color.WHITE)
#
#      y = y+1.8*radius
#
#      radius = radius*0.8
# arcade.finish_render()
arcade.run()