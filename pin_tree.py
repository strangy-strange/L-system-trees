import cv2
import numpy as np
from math import pi, sin, cos
from time import sleep
from random import randint
def line_build(dot, ang, leng):
    ang += 90
    return (int(dot [ 0 ]  +  sin( ang * pi/180 ) * leng), int(dot [ 1 ]  +cos( ang* pi/180 ) * leng) )

cnv = np.ones((1080, 1920, 3), dtype=np.uint8()) * 255

axi = 'A'
omni = axi
leng = 300
color = (0, 0, 0)
ang = 90 #+ randint(-18, 18)
start_tik = 16
start_dot = (960,1080)
last_dot =(960,1080 )

#cv2.line(cnv,(960,1080 ), last_dot , (0, 0, 0), start_tik)
dotty = [[start_dot  , ang]]
rules = {'A': 'AB', 'B':'A'}
while True:
    cnv = np.ones((1080, 1920, 3), dtype=np.uint8()) * randint(100,150)
    
    axi = 'A'
    omni = axi
    leng = 300
    color = (0, 0, 0)
    ang = 90 + randint(-18, 18)
    start_tik = 16
    start_dot = (960,1080)
    last_dot =(960,1080 )

    mas = [
                (2, 8 ,16),
                (8, 2, 16),
                (2, 16, 8),
                (16, 2, 8),
                (randint(2, 16), randint(2, 16), randint(2, 16)),
                (randint(2, 16), randint(2, 16), randint(2, 16)),
                (randint(2, 16), randint(2, 16), randint(2, 16)),
                (randint(2, 16), randint(2, 16), randint(2, 16)),
                (randint(2, 16), randint(2, 16), randint(2, 16)),
                (randint(2, 16), randint(2, 16), randint(2, 16)),
                (randint(2, 16), randint(2, 16), randint(2, 16))
        ]
    mask_color = mas[randint(0,len(mas)-1)] 
    #cv2.line(cnv,(960,1080 ), last_dot , (0, 0, 0), start_tik)
    dotty = [[start_dot  , ang]]
    rules = {'A': 'AB', 'B':'A'}
    for i in range ( 16):
        omni = axi
        axi = ''
        dotty_dotty = dotty
        for j in range( len( omni ) ):
            if omni [ j ] =='A':
                color = (mask_color[0] * i, mask_color[1]*i, mask_color[2]*i)
                axi = axi + rules['A']
            
                otkl = randint(15, 45)
                start_dot = dotty_dotty[j][0]   
                ang = dotty_dotty[j][1]  
                cv2.line(cnv, start_dot,  line_build( start_dot, ang + otkl, int( 500 / (1+i) ) ) , color, start_tik-i)

                dotty = dotty + [[line_build( start_dot, ang + otkl, int(500/(1+i)) ) , ang + otkl ]]
                
            if omni [ j ] == 'B':
                color = (mask_color [0]* i, mask_color[1]*i, mask_color[2]*i)
                axi = axi + rules['B']

                otkl = randint(-45, -15)
                start_dot = dotty_dotty[j][0]   
                ang = dotty_dotty[j][1]
                cv2.line(cnv, start_dot,  line_build( start_dot, ang + otkl, int( 500 / (1+i) ) ) , color, start_tik-i)

                dotty = dotty + [[line_build( start_dot, ang + otkl, int(500/(1+i)) ) , ang + otkl ]]
                
        cv2.imshow('tree', cnv)
        sleep(0.01 + 0.01 * i/2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        
    
    
    
