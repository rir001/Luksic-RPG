a1 = [1, 'blank.png',   'blank.png']                            #limites
a2 = [1, 'lucesL.png',  'blank.png']                            #Luces L
a3 = [1, 'lucesR.png',  'blank.png']                            #Luces R

b1 = [0, 'blank.png',   'blank.png']                            #madera
b2 = [0, 'goma.png',    'blank.png']                            #goma

s1 = [2, 'silla_roja_base.png', 'silla_roja_respaldo.png']      #silla roja
s2 = [2, 'silla_gris_base.png', 'silla_gris_respaldo.png']      #silla gris

p0 = [3, 'blank.png', 'blank.png', 'jorge']                  #Jorge Munoz

tabla = [
    [a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1],
    [a1,a1,a1,a1,a1,a1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,a1,a1,a1,a1,a1,a1],
    [a1,a1,a1,a1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,a1,a1,a1,a1],
    [a1,a1,a1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,p0,b1,b1,b1,b1,b1,a1,a1,a1],
    [a1,a1,a1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,a1,a1,a1],
    [a1,a1,b1,b1,b1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,b1,b1,b1,a1,a1],
    [a1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,a1],
    [a1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,a1],
    [a2,a1,s1,s1,s1,s1,b2,b2,s2,s1,s1,s2,s1,s1,s2,s1,s1,s2,s1,b2,b2,s1,s1,s1,s1,a3,a1],
    [a1,a1,s1,s1,s1,s1,b2,b2,s1,s2,s1,s1,s2,s1,s1,s2,s1,s1,s2,b2,b2,s1,s1,s1,s1,a1,a1],
    [a1,s1,s1,s1,s1,s1,b2,b2,s1,s1,s2,s1,s1,s2,s1,s1,s2,s1,s1,b2,b2,s1,s1,s1,s1,s1,a1],
    [a2,a1,s1,s1,s1,s1,b2,b2,s2,s1,s1,s2,s1,s1,s2,s1,s1,s2,s1,b2,b2,s1,s1,s1,s1,a3,a1],
    [a1,a1,s1,s1,s1,s1,b2,b2,s1,s2,s1,s1,s2,s1,s1,s2,s1,s1,s2,b2,b2,s1,s1,s1,s1,a1,a1],
    [a1,s1,s1,s1,s1,s1,b2,b2,s1,s1,s2,s1,s1,s2,s1,s1,s2,s1,s1,b2,b2,s1,s1,s1,s1,s1,a1],
    [a2,a1,s1,s1,s1,s1,b2,b2,s2,s1,s1,s2,s1,s1,s2,s1,s1,s2,s1,b2,b2,s1,s1,s1,s1,a3,a1],
    [a1,a1,s1,s1,s1,s1,b2,b2,s1,s2,s1,s1,s2,s1,s1,s2,s1,s1,s2,b2,b2,s1,s1,s1,s1,a1,a1],
    [a1,s1,s1,s1,s1,s1,b2,b2,s1,s1,s2,s1,s1,s2,s1,s1,s2,s1,s1,b2,b2,s1,s1,s1,s1,s1,a1],
    [a2,a1,s1,s1,s1,s1,b2,b2,s2,s1,s1,s2,s1,s1,s2,s1,s1,s2,s1,b2,b2,s1,s1,s1,s1,a3,a1],
    [a1,a1,s1,s1,s1,s1,b2,b2,s1,s2,s1,s1,s2,s1,s1,s2,s1,s1,s2,b2,b2,s1,s1,s1,s1,a1,a1],
    [a1,s1,s1,s1,s1,s1,b2,b2,s1,s1,s2,s1,s1,s2,s1,s1,s2,s1,s1,b2,b2,s1,s1,s1,s1,s1,a1],
    [a1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,a1],
    [a1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1,b1],
    [a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1]]