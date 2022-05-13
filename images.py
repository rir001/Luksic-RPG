import numpy as np
import tablero
import cv2
import os

step = 64

tabla_alto = len(tablero.tabla)
tabla_ancho = len(tablero.tabla[0])

def addd(capa, y, x, img1, img2):
    y *= step
    x *= step
    alto = len(img2)
    ancho = len(img2[0])
    if ((y + alto <= len(img1)) and (x + ancho <= len(img1[0]))):
        if capa == 0:
            for n in range(alto):
                for m in range(ancho):
                    img1[y + n][x + m] = img2[n][m]
                    
        elif capa == 1:
            for n in range(alto):
                for m in range(ancho):
                    down = (img1[y + n][x + m]) * (1-(img2[n][m][3]/255))
                    up =   (img2[n][m]) * (img2[n][m][3]/255)
                    img1[y + n][x + m] = (down + up)
        
def init():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('cargando mapa...')

    map1 = np.zeros((tabla_alto * step, tabla_ancho * step, 4), np.uint8)
    map2 = np.zeros((tabla_alto * step, tabla_ancho * step, 4), np.uint8)

    for nn in range(tabla_alto):
        for mm in range(tabla_ancho):
            addd(0, nn, mm, map1, np.array(cv2.imread('sprites/madera.png', cv2.IMREAD_UNCHANGED)))

    for nn in range(tabla_alto):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('cargando mapa...')

        print(f'{nn+1}/{tabla_alto} -- 1')
        print(f'0/{tabla_alto} -- 2')

        for mm in range(tabla_ancho):
            addd(1, nn, mm, map1, np.array(cv2.imread(f'sprites/{tablero.tabla[nn][mm][1]}', cv2.IMREAD_UNCHANGED)))

    for nn in range(tabla_alto):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('cargando mapa...')

        print(f'{tabla_alto}/{tabla_alto} -- 1')
        print(f'{nn+1}/{tabla_alto} -- 2')

        for mm in range(tabla_ancho):
            addd(0, nn, mm, map2, np.array(cv2.imread(f'sprites/{tablero.tabla[nn][mm][2]}', cv2.IMREAD_UNCHANGED)))

    cv2.imwrite('map1.png', map1)
    cv2.imwrite('map2.png', map2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()