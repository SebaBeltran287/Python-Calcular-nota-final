import os
os.system("cls")

notafinal = 0       # inicializar una variable (colocar un valor inicial)

nota1 = float(input("Nota1: " ))
nota2 = float(input("Nota2: " ))
nota3 = float(input("Nota3: " ))

print("1. promedio ")
print("2. ponderacion ")

opcion = int(input("ingrese tipo de calculo: "))

if opcion==1:
    # promedio
    notafinal = round( (nota1+nota2+nota3)/3 , 1)
    print(f"{notafinal}")
else:
    # ponderacion
    p1 = int(input("ponderacion nota 1: " ))
    p2 = int(input("ponderacion nota 2: " ))
    p3 = int(input("ponderacion nota 3: " ))
    suma = p1+p2+p3
    if suma==100:
        notafinal = nota1*p1/100 + nota2*p2/100 + nota3*p3/100
        notafinal = round( notafinal, 1 )
        print(f"{notafinal}")
    else:
        print(" las ponderaciones no suman 100")