nombreUsuario=input("ingrese su nombre")
edadUsuario=int(input("digita tu edad "))

if  edadUsuario>=0 and edadUsuario<=15:
    print(f"querido {nombreUsuario} juusted es un niño")

elif edadUsuario>15 and edadUsuario<=28:
    print(f"qurido{nombreUsuario} usted es un joven")

elif edadUsuario>28 and edadUsuario<=60:
    print(f"querido {nombreUsuario} usted es un adulto")
    
elif edadUsuario>60 and edadUsuario<=110:
    print(f"querido {nombreUsuario} usted es un adulo mayor")
    
else:
    print("edad invalida")