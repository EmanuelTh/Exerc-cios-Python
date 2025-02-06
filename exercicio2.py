import math
def area_triangulo(x , y, z):


    if x + y > z and x + z > y and y + z > x:
        semi_perimetro= (x+y+z)/2
        area= math.sqrt(semi_perimetro*(semi_perimetro-x)*(semi_perimetro-y)*(semi_perimetro-z))
        print (area)
    
    else:
        print('lados dados nao formam um triangulo')


a=5
b=6
c=7

area=  area_triangulo(a,b,c)