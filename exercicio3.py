import math
def bhaskara(a, b, c):
    delta = (b*b-4*a*c)
    x1= (-b + math.sqrt(delta))/(2*a)
    x2= (-b - math.sqrt(delta))/(2*a)

    print(x1,x2)

a= int(input())
b= int(input())
c= int(input())

bhaskara(a,b,c)