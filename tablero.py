a1 = [1, 'green.png'] #limites
a2 = [1, 'lucesL.png'] #Luces L
a3 = [1, 'lucesR.png'] #Luces R


b1 = [0, 'green.png'] #madera
b2 = [0, 'goma.png'] #goma


s1 = [2, 'silla_roja_base.png'] #silla roja
s2 = [2, 'silla_gris_base.png'] #silla gris


p0 = [3, 'green.png', 'jorge'] #Jorge Munoz



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
    [a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1,a1]
]

