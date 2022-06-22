import numpy as np
import tablero
import functions
import cv2

step = functions.bit
tabla_alto  = len(tablero.tabla)
tabla_ancho = len(tablero.tabla[0])

base = np.array(cv2.imread('Textures/base.png', cv2.IMREAD_UNCHANGED))

texture = []
for n in range(int((len(base)+1)/17)):
    texture.append([])
    for m in range(int((len(base[1])+1)/17)):
        texture[n].append(np.zeros((step, step, 4), np.uint8))
        for w in range(step):
            for z in range(step):                
                texture[n][m][w][z] = base[n*17 + w][m*17 + z]

def addd(y, x, img1, cor):
    if not len(cor) == 0:
        img2 = texture[cor[1]][cor[0]]
        y *= step
        x *= step

        if ((y + step <= len(img1)) and (x + step <= len(img1[0]))):
            for n in range(step):
                for m in range(step):
                    if (img2[n][m] != (255, 255, 255, 0)).all():
                        img1[y + n][x + m] = img2[n][m]


map1 = np.zeros((tabla_alto * step, tabla_ancho * step, 4), np.uint8)
map2 = np.zeros((tabla_alto * step, tabla_ancho * step, 4), np.uint8)


a = ((0, 0), (1, 0), (1, 0), (1, 0), (2, 0))
b = -1
for nn in range(tabla_alto):
    for mm in range(tabla_ancho):
        b += 1
        if 8 > nn:
            addd(nn, mm, map1, (a[b%3]))
        else: 
            addd(nn, mm, map1, ((0, 1)))

addd(7, 0, map1, ((5, 2)))
addd(7, 1, map1, ((5, 2)))
addd(7, 25, map1, ((5, 2)))
addd(7, 26, map1, ((5, 2)))


for nn in range(tabla_alto):
    for mm in range(tabla_ancho):
        addd(nn, mm, map1, tablero.tabla[nn][mm][1])
        addd(nn, mm, map2, tablero.tabla[nn][mm][2])

for pep in tablero.people:
    base = np.array(cv2.imread(f'Textures/{pep[3]}.png', cv2.IMREAD_UNCHANGED))
    for n in range(int((len(base)+1)/(step*2 + 1))):
        for m in range(int((len(base[1])+1)/(step + 1))):

            texx = np.zeros((step*2, step, 4), np.uint8)            
            for w in range(step*2):
                for z in range(step):                
                    texx[w][z] = base[n*(step*2+1) + w][m*(step+1) + z]
            cv2.imwrite(f'Textures/{pep[3]}/{m}-{n}.png', texx)



cv2.imwrite('Maps/down.png', map1)
cv2.imwrite('Maps/up.png', map2)

cv2.waitKey(0)
cv2.destroyAllWindows()

