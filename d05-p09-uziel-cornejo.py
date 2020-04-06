#practica 09
#cornejo olivares uziel
#garcia madrigal carlos martin

print("practica 09");
print("cornejo olivares uziel");
print("garcia madrigal carlos martin");

print("\n""*************************************""\n");

def e1(): #Descuento en un teatro
    total_descuento = 0
    count = 0
    iterador = ["1"];
    precio_boleto = 80
    descuento_por_categoria = [0,0,0,0,0];

    for i in iterador:
        precio_boleto = 80
        edad = int(input("Cual es tu edad? "));
        if (edad < 5):
            print("No puedes ingresar al tetro");
        elif (edad >= 5 and edad <= 14):
            descuento_por_categoria[0] += precio_boleto * .35
            count += 1
        elif (edad >= 15 and edad <= 19):
            descuento_por_categoria[1] += precio_boleto * .25
            count += 1
        elif (edad >= 20 and edad <= 45):
            descuento_por_categoria[2] += precio_boleto * .10
            count += 1
        elif (edad >= 46 and edad <= 65):
            descuento_por_categoria[3] += precio_boleto * .25
            count += 1

        elif (edad >= 66):
            descuento_por_categoria[4] += precio_boleto * .35
            count += 1
        salir = str(input("Quieres comprar otro boleto ? [Y/N] "));
        if (salir != "N" and salir != "n"):
            iterador.append(i);
    contador = 1;
    for descuento_categoria in descuento_por_categoria:
        print("El descuento de la categoria", contador," fue de: ",descuento_categoria);
        total_descuento += descuento_categoria;
        contador += 1;
    print("El total de descuento que se hizo en el teatro fue de: ",total_descuento);
    print("Personas que ingresaron al teatro ",count);
    print("\n""*************************************""\n");

def e2(): #Aire
    rep = [1];
    vhl = 1;
    tp = -1;

    for x in rep:
        print("Ingrese los datos del vehículo",vhl);
        print("Ingrese -1 para terminar de ingresar datos.");

        print("\n""*************************************""\n");

        try: 
            tp = str(input("¿El vehículo es una motocicleta o un automóvil? (presiona 1: auto, presiona 2: moto): "));
            if tp == "-1":
                print("Decidiste salir del programa.");
                rep.remove(1);
                tp = -1;
            elif tp == "vehl" or tp == "coche" or tp == "carro" or tp == "1" or tp == "vehiculo":
                tp = 4;
            elif tp == "moto" or tp == "motocicleta" or tp == "2":
                tp = 2;
            else: 
                tp = -1;
                print("Dato ingresado no valido, ingresar correctamente por favor");
                print("\n""*************************************""\n");

            if tp != -1:
                llantas = [];
                e = 0;
                for i in range(tp):
                    presion = str(input("Presión de este neumático %i: "%(i+1)));
                    presion = float(presion);
                    if presion > 0:
                        volumen = str(input("Volumen de este neumático %i: "%(i+1)));
                        volumen = float(volumen);
                        if volumen > 0:
                            temperatura = str(input("Temperatura de este neumático %i: "%(i+1)));
                            temperatura = float(temperatura)
                    msv = (presion * volumen)/(0.37 * (temperatura+460));
                    llantas.append(msv);
                if e == 0:
                    masa = 0;
                    for msv in llantas:
                        masa += msv;
                    msp = masa/tp;
                    print("Este vehículo con %i llantas tiene un promedio de masa de %0.1f"%(tp, msp));
                    vhl+=1
                    print("\n""*************************************""\n");
        except ValueError: 
            print("introduciste un valor incorrecto, favor de intentar de nuevo.")
            print("\n""*************************************""\n");
        rep.append(1)

def e3(): #Granja
    vl = [1];
    g = 1;
    c = 0;
    for i in vl:
        print("Ingresa los datos de la gallina %i" %g);
        print("Ingresa -1 para terminar");
        print("\n""*************************************""\n");
        try:
            p = str(input("Introduzca el peso (kg) de la gallina %i: " %g));
            p = float(p);
            if p == -1:
                print("Terminaste de calcular");
                print("\n""*************************************""\n");
                if g > 1:
                    c = c/g;
                    print("El promedio de calidad de las gallinas es de %.1f" %c);
                    if c >= 15:
                        cost = c * 1.2;
                        print("El precio por kilo será de : %.1f$" %cost);
                    if c > 8 and c < 15:
                        cost = c * 1.0;
                        print("El precio por kilo será de : %.1f$" %cost);
                    if c <= 8:
                        cost = c * 0.8;
                        print("El precio por kilo será de : %.1f$" %cost);
                vl.remove(1);

            elif p <= 0:
                print("El peso tiene que ser mayor a 0, volver a introducir");
            else:

                h = str(input("Altura (cm) de la gallina %i: " %g));
                h = float(h);
                if h <= 0:
                    print("La altura tiene que ser mayor a 0, volver a introducir");
                else:
                    egg = str(input("¿Cuántos huevos pone la gallina %i?: " %g));
                    egg = int(egg);
                    if egg <= 0:
                        print("Los huevos tienen que ser mayor a 0, volver a introducir");
                    else:
                        c = ((p*h)/egg)+c;
                        g+=1;
                        print("La calidad de la gallina es igual a: %0.1f" %((p*h)/egg));
                        print("\n""*************************************""\n");
        except ValueError: 
            print("introduciste un valor incorrecto, favor de intentar de nuevo.");
            print("\n""*************************************""\n");
        vl.append(1);

