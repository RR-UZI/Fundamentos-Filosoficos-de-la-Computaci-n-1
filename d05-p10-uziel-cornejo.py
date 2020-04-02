#practica 10
#cornejo olivares uziel
#garcia madrigal carlos martin

print("\n""**********************");

from colorama import init,Back,Fore,Cursor
import os
import sys, select

init()


# Constantes de las teclas de movimiento 
arriba = 'w'
abajo = 's'
derecha = 'd'
izquierda = 'a'

#Constantes que identifican cada figura 
triangulo = 0
cuadrado = 1
rectangulo = 2

#Constantes que identifican las teclas con las figuras 
tecla_cuadrado = 'c'
tecla_triangulo = 't'
tecla_rectangulo = 'r'


posicion_figura = [
     [0, 18], #Triangulo 
     [15, 18], #Cuadrado 
     [45,18] #Corazon
    ]

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()



def dibujar(x, y, color, linea):
    print(Cursor.POS(x,y) + color + linea)


def e2(punto, color): #Triangulo
    x = punto[0]
    y = punto[1]
    n = 10
    for row in range(n+1):
        for col in range(n+1):
            if col == 0:
                dibujar(x+col, y+row, color, "*")
            elif row == col:
                dibujar(x+col, y+row, color, "*")
            elif row == n:
                dibujar(x+col, y+row, color, "*")

def e3(punto, color): #Cuadrado
    x = punto[0]
    y = punto[1]
    n = 10
    for fila in range(n+1):
        for col in range(n+1):
            if (fila == 0 or fila == n):
                dibujar(x+col, y+fila, color, "*")
            elif col == 0 or col == n:
                dibujar(x+col, y+fila, color, "*")
    
def e4(punto, color): #Rectangulo
    x = punto[0]
    y = punto[1]
    n = 10
    m = 20
    for fila in range(n+1):
        for col in range(m+1):
            if (fila == 0 or fila == n):
                dibujar(x+col, y+fila, color, "*")
            elif col == 0 or col == m:
                dibujar(x+col, y+fila, color, "*")
    
        
###
##Funcion que borra la pantalla de acuerdo al sistema operativo. 
###
def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


###
## Inicializa las figuras con el color y posicion inicial
###
def dibuja_figura(figura_seleccionada):
    if figura_seleccionada == triangulo: 
        e3(posicion_figura[cuadrado], Fore.RED);
        e4(posicion_figura[rectangulo], Fore.YELLOW);
        e2(posicion_figura[triangulo], Fore.GREEN);
    elif figura_seleccionada == cuadrado:
        e2(posicion_figura[triangulo], Fore.RED);
        e4(posicion_figura[rectangulo], Fore.YELLOW);
        e3(posicion_figura[cuadrado], Fore.GREEN);
    elif figura_seleccionada == rectangulo:
        e2(posicion_figura[triangulo], Fore.YELLOW);
        e3(posicion_figura[cuadrado], Fore.RED);
        e4(posicion_figura[rectangulo], Fore.GREEN);
###
## Funcion para mover las figuras
### 
def mover(direccion, figura):
    if direccion == arriba:
        render(figura);
        posicion_figura[figura][1] -= 1
        dibuja_figura(figura);
    elif direccion == abajo: 
        render(figura);
        posicion_figura[figura][1] += 1
        dibuja_figura(figura);
    elif direccion == derecha: 
        render(figura);
        posicion_figura[figura][0] += 1
        dibuja_figura(figura);
    elif direccion == izquierda:
        render(figura);
        posicion_figura[figura][0] -= 1
        dibuja_figura(figura);
    

def render(figura_seleccionada):
    if figura_seleccionada == triangulo:
        e2(posicion_figura[triangulo],Fore.BLACK);
    elif figura_seleccionada == cuadrado:
        e3(posicion_figura[cuadrado],Fore.BLACK);
    elif figura_seleccionada == rectangulo:
        e4(posicion_figura[rectangulo],Fore.BLACK);

def inicializa_figuras():
    e2(posicion_figura[triangulo],Fore.RED);
    e3(posicion_figura[cuadrado],Fore.GREEN);
    e4(posicion_figura[rectangulo],Fore.YELLOW);


def main(): 
    ## Tecla c = Cuadrado 
    ## Tecla t = triangulo 
    ## Tecla t = Corazon 
    ## Color de la figura seleccionada = verde 
    figura_seleccionada = cuadrado
    borrarPantalla()
    print(Back.BLACK+Fore.BLUE+"practica 10");
    print(Back.BLACK+Fore.MAGENTA+"cornejo olivares uziel");
    print(Back.BLACK+Fore.CYAN+"garcia madrigal carlos martin");
    print("\n""**********************");
    print(Fore.LIGHTMAGENTA_EX+"Presiona -> t para selccionar el Triangulo")
    print("Presiona -> c para seleccionar el Cuadrado")
    print("Presiona -> r para seleccionar el Rectangulo")
    print(Fore.LIGHTMAGENTA_EX+"Presiona -> w para mover la figura seleccionada hacia arriba")
    print("Presiona -> s para mover la figura seleccionada hacia abajo")
    print("Presiona -> d para mover la figura seleccionada hacia la derecha")
    print("Presiona -> a para mover la figura seleccionada hacia la izquierda")
    print(Fore.LIGHTMAGENTA_EX+"Presiona -> q para salir")
    inicializa_figuras()
    getchar = _Getch(); 
    while(True):
        tecla = getchar()
        if tecla == 'q':
            break;
        elif tecla == tecla_triangulo:
            inicializa_figuras()
            figura_seleccionada = triangulo
            dibuja_figura(figura_seleccionada)
        elif tecla == tecla_cuadrado:
            inicializa_figuras()
            figura_seleccionada = cuadrado
            dibuja_figura(figura_seleccionada)
        elif tecla == tecla_rectangulo:
            inicializa_figuras()
            figura_seleccionada = rectangulo
            dibuja_figura(figura_seleccionada)
        elif tecla == arriba:
            mover(arriba, figura_seleccionada)
        elif tecla == abajo:
            mover(abajo, figura_seleccionada)
        elif tecla == derecha:
            mover(derecha, figura_seleccionada)
        elif tecla == izquierda:
            mover(izquierda, figura_seleccionada)
    borrarPantalla();


main();
    



