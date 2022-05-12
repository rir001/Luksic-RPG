import cv2
import numpy as np
import tablero
import os

os.system('cls' if os.name == 'nt' else 'clear')
print('cargando mapa...')

step = 64

def addd(y, x, img1, img2):
    y *= step
    x *= step
    alto = len(img2)
    ancho = len(img2[0])
    if ((y + alto <= len(img1)) and (x + ancho <= len(img1[0]))):
        for n in range(alto):
            for m in range(ancho):
                if not np.equal(img2[n][m], [0, 255, 0]).all():
                    img1[y + n][x + m] = img2[n][m]


tabla_alto = len(tablero.tabla)
tabla_ancho = len(tablero.tabla[0])

mapp = np.zeros((tabla_alto * step, tabla_ancho * step, 3), np.uint8)

for nn in range(tabla_alto):
    for mm in range(tabla_ancho):
        addd(nn, mm, mapp, np.array(cv2.imread('sprites/madera.png')))

for nn in range(tabla_alto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('cargando mapa...')
    print(f'{nn+1}/{tabla_alto}\t')
    for mm in range(tabla_ancho):
        addd(nn, mm, mapp, np.array(cv2.imread(f'sprites/{tablero.tabla[nn][mm][1]}')))
        

cv2.imwrite('map.png', mapp)

cv2.waitKey(0)
cv2.destroyAllWindows()