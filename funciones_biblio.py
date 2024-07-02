import json
import time
import os


libros = []
generos = ("Fantasia", "Terror", "Fabulas", "Novelas",
           "Ciencia Ficcion", "Romance", "Historia", "Deporte", "Otro")


def menu_opciones(p_opcs):
    while True:
        print('\tMenú biblioteca\n\n\t1. Agregar un libro\n\t2. Mostrar libros\n\t3. Buscar libro\n\t4. Actualizar información\n\t5. Guardar libros en un archivo JSON\n\t6. Salir\n')
        try:
            opc = int(input('\tIngrese una opción: '))
            if opc in p_opcs:
                return opc
            else:
                print(
                    'ERROR! debe ingresar una opcion valida, opciones validas (1,2,3,4,5,6)!')
            limpiar_esperar_screen()
        except:
            print('ERROR! debe ingresar un numero entero!')


def agregar_libro():
    print('Agregar libro!')
    limpiar_esperar_screen()
    while True:
        titulo = str(input('Ingrese el titulo del libro: '))
        if len(titulo.strip()) >= 3:
            print('Titulo registrado!')
            limpiar_esperar_screen()
            break
        else:
            print('ERROR! debe ingresar un libro que contenga al menos 3 letras!')
        limpiar_esperar_screen()

    while True:
        nombre_autor = str(input('Ingrese el nombre del autor: '))
        if len(nombre_autor.strip()) >= 3 and nombre_autor.isalpha():
            print('Nombre registrado!')
            limpiar_esperar_screen()
            break
        else:
            print('ERROR! el nombre del autor debe contener al menos 3 letras!')
        limpiar_esperar_screen()

    while True:
        apellido_autor = str(input('Ingrese el apellido del autor: '))
        if len(apellido_autor.strip()) >= 3 and apellido_autor.isalpha():
            print('Apellido registrado!')
            limpiar_esperar_screen()
            break
        else:
            print('ERROR! el apellido del autor debe contener al menos 3 letras!')
        limpiar_esperar_screen()

    while True:
        try:
            anio = int(input('Ingrese el año de publicacion del libro: '))
            if anio >= 1900 and anio <= 2024:
                print('Año de publicación registrado!')
                limpiar_esperar_screen()
                break
            else:
                print(
                    'ERROR! debe ingresar un añó valido, el año debe estar dentro de los años 1900 a 2024!')
            limpiar_esperar_screen()
        except:
            print('ERROR! debe ingresar números enteros!')

    while True:
        try:
            genero_tipo = int(input(
                'Ingrese el genero del libro (1:Fantasia 2:Terror 3:Fabula 4:Novela 5:Ciencia Ficción 6:Romance 7:Historia 8:Deportes 9:Otro): '))
            if genero_tipo in (1, 2, 3, 4, 5, 6, 7, 8):
                print('Genero registrado!')
                limpiar_esperar_screen()
                break
            else:
                print(
                    'ERROR! debe ingresar un genero valido, generos validos de libro (1,2,3,4,5,6,7,8,9)!')
            limpiar_esperar_screen()
        except:
            print('ERROR! debe ingresar un número entero!')

    nom_completo_autor = str(nombre_autor + " " + apellido_autor)

    libro = {
        "titulo": titulo,
        "autor": nom_completo_autor,
        "anio": anio,
        "genero": generos[genero_tipo-1]
    }

    libros.append(libro)

    print('LIBRO AGREGADO!')
    limpiar_esperar_screen()


def mostrar_libros():
    print('Ver libros!')
    limpiar_esperar_screen()

    if len(libros) >= 1:
        while True:
            print('\tListado de libros\n')
            for l in libros:
                print(
                    f"\tTitulo: {l["titulo"]}\tAutor: {l["autor"]}\tAño de publicacion: {l["anio"]}\tGenero: {l["genero"]}\n\t")
            mensaje = str(
                input('¿Deseas salir? Ingrese ("S":si o "N":redirigir): '))
            if mensaje.upper() in ("S", "N"):
                if mensaje.upper() == "S":
                    print('Saliendo.')
                    limpiar_esperar_screen()
                    break
                else:
                    print('Redirigiendo.')
                limpiar_esperar_screen()
            else:
                print(
                    'ERROR! debe ingresar una opcion valida, opciones validas("S" o "N")!')
            limpiar_esperar_screen()
    else:
        print('NO HAY LIBROS REGISTRADOS!')


