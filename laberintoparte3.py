''' Para esta sección del proyecto integrador necesitaremos aprender a manipular la terminal:
    Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, por cada presionada, borrar la terminal y e
    imprimir el nuevo número hasta el número 50.
    La operación de borrar la terminal e imprimir el nuevo número debe estar en su propia función.
    Para borrar la terminal antes de imprimir nuevo contenido usar la instrucción:
    os.system('cls' if os.name=='nt' else 'clear'), para esto se debe importar la librería os'''

#importar la libreria
import os
import readchar

#operacion borrar la terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#funcion
def manipulate_terminal():
    numbers = 0

    while numbers <= 50:
        print('Presiona tecla "n" para aumentar el numero')
        print(f'Numero actual: {numbers}')
        presseed_key = readchar.readkey()

        if presseed_key.lower() == 'n':
            numbers += 1
        else:
            break
        clear_terminal()

#funcionn
manipulate_terminal()

