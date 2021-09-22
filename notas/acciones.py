import notas.nota as modelo

class Acciones:
    def crear(self, usuario):
        print(f"OK {usuario[1]}!!! vamos a crear una nueva nota")
        titulo = input("\nIntroduce el titulo de tu nota: ")
        descripcion = input("Agrega contenido a tu nota: ")
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        if guardar[0] >=1:
            print(f"\n Correcto has guardado la nota: {nota.titulo}")
        else:
            print(f"\n Error no se pudo guardar la nota, lo siento {usuario[1]}")

    def mostrar(self, usuario):
        print(f"\nOk {usuario[1]}, aqui tienes tus notas: ")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        for nota in notas:
            print("\n***********************************************")
            print(nota[2])
            print(nota[3])

    def borrar(self, usuario):
        print(f"\n Ok {usuario[1]}!!! Vamos a borrar notas")
        titulo = input("Introduce el titulo de la nota que desas borrar: ")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()
        if eliminar[0] >= 1:
            print(f"La nota {nota.titulo} se borro correctamente")
        else:
            print("Error, no se ah borrado la nota. Intentalo mas tarde")

