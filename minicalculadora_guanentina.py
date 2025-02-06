#input
import math

x=int(input("ingrese un número: "))

y=int(input("ingrese un número: "))

opc=int(input("ingrese una opc: "))

#processing

if opc==1:
   r=(x+y)

if opc==2:
    r=(x-y) 

if opc==3:
    r=(x*y) 

if opc==4:
    r=(x/y) 

if opc==5:    
    r=(x**y) 
    
if opc==6:
    
    r = math.log (x,y) 

else:
    r=("opción no válida")

#output

print("resultado: " +str(r))