def buscar_libro_titulo():
    print('Buscar libro!')
    limpiar_esperar_screen()

    if len(libros) >= 1:
        while True:
            buscar_titulo = str(
                input('Ingrese el titulo del libro que desea buscar: '))
            for lib in libros:
                if lib["titulo"].lower() == buscar_titulo.lower():
                    print('Libro Encontrado!')
                    limpiar_esperar_screen()
                    print(
                        f"Titulo: {lib["titulo"]}\tAutor: {lib["autor"]}\tAño de publicacion: {lib["anio"]}\tGenero: {lib["genero"]}")
                    time.sleep(3)
                    break
                else:
                    print('Libro no encontrado!')
                limpiar_esperar_screen()

            try:
                opc_salir = int(
                    input('¿Deseas salir? Ingrese (1:salir 0:redirigir a buscar libro): '))
                if opc_salir in (1, 0):
                    if opc_salir == 1:
                        print('Saliendo.')
                        limpiar_esperar_screen()
                        break
                    else:
                        print('Redirigiendo.')
                    limpiar_esperar_screen()
                else:
                    print(
                        'ERROR! debe ingresar una opcion valida, opciones validas(1 o 0)!')
                limpiar_esperar_screen()
            except:
                print('ERROR! debe ingresar un número entero!')

    else:
        print('NO HAY LIBROS REGISTRADOS!')
    limpiar_esperar_screen()


def actualizar_info_libro():
    print('Actualizar libro!')
    limpiar_esperar_screen()

    if len(libros) >= 1:

        while True:
            titulo_actualizar = str(
                input('Ingrese el titulo del libro que desea actualizar: '))
            if len(titulo_actualizar.strip()) >= 3:
                print('Titulo ingresado correctamente!')
                limpiar_esperar_screen()
                break
            else:
                print('ERROR! debe ingresar un titulo que contenga al menos 3 letras!')
            limpiar_esperar_screen()

        while True:
            for t in libros:
                if t["titulo"].lower() == titulo_actualizar.lower():
                    while True:
                        nombre_autor = str(
                            input('Ingrese el nuevo nombre del autor: '))
                        if len(nombre_autor.strip()) >= 3 and nombre_autor.isalpha():
                            print('Nombre de autor ingresado correctamente')
                            limpiar_esperar_screen()
                            break
                        else:
                            print(
                                'ERROR! el nombre del autor debe contener al menos 3 letras!')
                        limpiar_esperar_screen()

                    while True:
                        ap_autor = str(
                            input('Ingrese el nuevo apellido del autor: '))
                        if len(ap_autor.strip()) >= 3 and ap_autor.isalpha():
                            print('Apellido de autor ingresado correctamente')
                            limpiar_esperar_screen()
                            break
                        else:
                            print(
                                'ERROR! el apellido del autor debe contener al menos 3 letras!')
                        limpiar_esperar_screen()

                    nombre_completo_autor = str(nombre_autor + " " + ap_autor)
                    t["autor"] = nombre_completo_autor

                    while True:
                        try:
                            anio_n = int(
                                input('Ingrese el nuevo año de la publicacion del libro: '))
                            if anio_n >= 1900 and anio_n <= 2024:
                                t["anio"] = anio_n
                                print('Año ingresado registrado!')
                                limpiar_esperar_screen()
                                break
                            else:
                                print(
                                    'ERROR! el año de la publicacion debe estar dentro de los años 1900 a 2024!')
                            limpiar_esperar_screen()
                        except:
                            print('ERROR! debe ingresar números enteros!')

                    while True:
                        try:
                            gen_tipo = int(
                                input('Ingrese el nuevo genero del libro (1:Fantasia 2:Terror 3:Fabula 4:Novela 5:Ciencia Ficción 6:Romance 7:Historia 8:Deportes 9:Otro): '))
                            if gen_tipo in (1, 2, 3, 4, 5, 6, 7, 8):
                                t["genero"] = generos[gen_tipo-1]
                                print('Genero ingresado registrado!')
                                limpiar_esperar_screen()
                                break
                            else:
                                print(
                                    'ERROR! debe ingresar un genero valido, opciones de genero validas(1,2,3,4,5,6,7,8)!')
                            limpiar_esperar_screen()
                        except:
                            print('ERROR! debe ingresar un número entero!')

                    print('LIBRO MODIFICADO!')
                    break
                else:
                    print('El libro que desea modificar no existe!')
            break
    else:
        print('NO HAY LIBROS PARA MODIFICAR!')
    limpiar_esperar_screen()


def guardar_libro_archivo_json():
    print('Guardar libros en un archivo JSON!')
    limpiar_esperar_screen()

    if len(libros) >= 1:
        while True:
            nombrearchivo = str(input('Ingrese el nombre del archivo: '))
            if len(nombrearchivo.strip()) >= 3:
                print('Nombre archivo registrado!')
                limpiar_esperar_screen()
                break
            else:
                print(
                    'ERROR! el nombre del archivo debe contener al menos 3 caracteres!')
            limpiar_esperar_screen()

        try:
            with open(f"{nombrearchivo}.json", "x") as archivo:
                json.dump(libros, archivo, indent=2)
                print('ARCHIVO CREADO!')
        except:
            print('ERROR! el archivo ya existe!')
    else:
        print('NO HAY LIBROS PARA GUARDAR!')
    limpiar_esperar_screen()


def limpiar_esperar_screen():
    time.sleep(1)
    os.system('cls')


def salir():
    for x in range(1, 4):
        print('Saliendo de biblioteca-k', ("."*x))
        limpiar_esperar_screen()
