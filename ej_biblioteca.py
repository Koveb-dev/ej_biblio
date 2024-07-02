# EJERCICIO BIBLIO

from funciones_biblio import *

print('Bienvenido a la biblioteca-k')
limpiar_esperar_screen()


opciones = (1, 2, 3, 4, 5, 6)

while True:
    limpiar_esperar_screen()
    opc = menu_opciones((opciones))

    if opc == 1:
        agregar_libro()
    elif opc == 2:
        mostrar_libros()
    elif opc == 3:
        buscar_libro_titulo()
    elif opc == 4:
        actualizar_info_libro()
    elif opc == 5:
        guardar_libro_archivo_json()
    else:
        salir()
        break
