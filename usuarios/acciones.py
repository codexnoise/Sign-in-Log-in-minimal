import usuarios.usuario as modelo
import notas.acciones  

class Acciones:
    def registro(self):
        print("\nIniciando registro en el sistema ...")
        nombre = input("Ingrese su nombre: ")
        apellidos = input("Ingrese sus apeliidos: ")
        email = input("Ingrese su email: ")
        password = input("Ingrese su contrasena: ")
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
        
        if registro[0]>=1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email: {registro[1].email}")
        else:
            print("\nError de registro")

    def login(self):
        print("Identificate en el sistema ...")
        try:
            email = input("Ingrese su email: ")
            password = input("Ingrese su contrasena: ")
            usuario=modelo.Usuario('','', email, password)
            login = usuario.identificar()
            if email == login[3]:
                print(f"\nBinvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Error de ingreso, intentalo mas tarde")

    def proximasAcciones(self,usuario):
        print("""
            Acciones disponibles:
            - Crear nota
            - Mostrar nota
            - Eliminar nota
            - Salir
        """)
        accion = input("Que deseas hacer?: ")
        ejecutar = notas.acciones.Acciones()

        if accion == "crear":
            ejecutar.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            ejecutar.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            ejecutar.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            exit()
       
