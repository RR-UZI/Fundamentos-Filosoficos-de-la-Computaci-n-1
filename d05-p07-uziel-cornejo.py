#practica 07
#cornejo olivares uziel
#garcia madrigal carlos martin

print("practica 07");
print("cornejo olivares uziel");
print("garcia madrigal carlos martin");


def e1(): #calificaciones examen
    examen = float(input("Escribe cuanto saco en el examen: "));
    if ((examen >= 80) and (examen <= 100)):
     print("aprobado: ",examen);
    elif  ((examen <= 79) and (examen > 0)):
     print("reprobado: ",examen);
    else:
     print("datos introducidos no validos")
     return e1()    
        
     


def e2(): #sueldo de un trabajador
    sueldo = float(input("Escribe el sueldo del trabajador: "));
    aum1 = sueldo * .30
    aum2 = sueldo * .15
    aum3 = sueldo * .05
    saum1 = sueldo + aum1
    saum2 = sueldo + aum2
    saum3 = sueldo + aum3

    if((sueldo <= 19999) and (sueldo > 0)):
     print("Sueldo con el aumento: $",saum1);
    elif ((sueldo <= 22999) and (sueldo >= 20000)):
     print("Sueldo con el aumento: $",saum2);
    elif ((sueldo <= 24999) and (sueldo >= 23000)):
     print("Sueldo con aumento: $",suam3);
    elif (sueldo >= 25000):
     print("No cumple con los requisitos para recibir un aumento, su sueldo es de: ",sueldo)
    else:
        print("datos introducidos no validos");
        return e2()




def e3():  #salio por horas de un trabajador
    salario = float(input("Escriba el salario del trabajador por hora: "));
    horas = float(input("Escriba las horas que trabajo: "));
    sh1 = salario * horas
    sh2 = (horas - 40)*2
    sh3 = sh2 * salario
    sh4 = sh3 + (salario * 40)
    sh5 = (horas - 40)*3
    sh6 = sh5 * salario
    sh7 = sh6 + (salario * 40)

    if ((horas <= 40) and (horas > 0)):
     print("Salario en base a las horas: $",sh1);
    elif ((horas <= 48) and (horas >=41)):
     print("Salario en base a las horas: $",sh4);
    elif ((horas <= 56) and (horas >= 49)):
     print("Salario en base a las horas: $",sh4);
    elif (horas >=57):
     print("Salario en base a las horas: $",sh7);
    else:
        print("Datos introducidos no validos");



def e4(): #Monto mensual que recibira una familia
    hijos = int(input("Cuantos hijos tiene tu familia: "));
    edad = int(input("Cuantos hijos tienen entre 16 y 18 años: "));
    viuda = str(input("La madre de familia es viuda?: "));
    viuda1 = 20;
    esc = edad * 10;
    mont1 = esc + 70 + viuda1;
    mont2 = esc + 70;            
    mont3 = esc + 90 + viuda1;
    mont4 = esc + 90;
    mont5 = esc + 120 + viuda1;
    mont6 = esc + 120


    if ((hijos <= 2) and (hijos > 0) and (viuda == "si")):
      print("Monto mensual de la familia:",mont1);
    elif ((hijos <= 2) and (hijos > 0) and (viuda == "no")):
        print("Monto mensual de la familia:",mont2);
    elif ((hijos >= 3) and (hijos <= 5) and (viuda == "si")):
        print("Monto mensual de la familia:",mont3);
    elif ((hijos >= 3) and (hijos <= 5 ) and (viuda == "no")):
        print("Monto mensual de la familia:",mont4);
    elif ((hijos >= 6) and (viuda == "si")):
        print("Monto mensual de la familia:",mont5);
    elif ((hijos >= 6) and (viuda == "no")):
        print("Monto mensual de la familia:",mont6);
    else:
        print("Datos introducidos no validos")



