#practica 08
#cornejo olivares uziel
#garcia madrigal carlos martin

print("practica 08");
print("cornejo olivares uziel");
print("garcia madrigal carlos martin");

print("\n""*************************************""\n");

def e1(): # Área de una esfera
    print("\n""****************************************");
    radio = float(input("El radio de la esfera es: "));
    while (radio < 1):
      print("ERROR: El radio debe ser mayor que cero.");
      print("\n""****************************************");
      radio=float(input("Introduzca el radio de la esfera correctamente: "));
    pi = 3.1415
    area =  (4 * pi * radio**2);
    print("El área de una esfera de radio",radio,"es: ",area);
    print("\n""****************************************");

    
def e2(): #Volumen de un cubo
    print("\n""****************************************");
    arista = float(input("La arista del cubo es: "));
    cuenta = 0
    while (arista > 0):
     volumen = (arista ** 3);
     print("El volumen de un cubo de arista",arista, "es: ",volumen);
     arista = float(input("La arista del cubo es: "));
     cuenta += 1
    print("Los volumenes de cubos que han sido calculados son: ",cuenta);
    print("\n""****************************************");

 
def e3(): #Tablas de multiplicar
    print("\n""****************************************");
    from time import sleep;
    n = int(input("Ingresa tabla de multiplicar: "));
    while (n < 0):
     print("ERROR: El valor de la tabla de multiplicar debe ser positivo.");
     n = int(input("Ingresa tabla de multiplicar: "));
    contador = int(input("Ingresa de que numero quieres empezar a multiplicar: "));
    while (contador < 0):
     print("ERROR: El contador debe ser mayor que cero.");
     contador = int(input("Ingresa de que numero quieres empezar a multiplicar: "));
    while (contador >= 0):
     print(n,"x",contador,"=",(n * contador));
     contador -= 1
     sleep(1)
    print("\n""****************************************");


def e4(): #Signo contrario
    print("\n""****************************************");
    n = int(input("Cuantos numeros deseas ingresar: "));
    while (n > 0):
     num = int(input("Ingresa el numero: "));
     print(num * -1);
     n -= 1
    print("\n""****************************************");


def e5(): #Grupo de N Alumnos
    print("\n""****************************************");
    alumnos = int(input("Cuantos alumnos hay en el grupo: "));
    while (alumnos <= 0):
     print("ERROR Los alumnos deben ser mayor a 0");
     alumnos = int(input("Cuantos alumnos hay en el grupo: "));
  
    contar = alumnos
    cuenta = 0
    max_cal = 0
    max_nombre = ""
    
    while (alumnos > 0):
     nombre = (input("Nombre del alumno: "));
     calificacion = float(input("Cual es la calificacion del alumno: "));
     while (calificacion < 0 or calificacion > 100):
      print("ERROR La calificacion debe estar entre 0 y 100");
      calificacion = float(input("Cual es la calificacion del alumno: "));
     if (max_cal < calificacion):
        max_cal = calificacion
        max_nombre = nombre
     alumnos -= 1
     cuenta += calificacion
    print( "La media del grupo es: ",( cuenta / contar));
    print("La calificacion mas alta fue: ",max_cal,"y fue",max_nombre);
    print("\n""****************************************"); 

def e6(): #Transito de CDMX
    print("\n""****************************************");
    numero_de_autos = int(input("Cuantos autos pasaron: "));
    while (numero_de_autos < 0):
        print("ERROR El numero de autos debe ser mayor a 0")
        numero_de_autos = int(input("Cuantos autos pasaron: "));
    amarillo = 0
    rosa = 0
    rojo = 0                       
    verde = 0            
    azul = 0            

    while (numero_de_autos > 0):
        placa = str(input("Cual es el numero de placa: "));
        ultimo_digito = placa[len(placa)-1];
        if (ultimo_digito == '1' or ultimo_digito == '2'):
            amarillo += 1
        elif (ultimo_digito == '3' or ultimo_digito == '4'):
            rosa += 1
        elif (ultimo_digito == '5' or ultimo_digito == '6'):
            rojo +=1
        elif (ultimo_digito == '7' or ultimo_digito == '8'):
            verde += 1
        elif (ultimo_digito == '9' or ultimo_digito == '0'):
            azul += 1
        else:
            print("ERROR datos no validos");
            return e05();
        numero_de_autos -= 1

    print("Numero de autos color amarillo: ",amarillo,
          "\n"
          "Numero de autos color rosa: ",rosa,
          "\n"
          "Numero de autos color rojo: ",rojo,
          "\n"
          "Numero de autos color verde: ",verde,
          "\n"
          "Numero de autos color azul: ",azul);
    print("\n""****************************************");



def menu():
    opciones=0
    while (opciones!=1):
        print("1. Salir");
        print("2. Ejercicio 1");
        print("3. Ejercicio 2");
        print("4. Ejercicio 3");
        print("5. Ejercicio 4");
        print("6. Ejercicio 5");
        print("7. Ejercicio 6");
        opciones=int(input("Elige la opcion: "));
        if (opciones==2):
            e1();
        if (opciones==3):
            e2();
        if (opciones==4):
            e3();
        if (opciones==5):
            e4();
        if (opciones==6):
            e5();
        if (opciones==7):
            e6();

menu();

            












            
 