def e4(): #Diputados
    vt = [1];
    dp1 = 0;
    dp2 = 0;
    dp3 = 0;
    dp4 = 0;
    for i in vt:
        print("-1 : Terminar\n1: En contra\n2: A favor\n3: Se abstiene\n");
        print("\n""*************************************""\n");
        try:
            dt = str(input("El diputado %i decidió: " %(dp1+1)));
            dp1+=1;
            if dt == "en contra" or dt == "1":
                dp2+=1;
            elif dt == "a favor" or dt == "2":
                dp3+=1;
            elif dt == "se abstiene" or dt == "3":
                dp4+=1;
            elif dt == "terminar" or dt == "-1":
                print("\nDecidiste terminar el conteo de votos.");
                print("\nSe tomaron en cuenta %i diputados." %(dp1-1));
                print("%i Estuvieron a favor %.2f%%" %(dp3, (dp3*100)/(dp1-1)));
                print("%i Estuvieron en contra %.2f%%" %(dp2, (dp2*100)/(dp1-1)));
                print("%i Se abstuvieron de votar %.2f%%" %(dp4, (dp4*100)/(dp1-1)));
                vt.remove(1);
            else:
                print("Introduciste un valor incorrecto, favor de intentar de nuevo.");
                dp1-=1;
        except ValueError:
                print("Introduciste un valor incorrecto, favor de intentar de nuevo.");

        vt.append(1);

def e5():#Hexadecimal
    vt = [1];
    print("\n""*************************************""\n");
    for i in vt:
        try:
            n = str(input("Introduce un número entero par: "));
            n = int(n);

            if n%2==0:
                h = hex(n);
                print("El número %i en hexadecimal es" %n, h);
                h = 0;
                for x in range(0, (n+1), 2):
                    h2 = hex(x);
                    print("Haciendo la suma del hexadecimal:", h2);
                    h += x;
                h = hex(h);    
                print("La suma de los pares del 0 al %i en hexadecimal es" %n, h);
                print("\n""*************************************""\n");
                vt.remove(1);
            else: 
                print("Introduciste un numero impar, favor de ingresar uno par");
                print("\n""*************************************""\n");
        except ValueError:
            print("Introduciste un valor incorrecto, favor de ingresar un número entero.");
            print("\n""*************************************""\n");
        vt.append(1);



    

    
def e6(): # n alumnos
    max_cal = 0 
    max_calificaciones = []
    n_alumnos = int(input("Ingrese numero de alumnos a calificar: "));

    try:
        for alumno in range(n_alumnos):
            nombre = str(input("Nombre del alumno: "));
            calificacion = 0
            for i in range(1,4):
                calificacion += float(input("Ingrese la calificacion de la practica {} :".format(i)));
            promedio = calificacion / 3
            if (max_cal < promedio):
                max_calificaciones = []
                max_cal = promedio
                max_calificaciones.append([max_cal, nombre])
            elif (max_cal == promedio):
                max_calificaciones.append([max_cal, nombre])
        if len(max_calificaciones) > 1:
            print("Hubo un empate");
        for max_cal in max_calificaciones:
            print("Nombre: ", max_cal[1],
                "Mayor Promedio: ",max_cal[0]);
        print("\n""*************************************""\n");

    except ValueError:
            print("introduciste un valor incorrecto, favor de intentar de nuevo.");
            return e6();
            print("\n""*************************************""\n");
                
def menu():
    opciones=0 
    try:
        while (opciones!=-1):
            print("-1. Salir");
            print("Presiona 1: Ejercicio 1");
            print("Presiona 2: Ejercicio 2");
            print("Presiona 3: Ejercicio 3");
            print("Presiona 4: Ejercicio 4");
            print("Presiona 5: Ejercicio 5");
            print("Presiona 6: Ejercicio 6");
            print("\n""*************************************""\n");
            opciones=int(input("Elige la opcion: "));
            if (opciones==1):
                e1();
            if (opciones==2):
                e2();
            if (opciones==3):
                e3();
            if (opciones==4):
                e4();
            if (opciones==5):
                e5();
            if (opciones==6):
                e6();
            if (opciones==0):
                print("Introduciste un valor incorrecto, favor de intentar de nuevo.");
                print("\n""*************************************""\n");
                return menu()
            if (opciones<=-2):
                print("Introduciste un valor incorrecto, favor de intentar de nuevo.");
                print("\n""*************************************""\n");
                return menu();
            if (opciones>=7):
                print("Introduciste un valor incorrecto, favor de intentar de nuevo.");
                print("\n""*************************************""\n");
                return menu();
    except ValueError:
        print("Introduciste un valor incorrecto, favor de intentar de nuevo.");
        print("\n""*************************************""\n");
        return menu();
        
menu();         






































    
    
       







e1();

          
        
    
 
        
