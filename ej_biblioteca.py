from funciones_biblio import *


print('Bienvenido a la app Biblioteca!')
limpiar_pant_esperar()

opciones = (1, 2, 3, 4, 5, 6)

while True:
    limpiar_pant_esperar()
    opc = opciones_and_menu((opciones))

    if opc == 1:
        print('Agregar un libro!')
        limpiar_pant_esperar()
        agregar_libro()
    elif opc == 2:
        print('Mostrar libros!')
        limpiar_pant_esperar()
        mostrar_libros()
    elif opc == 3:
        print('Buscar libro por titulo')
        limpiar_pant_esperar()
        buscar_libro_titulo()
    elif opc == 4:
        print('Actualizar informacion de un libro!')
        limpiar_pant_esperar()
        actualizar_info_libro()
    elif opc == 5:
        print('Guardar libros en json!')
        limpiar_pant_esperar()
        guardar_libros_archivo_json()
    else:
        salir()
        break
