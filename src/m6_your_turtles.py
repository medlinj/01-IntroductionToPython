"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and JD Medlin.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg
window = rg.TurtleWindow()

thing1 = rg.SimpleTurtle('turtle')
thing1.pen = rg.Pen('yellow',5)
thing1.speed = 10

radius = 75

for k in range(10):
    thing1.draw_circle(radius)

    thing1.pen_up()
    thing1.right(90)
    thing1.forward(20)
    thing1.left(45)

    thing1.pen_down()

    radius = radius - 5

thing2 = rg.SimpleTurtle('turtle')
thing2.pen = rg.Pen('brown',5)
thing2.speed = 5

size = 20

thing2.backward(35)

for k in range(6):
    thing2.draw_square(size)

    thing2.pen_up()
    thing2.right(45)
    thing2.forward(10)
    thing2.left(90)

    thing2.pen_down()

    size = size - 3


print('Flower Power!!!')

window.close_on_mouse_click()