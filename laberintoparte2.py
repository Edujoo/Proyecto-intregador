'''Para esta primera parte debemos aprender a usar la librería `readchar` que nos permitirá leer un caracter suelto del teclado.

Tu tarea es
Instalar la librería: https://pypi.org/project/readchar/
Investigar cómo leer un caracter del teclado
Escribir un programa que corra un bucle infinito leyendo e imprimiento las teclas y sólo terminará cuando se presione la tecla ↑ indicada como UP'''


#Para leer el teclado usaremos readchar que es una libreria que nos ayuda a leer caracteres individuales y pulsasiones de teclas 
import readchar
from readchar import readkey, key

#Para leer un caracter del teclado 
def read_key():

    "Diccionario de teclas especiales"
    special_key = {
       key.RIGHT: "Flecha derecha →",
       key.LEFT: "Flecha izquierda ←",
       key.DOWN: "Flecha Abajo ↓",
       key.ENTER: "Enter",
       key.TAB: "Tab",
    }

    #Para salir del bucle se usara la tecla hacia arriba indicada como up
    print("\nPara salir del bucle presiona 'Fecha Arriba - UP'.")
    print("Puedes presionar una tecla para iniciar.")

    #este sera el bucle
    while True:
        presseed_key = readchar.readkey()

        if presseed_key == key.UP:
            print("Presionaste la tecla para salir")
            break
        elif presseed_key in special_key:
           pressed_key_name = special_key[presseed_key]
           print(f"Presionaste tecla: {pressed_key_name}")
        else:
            print(f"Presionaste tecla: {presseed_key}")

#funcion
read_key()