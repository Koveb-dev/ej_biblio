import time
import os
import json

libros = []
generos = ("Ciencia Ficcion", "Terror", "Aventuras", "Romantica", "Novela",
           "Historia", "Fantasia", "Infantil", "Juvenil", "Thriller", "Contemporaneo", "Otro")


def opciones_and_menu(p_opcs):
    while True:
        print('\tMenú biblioteca\n\n\t1. Agregar un libro\n\t2. Mostrar libros\n\t3. Buscar libro por titulo\n\t4. Actualizar informacion de un libro\n\t5. Guardar libros en un archivo JSON\n\t6. Salir\n')
        try:
            opc = int(input('Ingrese una opción: '))
            if opc in p_opcs:
                return opc
            else:
                print(
                    'ERROR! debe ingresar una opción valida, opciones validas(1,2,3,4,5,6)!')
            limpiar_pant_esperar()
        except:
            print('ERROR! debe ingresar un número entero!')


def agregar_libro():
    while True:
        titulo = str(input('Ingrese el titulo del libro: '))
        if len(titulo.strip()) >= 3:
            print('Titulo de libro registrado!')
            limpiar_pant_esperar()
            break
        else:
            print('ERROR! el titulo debe contener al menos 3 caracteres!')
        limpiar_pant_esperar()

    while True:
        nombre_autor = str(input('Ingrese el nombre del autor: '))
        if len(nombre_autor.strip()) >= 3 and nombre_autor.isalpha():
            print('Nombre del autor registrado!')
            limpiar_pant_esperar()
            break
        else:
            print('ERROR! debe ingresar un nombre que contenga al menos 3 letras')
        limpiar_pant_esperar()

    while True:
        apellido_autor = str(input('Ingrese el apellido del autor: '))
        if len(apellido_autor.strip()) >= 3 and apellido_autor.isalpha():
            print('Apellido del autor registrado!')
            limpiar_pant_esperar()
            break
        else:
            print('ERROR! debe ingresar un apellido que contenga al menos 3 letras')
        limpiar_pant_esperar()

    while True:
        try:
            anio_publi = int(
                input(f'Ingrese el año de la publicación del libro {titulo}: '))
            if anio_publi >= 1900 and anio_publi <= 2024:
                print('Año del libro registrado!')
                limpiar_pant_esperar()
                break
            else:
                print(
                    'ERROR! debe ingresar un año que este dentro de los año 1900 a 2024!')
            limpiar_pant_esperar()
        except:
            print('ERROR! debe ingresar números enteros!')

    while True:
        print("\tGeneros:\n\t1. Ciencia Ficcion\n\t2. Terror\n\t3. Aventuras \n\t4. Romantica\n\t5. Novela \n\t6. Historia \n\t7. Fantasia \n\t8. Infantil \n\t 9. Juvenil \n\t10. Thriller \n\t11. Contemporaneo\n\t12. Otro")
        try:
            genero_tipo = int(input('Ingrese el genero del libro: '))
            if genero_tipo >= 1 and genero_tipo <= 12:
                print('Genero del libro registrado!')
                limpiar_pant_esperar()
                break
            else:
                print('ERROR! debe ingresar una opcion valida de genero valido, opciones de genero validas (1,2,3,4,5,6,7,8,9,10,11,12)!')
            limpiar_pant_esperar()
        except:
            print('ERROR! debe ingresar un número entero!')

    nombre_completo_autor = str(nombre_autor + " " + apellido_autor)

    libro = {
        "titulo": titulo,
        "autor": nombre_completo_autor,
        "año": anio_publi,
        "genero": generos[genero_tipo-1]
    }

    libros.append(libro)
    print('LIBRO AGREGADO!')
    limpiar_pant_esperar()


def mostrar_libros():
    if len(libros) >= 1:
        while True:
            for l in libros:
                print('\tListado de libros\n')
                print(
                    f"\tTitulo: {l["titulo"]}\n\tAutor: {l["autor"]}\n\tAño: {l["año"]}\n\tGenero: {l["genero"]}\n\t")
            try:
                opc = int(
                    input('¿Deseas salir? Ingrese (1:Salir 2:Redirigir): '))
                if opc in (1, 2):
                    if opc == 1:
                        print('Saliendo')
                        limpiar_pant_esperar()
                        break
                    else:
                        print('Redirigiendo!')
                    limpiar_pant_esperar()
            except:
                print('ERROR! debe ingresar un númeroe entero!')

    else:
        print('NO HAY LIBROS REGISTRADOS!')
    limpiar_pant_esperar()


def buscar_libro_titulo():
    if len(libros) >= 1:
        while True:
            titulo_libro = str(
                input('Ingrese el titulo del libro que desea buscar: '))
            for x in libros:
                if x["titulo"] == titulo_libro:
                    print('Libro encontrado!')
                    limpiar_pant_esperar()
                    print(
                        f"\tTitulo: {x["titulo"]}\tAutor: {x["autor"]}\tAño: {x["año"]}\tGenero: {x["genero"]}")
                else:
                    print('Libro no encontrado :(! )')
                limpiar_pant_esperar()
            try:
                opc = int(
                    input('Deseas salir? Ingrese (1: Salir 2: Redirigir): '))
                if opc in (1, 2):
                    if opc == 1:
                        print('saliendo.')
                        limpiar_pant_esperar()
                        break
                    else:
                        print('redirigiendo opcion buscar libro.')
                    limpiar_pant_esperar()
                else:
                    print(
                        'ERROR! debes ingresar una opcion valida, opciones validas(1,2)!')
                limpiar_pant_esperar()
            except:
                print('ERROR! debe ingresar un número entero!')

    else:
        print('NO HAY LIBROS REGISTRADOS!')
    limpiar_pant_esperar()


def actualizar_info_libro():
    if len(libros) >= 1:
        while True:
            titulo_buscar = str(
                input('Ingrese el titulo del libro que actualizara: '))
            for x in libros:
                if x["titulo"] == titulo_buscar:
                    while True:
                        pass


def guardar_libros_archivo_json():
    pass


def salir():
    for x in range(1, 4):
        print('Saliendo de app biblioteca', ("."*x))
        limpiar_pant_esperar()


def limpiar_pant_esperar():
    time.sleep(1)
    os.system('cls')
