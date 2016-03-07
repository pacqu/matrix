from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    lines = len(matrix) / 2
    for i in range( lines ):
        x0 = matrix[i * 2][0]
        y0 = matrix[i * 2][1]
        x1 = matrix[(i * 2) + 1][0]
        y1 = matrix[(i * 2) + 1][1]
        draw_line( screen, x0, y0, x1, y1, color )

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    point = []
    point.append(x)
    point.append(y)
    point.append(z)
    point.append(1)
    matrix.append(point)


def draw_line( screen, x0, y0, x1, y1, color ):
    dx = x1 - x0
    dy = y1 - y0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
    
    if dx == 0:
        y = y0
        while y <= y1:
            plot(screen, color,  x0, y)
            y = y + 1
    elif dy == 0:
        x = x0
        while x <= x1:
            plot(screen, color, x, y0)
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx

#print(" ")
#m = new_matrix(4,1)
#print_matrix(m)
#add_point(m, 2,2)
#add_point(m, 4,4,4)
#print "matrix with points"
#print_matrix(m)
print "m1"
#m1 = new_matrix(4,4)
#print_matrix(m1)
#print "m2"
#m2 = new_matrix(4,2)
#m2[0] = [1,2,5,2]
#m2[1] = [4,3,4,5]
#print_matrix(m2)
#print "matrix mult"
#m3 = matrix_mult(m1,m2)
#print_matrix(m3)
