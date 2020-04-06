#practica 06
#cornejo olivares uziel
#garcia madrigal carlos martin
print("practica 06")
print("cornejo olivares uziel")
print("garcia madrigal carlos martin")

print("\n""*********************************************************************************************************")

def e01():
    t1=30;
    t2=75;
    t3=85;
    t4=30;
    t5=75;
    t6=85;
    e=100;
    print("1) Calcular el promedio general de las 3 materias y obtener el promedio en cada una de ellas con los valores siguientes: ");
    print("Tarea 1 =",t1);
    print("Tarea 2 =",t2);
    print("Tarea 3 =",t3);
    print("Tarea 4 =",t4);
    print("Tarea 5 =",t5);
    print("Tarea 6 =",t6);
    print("Examen =",e);
e01();

def e01_1():
    t1=30;
    t2=75;
    t3=85;
    t4=30;
    t5=75;
    t6=85;
    e=100;
    examen=.20*e;
    tareas=((t1+t2+t3)/3)*.80;
    resultado=examen+tareas;
    print("La calificacion que obtuvo en matematicas es:",resultado);
   
e01_1();    

def e01_2():
    t1=30;
    t2=75;
    t3=85;
    t4=30;
    t5=75;
    t6=85;
    e=100;
    examen=.15*e;
    tareas=((t1+t2+t3)/3)*.85;
    resultado=examen+tareas;
    print("La calificacion que obtuvo en fisica es:",resultado);
    
e01_2();

def e01_3():
    t1=30;
    t2=75;
    t3=85;
    t4=30;
    t5=75;
    t6=85;
    e=100;
    examen=.75*100;
    tareas=((t1+t2+t3+t4+t5+t6)/6)*.25;
    resultado=examen+tareas;
    print("La calificacion que obtuvo en quimica es:",resultado);

e01_3();

def e01_4():
    t1=30;
    t2=75;
    t3=85;
    t4=30;
    t5=75;
    t6=85;
    e=100;
    examen1=.20*e;
    tareas1=((t1+t2+t3)/3)*.80;
    examen2=.15*e;
    tareas2=((t1+t2+t3)/3)*.85;
    examen3=.75*100;
    tareas3=((t1+t2+t3+t4+t5+t6)/6)*.25;
    resultado=((examen1+tareas1)+(examen2+tareas2)+(examen3+tareas3))/3;
    print("Su promedio general en las tres materias es:",resultado);

e01_4()
    
print("\n""*********************************************************************************************************")

def e02():
    cap_inv=1500000;
    gan=cap_inv*.033;

    print("2) Un individuo desea invertir su capital en un banco y desea saber cuánto dinero ganara después de un mes si el banco paga a razón de 3.3% mensual.");

    print("Invierte: $",cap_inv,"pesos");

    print("Despues de un mes ganara: $",gan,"pesos");

e02();

print("\n""*********************************************************************************************************")

def e03():
    sb=123.22;
    c=sb*0.15;
    cv=sb+c;
    ta=(cv*10)*365;
    tm=ta/31;
    print("3) Un vendedor recibe un sueldo base más un 15% extra por comisión de sus ventas");
    print("el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las diez ventas que realiza en un año y el total que recibirá por mes tomando en cuenta su sueldo base y comisiones");
    print("El sueldo base son $123.22 pesos al dia");
    print("Obtendra al año: $",ta,"pesos");
    print("Obtendra al mes: $",tm,"pesos");



e03();    

print("\n""*********************************************************************************************************")

def e04():
    tc=1000;
    d=tc*0.165;
    tp=tc-d;

    print("4) Una tienda ofrece un descuento del 16.5% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.");
    print("El total de la compra inicial es de $ 1000 pesos");
    print("El total final de la compra con el descuento es: $",tp,"pesos");

e04();
          
print("\n""*********************************************************************************************************")

def e05():
    ef=100;
    tf=30;
    c1=70;
    c2=85;
    prom=(c1+c2)/2;
    ppar=prom*0.55;
    pef=ef*0.30;
    ptf=tf*0.15;
    cf=ppar+pef+ptf;
    
    print("5) Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:");
    print("55% del promedio de sus dos calificaciones parciales");
    print("30% de la calificación del examen final");
    print("15% de la calificación de un trabajo final");
    print("En el primer parcial saco: 70 y en el segundo: 85");
    print("La calificación final en la materia de algoritmos es:",cf);

e05();

print("\n""*********************************************************************************************************")

def e06():
    nh=20;
    nm=10;
    ta=nh+nm;
    ph=(nh*100)/ta;
    pm=(nm*100)/ta;

    print("6) Un maestro desea saber qué porcentaje de hombres y que porcentaje de mujeres hay en un grupo de estudiantes");
    print("El total de hombres en la clase es de 20");
    print("El total de mujeres en la clase es de 10");
    print("El porcentaje de hombres en la clase es de:",ph);
    print("El porcentaje de mujeres en la clase es de:",pm);

e06();

print("\n""*********************************************************************************************************")

def e07():
    fnac=2001;
    fact=2020;
    edad=fact-fnac;

    print("7) Realizar un algoritmo que calcule la edad de una persona");
    print("Mi fecha de nacimiento es 2001");
    print("La fecha actual es 2020");
    print("Mi edad actual es",edad,"años");
          
e07();

print("\n""*********************************************************************************************************")

def e08():
    pa=12000000;
    pg=0.20*pa;
    pt=0.20*pa;
    pp=0.60*pa;

    print("8) En un hospital existen tres áreas: Ginecología, Pediatría, Traumatología");
    print("Ginecología recibe un 20% de presupuesto");
    print("Traumatología recibe un 20% de presupuesto");
    print("Pediatría recibe un 60% de presupuesto");
    print("Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal:");
    print("El presupuesto anual del hospital es de $12000000 pesos");
    print("El presupuesto anual que recibira el area de Ginecología es: $",pg,"pesos");
    print("El presupuesto anual que recibira el area de Traumatología es: $",pt,"pesos");
    print("El presupuesto anual que recibira el area de Pediatría es: $",pp,"pesos");

e08();

print("\n""*********************************************************************************************************")

def e09():
    pa=7000;
    gan=pa*0.40;
    pf=pa+gan;

    print("9) El dueño de una tienda compra un artículo a un precio determinado");
    print("Obtener el precio en que lo debe vender para obtener una ganancia del 40%");
    print("El precio del articulo es de $7000");
    print("El precio final con la ganancia es de: $",pf,"pesos");

e09();

print("\n""*********************************************************************************************************")

def e10():
    l=1
    m=1
    v=1
    ps=(l+m+v)/3
    
    print("10) Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra los tiempos obtenidos");
    print("Determinar el tiempo promedio que la persona tarda en recorrer la ruta en una semana cualquiera");
    print("El tiempo que hace el lunes, miercoles y viernes es de: 1 hora");
    print("El tiempo promedio semanal de la persona es de:",ps,"hora");
    
e10();

print("\n""*********************************************************************************************************")

def e11():
    p1=1000000;
    p2=1500000;
    p3=500000;
    ti=p1+p2+p3;
    pp1=(p1*100)/ti;
    pp2=(p2*100)/ti;
    pp3=(p3*100)/ti;
    
    print("11) Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta")
    print("Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida")
    print("El total invertido para fundar la empresa es de: $",ti,"pesos");
    print("El porcentaje invertido por la persona 1 es de:",pp1,"%");
    print("El porcentaje invertido por la persona 2 es de:",pp2,"%");
    print("El porcentaje invertido por la persona 3 es de:",pp3,"%");

e11();

    
    
