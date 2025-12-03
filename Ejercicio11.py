
def validacion_contraseña():
    contraseña_sistema  = "admin123"

    Contraseña_usuario = input("ingrese contraseña")

    if contraseña_sistema == Contraseña_usuario:
        print("Contraseña correcta")
    else:
        print("contraseña incorrecta")        

validacion_contraseña()