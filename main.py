from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
m = new_matrix()

for x in range(10000):
    y = 100000 - x**2
    y = math.sqrt(abs(y))
    add_point(m, x, y)

draw_lines(m, screen, color)

for i in range(1000):
    sc = make_translate(0, i, 0)
    temp = matrix_mult(sc,m)
    color[GREEN] = 0
    color[RED] = 255 -(i%255)
    color[BLUE] = i%255
    draw_lines(temp, screen, color)

display(screen)
