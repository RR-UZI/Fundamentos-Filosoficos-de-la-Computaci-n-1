# practica 11
# cornejo olivares uziel
# garcia madrigal carlos martin

from colorama import init, Back, Fore, Cursor
import os
import sys
import select
import random



class _Getch:

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty
        import sys

    def __call__(self):
        import sys
        import tty
        import termios
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


letras = [
    [
        " # ",
        "# #",
        "###",
        "# #",
        "# #"
    ],  # A

    [
        "## ",
        "# #",
        "## ",
        "# #",
        "##"
    ],  # B

    [
        " ##",
        "#  ",
        "#  ",
        "#  ",
        " ##"
    ],  # C

    [
        "## ",
        "# #",
        "# #",
        "# #",
        "## "
    ],  # D

    [
        "###",
        "#  ",
        "## ",
        "#  ",
        "###"
    ],  # E

    [
        "###",
        "#  ",
        "## ",
        "#  ",
        "#  "
    ],  # F

    [
        " ##",
        "#  ",
        "# #",
        "# #",
        " ##"
    ],  # G

    [
        "# #",
        "# #",
        "###",
        "# #",
        "# #"
    ],  # H

    [
        "###",
        " # ",
        " # ",
        " # ",
        "###"
    ],  # I

    [
        " ##",
        "  #",
        "  #",
        "# #",
        " # "
    ],  # J

    [
        "# #",
        "# #",
        "## ",
        "# #",
        "# #"
    ],  # K

    [
        "#  ",
        "#  ",
        "#  ",
        "#  ",
        "###"
    ],  # L

    [
        "# #",
        "###",
        "###",
        "# #",
        "# #"
    ],  # M

    [
        "###",
        "# #",
        "# #",
        "# #",
        "# #"
    ],  # N

    [
        " # ",
        "# #",
        "# #",
        "# #",
        " # "
    ],  # O
    [
        "## ",
        "# #",
        "## ",
        "#  ",
        "#  "
    ],  # P
    [
        " #",
        "# #",
        "# #",
        " ##",
        "  #"
    ],  # Q
    [
        "## ",
        "# #",
        "## ",
        "# #",
        "# #",
    ],  # R
    [
        " ##",
        "# ",
        " #",
        "  #",
        "## "
    ],  # S
    [
        "###",
        " #",
        " #",
        " #",
        " #"
    ],  # T
    [
        "# #",
        "# #",
        "# #",
        "# #",
        "###"
    ],  # U
    [
        "# #",
        "# #",
        "# #",
        "# #",
        " #"
    ],  # V
    [
        "# #",
        "# #",
        "###",
        "###",
        "# #"
    ],  # W
    [
        "# #",
        "# #",
        " #",
        "# #",
        "# #"
    ],  # X
    [
        "# #",
        "# #",
        " #",
        " #",
        " #"
    ],  # Y
    [
        "###",
        "  #",
        " #",
        "# ",
        "###"
    ],  # Z
    [
        "   ",
        "   ",
        "   ",
        "   ",
        "   "
    ]  # espacio
]
colores = [Fore.GREEN, Fore.RED, Fore.LIGHTYELLOW_EX,
           Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.LIGHTGREEN_EX]

color_por_default = Fore.WHITE


def obtener_color_aleatorio():
    return colores[random.randrange(len(colores))]


def escribe_linea(x, y, color, linea):
    print(Cursor.POS(x, y) + color + linea)

###
# Funcion que borra la pantalla de acuerdo al sistema operativo.
###
def borrarPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def imprime_letra_en_ascii(letra, x, y, color):
    for row in letra:
        escribe_linea(x, y, color, row)
        y += 1


def obtenerLetra(letra):
    if letra == 32:
        return letras[len(letras)-1]
    if(letra > 90 or letra < 65):
        raise Exception("Caracter no valido!")
    return letras[letra-65]


def imprimir_frase(frase):
    borrarPantalla()
    print(Fore.WHITE+"Para salir presiona la tecla -> Q");
    x = 0
    for letra in frase:
        letra_ascii = obtenerLetra(ord(letra))
        imprime_letra_en_ascii(letra_ascii, x, 5, color_por_default)
        if x == 0:
            x += 5
        else:
            x += 4


def pedir_frase():
    frase = input("Ingresa frase: ")
    frase = frase.upper()
    imprimir_frase(frase)
    getch = _Getch()
    tecla = ""
    color = obtener_color_aleatorio()
    if (len(frase) == 1):
        letra_seleccionada = 0;
    else:
        letra_seleccionada = random.randrange(len(frase)-1)
    imprime_letra_en_ascii(obtenerLetra(ord(frase[letra_seleccionada])),
                           calcular_coordenada_de_letra_seleccionada(
                               letra_seleccionada),
                           5,
                           color)
    while(tecla != 'q'):
        tecla = getch()
        if(tecla == '\033'):  # flecha
            getch()  # ignorar [
            tecla = getch()
            if tecla == 'C':  # derecha
                imprimir_frase(frase)
                color = obtener_color_aleatorio()
                if (letra_seleccionada + 1 == len(frase)):
                    letra_seleccionada = 0
                else:
                    letra_seleccionada += 1
                imprime_letra_en_ascii(obtenerLetra(ord(
                    frase[letra_seleccionada])), calcular_coordenada_de_letra_seleccionada(letra_seleccionada), 5, color)
            elif tecla == 'D':  # izquierda
                imprimir_frase(frase)
                color = obtener_color_aleatorio()
                if (letra_seleccionada - 1 < 0):
                    letra_seleccionada = len(frase)-1
                else:
                    letra_seleccionada -= 1
                imprime_letra_en_ascii(obtenerLetra(ord(
                    frase[letra_seleccionada])), calcular_coordenada_de_letra_seleccionada(letra_seleccionada), 5, color)


def calcular_coordenada_de_letra_seleccionada(indice):
    if indice == 0:
        return indice
    return indice * 4 + 1


def menu():
    print(Fore.BLUE+"practica 11");
    print(Fore.MAGENTA+"cornejo olivares uziel");
    print(Fore.CYAN+"garcia madrigal carlos martin");
    print("\n""**********************""\n");
    pedir_frase();
    init()
    opcion = 0
    while(opcion != 2):
        borrarPantalla()
        print("1. Ingresar Frase ")
        print("2. Salir")
        try:
            opcion = int(input("Ingresa opcion deseada: "))
        except:
            print("Valor no valido favor de ingreser una opcion correcta ");
            input("Presiona enter para continuar ")
        if (opcion == 1):
            pedir_frase()
            


menu()
