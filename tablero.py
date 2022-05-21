a1 = [1, 'blank.png',   'blank.png']                            #limites
a2 = [1, 'lucesL.png',  'blank.png']                            #Luces L
a3 = [1, 'lucesR.png',  'blank.png']                            #Luces R
a4 = [1, 'telon.png',   'blank.png']
a5 = [0, 'subida/subida_L.png', 'blank.png']
a6 = [0, 'subida/subida_R.png', 'blank.png']

b1 = [0, 'blank.png',   'blank.png']                            #nada

s1 = [2, 'sillas/silla_roja_base.png', 'sillas/silla_roja_respaldo.png']      #silla roja
s2 = [2, 'sillas/silla_gris_base.png', 'sillas/silla_gris_respaldo.png']      #silla gris

p0 = [3, 'blank.png', 'blank.png', 'jorge']                  #Jorge Munoz

tabla = [
    [a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a4,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1],
    [a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1],
    [a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1],
    [a1,a1,a1,a1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,a1,a1,a1,a1],
    [a1,a1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,p0,b1,b1,b1,b1,b1,b1,a1,a1],
    [a1,a1,a5,a1,a1,a1,a1,a1,b1,b1,b1,b1,b1,a6,b1,b1,b1,b1,b1,a1,a1,a1,a1,a1,b1,a1,a1],
    [a1,b1,b1,b1,b1,b1,b1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,b1,b1,b1,b1,b1,b1,a1],
    [a1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,a1],
    [a2,a1,s1,s1,s1,s1,b1,b1,s2,s1,s1,s2,s1,s1,s2,s1,s1,s2,s1,b1,b1,s1,s1,s1,s1,a3,a1],
    [a1,a1,s1,s1,s1,s1,b1,b1,s1,s2,s1,s1,s2,s1,s1,s2,s1,s1,s2,b1,b1,s1,s1,s1,s1,a1,a1],
    [a1,s1,s1,s1,s1,s1,b1,b1,s1,s1,s2,s1,s1,s2,s1,s1,s2,s1,s1,b1,b1,s1,s1,s1,s1,s1,a1],
    [a2,a1,s1,s1,s1,s1,b1,b1,s2,s1,s1,s2,s1,s1,s2,s1,s1,s2,s1,b1,b1,s1,s1,s1,s1,a3,a1],
    [a1,a1,s1,s1,s1,s1,b1,b1,s1,s2,s1,s1,s2,s1,s1,s2,s1,s1,s2,b1,b1,s1,s1,s1,s1,a1,a1],
    [a1,s1,s1,s1,s1,s1,b1,b1,s1,s1,s2,s1,s1,s2,s1,s1,s2,s1,s1,b1,b1,s1,s1,s1,s1,s1,a1],
    [a2,a1,s1,s1,s1,s1,b1,b1,s2,s1,s1,s2,s1,s1,s2,s1,s1,s2,s1,b1,b1,s1,s1,s1,s1,a3,a1],
    [a1,a1,s1,s1,s1,s1,b1,b1,s1,s2,s1,s1,s2,s1,s1,s2,s1,s1,s2,b1,b1,s1,s1,s1,s1,a1,a1],
    [a1,s1,s1,s1,s1,s1,b1,b1,s1,s1,s2,s1,s1,s2,s1,s1,s2,s1,s1,b1,b1,s1,s1,s1,s1,s1,a1],
    [a2,a1,s1,s1,s1,s1,b1,b1,s2,s1,s1,s2,s1,s1,s2,s1,s1,s2,s1,b1,b1,s1,s1,s1,s1,a3,a1],
    [a1,a1,s1,s1,s1,s1,b1,b1,s1,s2,s1,s1,s2,s1,s1,s2,s1,s1,s2,b1,b1,s1,s1,s1,s1,a1,a1],
    [a1,s1,s1,s1,s1,s1,b1,b1,s1,s1,s2,s1,s1,s2,s1,s1,s2,s1,s1,b1,b1,s1,s1,s1,s1,s1,a1],
    [a1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,a1],
    [a1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1],
    [a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1]]