def e5(): #Datos del usuario en 2020
    dia = int(input("Dia de nacimiento: "));
    mes = int(input("Mes de nacimiento: "));
    año = int(input("Año de nacimiento: "));
    bisiesto = ((año % 4 == 0) and (año % 100 != 0)) or (año % 400 == 0);
    if ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia < 1 or dia > 30)):
       print("Fecha invalida");
       return e5()
    if ((mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and (dia < 1 or dia > 31)):
       print("Fecha invalida");
       return e5()
    if (mes == 2):
        if (bisiesto and (dia < 1 or dia > 29)):
            print("Fecha invalida");
            return e5()
        if (not bisiesto and (dia < 1 or dia > 28)):
            print("Fecha invalida");
            return e5()
    if (año <= 2001):
        print("Puedes formar parte del equipo de futbol");
        grado = str(input("Grado escolar que cursas: "));
        grupo = str(input("Grupo: "));
        promedio = float(input("Promedio hasta el ultimo semestre: "));
        if ((promedio >= 60) and (promedio <= 100)):
         horario = str(input("Horario que prefieres de entrenamiento: "));
        if ((promedio < 60) and (promedio > 0)):
         print( "Sentimos mucho pero no podrás formar parte por tu bajo promedio");
    if (año > 2001):
     print("No puedes formar parte de algun equipo");




def e6(): #Automovil
   numero = str(input("Numero del auto: "));  
   if (len(numero) != 6):
    print("Numero del auto no valido, favor de ingresar un numero con 6 digitos");
    return e6()
   int_numero = int(numero); 
   millas = float(input("Millas recorridas: "));
   if (millas > 80):
    print( "Esta arriba del límite de velocidad")
   km = float(input("Kilometros recorridos del auto: "));
   if (km > 200) and (km < 350):
    print("Hace falta mantenimiento al auto");
   kml = float(input("Kilometros que recorre el auto con 1 litro de gasolina: "));
   if ((kml < 10) and (kml > 16)):
    print("Datos no validos");
   if ((kml >= 14) and (kml <= 16)):
    kmc = (kml/100);
    print("Consume poca gasolina")
    print("Su auto consume: ",kmc, "litros de gasolina en 100 kilometros");
   elif ((kml >= 10) and (kml <=13)):
    print("Consume algo de gasolina");
   else:
    print("Datos introducidos no validos, vuelva a ingresar los datos");
    return e6()




def e7(): #basketball
    numero = int(input("Ingresa el numero del jugador: "));
    tiro = int(input("Ingresa la cantidad de tiros que anoto el jugador: "));
    fallo = int(input("Ingresa cuantos tiros fallo el jugador: "));
    if ((tiro < 0) and (fallo < 0)):
     print("Datos no validos");
     return e7()
    total_tiros = tiro + fallo
    print("El total de tiros que realizo el jugador es:",total_tiros,"tiros");
    puntos = int(input("Ingresa la cantidad de puntos que anoto el jugador: "));
    if ((puntos >= 3) and (puntos <= 6)):
     print("Anoto pocos puntos");
    elif ((puntos >= 7) and (puntos <= 15)):
     print("Anotó puntos aceptables");
     puntos_3 = (puntos // 3);
     print("Anoto en promedio",puntos_3,"tiros de tres puntos");
    elif ((puntos >= 16) and (puntos <= 22)):
     print("Felicidades por sus anotaciones");
     puntos_3 = (puntos // 3);
     print("Anoto en promedio",puntos_3,"tiros de tres puntos");
    else:
     print("Datos introducidos no validos");
     return e7()

def imprime():
    print("\n""*********************************************************""\n");
    e1();
    print("\n""*********************************************************""\n");
    e2();
    print("\n""*********************************************************""\n");
    e3();
    print("\n""*********************************************************""\n");
    e4();
    print("\n""*********************************************************""\n");
    e5();
    print("\n""*********************************************************""\n");
    e6();
    print("\n""*********************************************************""\n");
    e7();
    print("\n""*********************************************************""\n");
imprime();





          



















        
