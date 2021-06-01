"""
PYTHON & MYSQL:
- Abrir asistente
- Login o registro
- Si eleginos registro, creara un usuario en la base de datos
- Si elegimos login, identificara al usuario y nos preguntara:
- Crear nota, mostrar notas, borrarlas
"""
from usuarios import acciones

print("""
Acciones disponibles:
    - registro
    - login
""")

ejecutar = acciones.Acciones()
accion = input("Que deseas hacer ?")

if accion == "registro":
    ejecutar.registro()
elif accion == "login":
    ejecutar.login()
    
