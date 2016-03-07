import math

def make_translate( x, y, z ):
    m = ident( new_matrix() )
    m[3][0] = x
    m[3][1] = y
    m[3][2] = z
    return m

def make_scale( x, y, z ):
    m = ident( new_matrix() )
    m[0][0] = x
    m[1][1] = y
    m[2][2] = z
    return m
    
def make_rotX( theta ):   
    m = ident( new_matrix() )
    rad = math.radians(theta)
    m[1][1] = math.cos( rad )
    m[1][2] = math.sin( rad )
    m[2][1] = math.sin( rad ) * -1
    m[2][2] = math.cos( rad )
    return m

def make_rotY( theta ):
    m = ident( new_matrix() )
    rad = math.radians(theta)
    m[0][0] = math.cos(rad)
    m[0][2] = math.sin(rad)
    m[2][0] = math.sin(rad) * -1
    m[2][2] = math.cos(rad)
    return m

def make_rotZ( theta ):
    m = ident( new_matrix() )
    rad = math.radians(theta)
    m[0][0] = math.cos(rad)
    m[0][1] = math.sin(rad) 
    m[1][0] = math.sin(rad) * -1
    m[1][1] = math.cos(rad)
    return m

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    #each coordinate is printed top-down
    #for loop goes through "x" -> "1" rows
    for r in range( len(matrix[0]) ):
        row = ""
        #for loop goes through each coordinate
        for c in range( len(matrix) ):
            #add appropriate row value to row string
            row += str(matrix[c][r]) + " "
        print row

def ident( matrix ):
    m = new_matrix(len(matrix), len(matrix))
    for c in range( len(matrix) ):
        for r in range( len(matrix) ):
            if (r == c):
                m[c][r] = 1
            else:
                m[c][r] = 0 
    return m

def scalar_mult( matrix, x ):
    for c in range( len(matrix) ):
        for r in range( len(matrix[c]) ):
            matrix[c][r] *= x
    return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    #m1 columns (c1) = m2 rows (r2) = 4
    #resulting has to have 4 rows
    m = new_matrix( len(m1[0]), len(m2) )
    for c2 in range( len(m2) ):
        for r1 in range( len(m1[0]) ):
            temp = 0
            for r2 in range( len(m2[c2]) ):
                temp += (m2[c2][r2]*m1[r2][r1])
            #print temp
            m[c2][r1] = temp
    m2 = m
    return m

#print "Original Matrix"
#m = new_matrix(6,6)
#print_matrix(m)
#print(" ")
#print "Identity Matrix"
#i = ident(m)
#print_matrix(i)
#print(" ")
#print i[0]
#print i[1]
#print "Scalar Multiplied Matrix"
#scalar_mult(m, 3)
#print_matrix(m)
#print "Translate"
#t = make_translate(1,2,3)
#print_matrix(t)
