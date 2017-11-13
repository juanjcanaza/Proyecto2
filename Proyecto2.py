import time
import sys

def registrar():
    cod = input(">> Codigo: ")
    cil = input(">> Ciclo: ")
    if cil == "1":
        print("Estos son los cursos que llevara durante el ciclo:")
        for i in cursos2:
            print(i)
            print("")
            print("**¡GRACIAS POR REGISTRARSE!**\n¿Desea entrar a comsultar?")
            perm = input("-> ")
            if perm =="si":
                print("-----------------------¡Bienvenido Kachimbo!!-----------------------")
                print(opte())
            elif perm != "si":
                return("¡Vuelva pronto!...")




    elif cil =="2" or cil=="3":
        var2 = int(input("¿Cuantos cursos va a llevar?(≤8):"))
        if var2 > 8:
            print("¡Lo sentimos, a sobrepasado el limite de cursos a llevar!")
            sys.exit(0)


        else:
            for i in cursos4:
                print(i)
                print("")
                print("Ahora, ¿Qué cursos deseas llevar? ")
            for j in range(1, var2 + 1):
                var3 = input(">> Curso#" + str(j) + ":")

        print(" ")
        print("**¡GRACIAS POR REGISTRARSE!**\n¿Desea entrar a comsultar?")
        pom = input("--> ")
        if pom == "si":
            print("-----------------------¡Bienvenido Kachimbo!!-----------------------")
            print(opta())
        elif pom != "si":
            return ("¡Vuelva pronto!...")


    else:
        print(">->->->->->->->->->->->->->->->->->->->->->->\nEste ciclo no esta dentro de las consultas\n"
              "\t ¡Por favor ingrese de nuevo!\n>->->->->->->->->->->->->->->->->->->->->->->")
        sys.exit(0)


def iniciar_sesion():
    c = input("Ingresa tu código: ")
    s = input("Ingresa tu carrera: ")
    print("-------------------------¡Bienvenido " + nomb +"!!---------------------------\n¿Que deseas consultar? \n1. Créditos \t2. Pensiones \t3. Menú de la semana \t4. Cubiculos")
    op = int(input("-->"))
    if op == 1:
        print("------------------------CREDITOS------------------------")
        creditos()
        opt()
    elif op == 2:
        print("------------------------PENSIONES------------------------")
        pensiones()
        opt()
    elif op == 3:
        print("-----------------------------MENU DE LA SEMANA----------------------------")
        menu()
        opt()
    elif op == 4:
        print("------------------------------RESERVACION DE CUBICULOS------------------------------")
        cubiculos()
        opt()


def cubiculos():
    preg = input("¿Que espera...quiere reservar un cubiculo? -->")
    while preg == "no" or preg == "No" or preg != "si":
        return (opt())
    while preg == "si":
        for i in cubi:
            print(i)
            print(reserva_cubi())

def reserva_cubi():
        I = "E800"
        II = "E801"
        III = "E802"
        IV = "E803"
        V = "E804"
        VI = "E805"

        A = "11:00am a 1:00pm"
        B = "1:00pm a 3:00pm"
        C = "3:00pm a 5:00pm"
        D = "12:00pm a 2:00pm"
        E = "9:00am a 11:00am"
        F = "2:00pm a 4:00pm"
        G = "4:00pm a 6:00pm"
        H = "10:00am a 12:00pm"

        op1 = input("Para registrarse elija un cubiculo --> ")
        if op1 == "I":
            print("-------------------------------------------------------\n  \t      Este cubiculo esta disponible\n\t Tiene para elegir los siguientes horarios:\n 11:00am a 1:00pm - 1:00pm a 3:00pm - 3:00pm a 5:00pm\n-------------------------------------------------------")
            print("A. 11:00am a 1:00pm\nB. 1:00pm a 3:00pm\nC. 3:00pm a 5:00pm")
            op2 = input("Ahora, escoja el horario --> ")
            if  op2 == "A":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo",I,"\n \tEn el horario de",A,"\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op2 == "B":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo",I,"\n \tEn el horario de",B,"\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op2 == "C":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo",I,"\n \tEn el horario de",C,"\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            else:
                print(">->->->->->->->->->->->->->->->->->->->->\n¡ERROR!, Este horario no esta disponible \n>->->->->->->->->->->->->->->->->->->->->")
                return(reserva_cubi())

        elif op1 == "II":
            print("-------------------------------------------------------\n  \t      Este cubiculo esta disponible\n\t Tiene para elegir los siguientes horarios:\n 10:00am a 12:00pm - 12:00pm a 2:00pm - 2:00pm a 4:00pm\n \t \t \t  -4:00pm a 6:00pm\n-------------------------------------------------------")
            print("H. 10:00am a 12:00pm\nD. 12:00pm a 2:00pm\nF. 2:00pm a 4:00pm\nG. 4:00pm a 6:00pm")
            op3 = input("Ahora, escoja el horario --> ")
            if op3 == "H":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", II,"\n \tEn el horario de", H, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op3 =="D":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", II,"\n \tEn el horario de", D, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op3 =="F":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", II,"\n \tEn el horario de", F, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op3 =="G":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", II,"\n \tEn el horario de", G, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            else:
                print(">->->->->->->->->->->->->->->->->->->->->\n¡ERROR!, Este horario no esta disponible \n>->->->->->->->->->->->->->->->->->->->->")
                return (reserva_cubi())

        elif op1 == "III":
            print("-------------------------------------------------------\n  \t      Este cubiculo esta disponible\n\t Tiene para elegir los siguientes horarios:\n 11:00pm a 1:00pm - 1:00pm a 3:00pm - 3:00pm a 5:00pm\n-------------------------------------------------------")
            print("A. 11:00pm a 1:00pm\nB. 1:00pm a 3:00pm\nC. 3:00pm a 5:00pm")
            op4 = input("Ahora, escoja el horario --> ")
            if op4 == "A":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", III,"\n \tEn el horario de", A, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op4 == "B":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", III,"\n \tEn el horario de", B, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op4 == "C":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", III,"\n \tEn el horario de", C, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            else:
                print(">->->->->->->->->->->->->->->->->->->->->\n¡ERROR!, Este horario no esta disponible \n>->->->->->->->->->->->->->->->->->->->->")
                return (reserva_cubi())

        elif op1 == "IV":
            print("-------------------------------------------------------\n  \t      Este cubiculo esta disponible\n\t Tiene para elegir los siguientes horarios:\n 9:00am a 11:00am - 11:00am a 1:00pm - 1:00pm a 3:00pm\n \t \t \t  - 3:00pm a 5:00pm\n-------------------------------------------------------")
            print("E. 9:00am a 11:00am\nA. 11:00am a 1:00pm\nB. 1:00pm a 3:00pm\nC. 3:00pm a 5:00pm")
            op5 = input("Ahora, escoja el horario --> ")
            if op5 == "E":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", IV,"\n \tEn el horario de", E, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op5 == "A":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", IV,"\n \tEn el horario de", A, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op5 == "B":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", IV,"\n \tEn el horario de", B, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op5 == "C":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", IV,"\n \tEn el horario de", C, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            else:
                print(">->->->->->->->->->->->->->->->->->->->->\n¡ERROR!, Este horario no esta disponible \n>->->->->->->->->->->->->->->->->->->->->")
                return (reserva_cubi())

        elif op1 == "V":
            print("-------------------------------------------------------\n  \t      Este cubiculo esta disponible\n\t Tiene para elegir los siguientes horarios:\n 10:00am a 12:00pm - 12:00pm a 2:00pm - 2:00pm a 4:00pm\n \t \t \t  - 4:00pm a 6:00pm\n-------------------------------------------------------")
            print("H. 10:00am a 12:00pm\nD. 12:00pm a 2:00pm\nF. 2:00pm a 4:00pm\nG. 4:00pm a 6:00pm")
            op6 = input("Ahora, escoja el horario --> ")
            if op6 == "H":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", V,"\n \tEn el horario de", H, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op6 == "D":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", V,"\n \tEn el horario de", D, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op6 == "F":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", V,"\n \tEn el horario de", F, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op6 == "G":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", V,"\n \tEn el horario de", G, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            else:
                print(">->->->->->->->->->->->->->->->->->->->->\n¡ERROR!, Este horario no esta disponible \n>->->->->->->->->->->->->->->->->->->->->")
                return (reserva_cubi())

        elif op1 == "VI":
            print("-------------------------------------------------------\n  \t      Este cubiculo esta disponible\n\t Tiene para elegir los siguientes horarios:\n 9:00am a 11:00am - 11:00am a 1:00pm - 1:00pm a 3:00pm\n \t \t \t  - 3:00pm 5:00pm\n-------------------------------------------------------")
            print("E. 9:00am a 11:00am\nA. 11:00am a 1:00pm\nB. 1:00pm a 3:00pm\nC. 3:00pm 5:00pm")
            op7 = input("Ahora, escoja el horario --> ")
            if op7 == "E":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", VI,"\n \tEn el horario de", E, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op7 == "A":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", VI,"\n \tEn el horario de", A, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op7 == "B":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", VI,"\n \tEn el horario de", B, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op7 == "C":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", VI,"\n \tEn el horario de", C, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            else:
                print(">->->->->->->->->->->->->->->->->->->->->\n¡ERROR!, Este horario no esta disponible \n>->->->->->->->->->->->->->->->->->->->->")
                return (reserva_cubi())

        elif op1 == "VII":
            print("-------------------------------------------------------\n  \t      Este cubiculo esta disponible\n\t Tiene para elegir los siguientes horarios:\n 10:00am a 12:00pm - 12:00pm a 2:00pm - 2:00pm a 4:00pm\n \t \t \t  - 4:00pm a 6:00pm\n-------------------------------------------------------")
            print("H. 10:00am a 12:00pm\nD. 12:00pm a 2:00pm\nE. 2:00pm a 4:00pm\nG. 4:00pm a 6:00pm")
            op8 = input("Ahora, escoja el horario --> ")
            if op8 == "H":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", VII,"\n \tEn el horario de", H, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op8 == "D":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", VII,"\n \tEn el horario de", D, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op8 == "E":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", VII,"\n \tEn el horario de", E, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            elif op8 == "G":
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n  \tSe ha reservado el cubiculo", VII,"\n \tEn el horario de", G, "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            else:
                print(">->->->->->->->->->->->->->->->->->->->->\n¡ERROR!, Este horario no esta disponible \n>->->->->->->->->->->->->->->->->->->->->")
                return (reserva_cubi())

        else:
            while op1 != "I" or op1 != "II" or op1 != "III" or op1 != "IV" or op1 != "V" or op1 != "VI" or op1 != "VII" or op1 != "VIII" or op1 != "IX":
                print(">->->->->->->->->->->->->->->->->->->->->\n ¡ERROR!, este cubiculo no esta registrado\n>->->->->->->->->->->->->->->->->->->->->")
                return(reserva_cubi())

        opt()


def creditos():
    print("¿En que ciclo estas?:\n1. Primer Ciclo \t   2. Segundo Ciclo \t   3. Tercer Ciclo")
    ci = input("-->")
    if ci == "1":
        for i in cur1:
            print(i)
        cu = input(">> Ingresa el curso:")
        if cu == "a":
            for i in mat:
                print(i)
        elif cu == "b":
            for i in fis:
                print(i)
        elif cu == "c":
            for i in compu:
                print(i)
        elif cu == "d":
            for i in glob:
                print(i)
        elif cu == "e":
            for i in coe:
                print(i)
        elif cu == "f":
            for i in quig:
                print(i)
        elif cu == "g":
            for i in quie:
                print(i)
        else:
            while cu != "a" or cu != "b" or cu != "c" or cu != "d" or cu != "e" or cu != "f" or cu != "g":
                print(
                    ">->->->->->->->->->->->->->->->->->->->->->->->->->\nERROR...curso invalido, por favor ingrese de nuevo!\n>->->->->->->->->->->->->->->->->->->->->->->->->->")
                return (creditos())
    elif ci == "2":
        for i in cur2:
            print(i)
        cu2 = input(">> Ingresa el curso:")
        if cu2 == "a":
            for i in mat2:
                print(i)
        elif cu2 == "b":
            for i in fis2:
                print(i)
        elif cu2 == "c":
            for i in cm:
                print(i)
        elif cu2 == "d":
            for i in po:
                print(i)
        elif cu2 == "e":
            for i in coe2:
                print(i)
        elif cu2 == "f":
            for i in ing:
                print(i)
        elif cu2 == "g":
            for i in pi:
                print(i)
        elif cu2 == "h":
            for i in ide:
                print(i)
        else:
            while cu2 != "a" or cu2 != "b" or cu2 != "d" or cu2 != "e" or cu2 != "f" or cu2 != "c" or cu2 != "g" or cu2 != "h":
                print(">->->->->->->->->->->->->->->->->->->->->->->->->->\nERROR...curso invalido, por favor ingrese de nuevo!\n>->->->->->->->->->->->->->->->->->->->->->->->->->")
                return (creditos())
    elif ci == "3":
        for i in cur3:
            print(i)
        cu3 = input(">> Ingresa el curso:")
        if cu3 == "a":
            for i in mat3:
                print(i)
        elif cu3 == "b":
            for i in ter:
                print(i)
        elif cu3 == "c":
            for i in ep:
                print(i)
        elif cu3 == "d":
            for i in ing2:
                print(i)
        elif cu3 == "e":
            for i in ge:
                print(i)
        elif cu3 == "f":
            for i in pi2:
                print(i)
        else:
            while cu3 != "matematica III" or cu3 != "Matematica III" or cu3 != "Termodinamica" or cu3 != "termodinamica" or cu3 != "Estadistica y Probabilidades" or cu3 != "estadistica y probabilidades" or cu3 != "Gestion de Empresas" or cu3 != "gestion de empresas" or cu3 != "Ingles II" or cu3 != "ingles II" or cu3 != "Proyecto Interdisciplinario II" or cu3 != "proyecto interdisciplinario II":
                print(">->->->->->->->->->->->->->->->->->->->->->->->->->\nERROR...curso invalido, por favor ingrese de nuevo!\n>->->->->->->->->->->->->->->->->->->->->->->->->->")
                return (creditos())
    opt()


def pensiones():
    e = input("Ingresa tu escala(A - B - C - D - E): ")
    if e == "A":
        print(
            "\n--------------------------------\n Su pensión es: S/.875 x Crédito \n--------------------------------\n>> El monto mensual es: S/."+str((24*875)//5))
    elif e == "B":
        print(
            " \n--------------------------------\n Su pensión es: S/.733 x Crédito \n--------------------------------\n>> El monto mensual es: S/."+str((24*733)//5))
    elif e == "C":
        print(
            " \n--------------------------------\n Su pensión es: S/.618 x Crédito \n--------------------------------\n>> El monto mensual es: S/."+str((24*618)//5))
    elif e == "D":
        print(
            " \n--------------------------------\n Su pensión es: S/.500 x Crédito \n--------------------------------\n>> El monto mensual es: S/."+str((24*500)//5))
    elif e == "E":
        print(
            " \n--------------------------------\n Su pensión es: S/.414 x Crédito \n--------------------------------\n>> El monto mensual es: S/."+str((24*414)//5))
    else:
        while e != "A" or e != "B" or e != "C" or e != "D" or e != "E":
            print(">->->->->->->->->->->->->->->->\n ERROR, escala no admitida \n Intentelo de nuevo por favor\n>->->->->->->->->->->->->->->->")
            return (pensiones())
    opt()


def menu():
    print("Elige el día del menú:\nI. Lunes \tII. Martes \t III. Miercoles  \tIV. Jueves  \t V. Viernes")
    dm = input("-->")
    if dm == "I":
        for i in lu:
            print(i)
    elif dm == "II":
        for i in mar:
            print(i)
    elif dm == "III":
        for i in mier:
            print(i)
    elif dm == "IV":
        for i in juev:
            print(i)
    elif dm == "V":
        for i in vier:
            print(i)
    else:
        while dm != "I" or dm != "II" or dm != "III" or dm != "IV" or dm != "V":
            print(
                ">->->->->->->->->->->->->->->->->->->->->->->->->->->->\nUpps...No hay menu disponible en este dia,lo sentimos!\n>->->->->->->->->->->->->->->->->->->->->->->->->->->->")
            return (menu())
    opt()


def opt():
    print(
        "¡Bien " + nomb + "!, Ahora...\n¿Deseas consultar algo más? \n1. Créditos \t2. Pensiones \t3. Menú de la semana  \t4. Cubiculos")
    o = int(input("-->"))
    if o == 1:
        print("------------------------CREDITOS------------------------")
        creditos()
    elif o == 2:
        print("------------------------PENSIONES------------------------")
        pensiones()
    elif o == 3:
        print("-----------------------------MENU DE LA SEMANA----------------------------")
        menu()
    elif o == 4:
        print("------------------------------RESERVACION DE CUBICULOS------------------------------")
        cubiculos()


def creditos2():
    print("------------------------CREDITOS------------------------\nEn este ciclo llevara")


def opte():
    print("¡Bien " + nomb + "!, Ahora...\n¿Qué deseas consultar?\n1. Créditos \t2. Pensiones \t3. Menú de la semana \t4 .Cubiculos")
    k = int(input("-->"))
    if k == 1:
        print("-----------------------------CREDITOS-----------------------------")
        for i in cursos1:
            print(i)
            print(opt())
    elif k == 2:
        print("------------------------PENSIONES------------------------")
        pensiones()
    elif k == 3:
        print("-----------------------------MENU DE LA SEMANA----------------------------")
        menu()
    elif k == 4:
        print("------------------------------RESERVACION DE CUBICULOS------------------------------")
        cubiculos()

def opta():
    print("¡Bien " + nomb + "!, Ahora...\n¿Qué deseas consultar?\n1. Créditos \t2. Pensiones \t3. Menú de la semana \t4 .Cubiculos")
    q = int(input("-->"))
    if q == 1:
        print("-----------------------------CREDITOS-----------------------------")
        print(creditos())
    elif q == 2:
        print("------------------------PENSIONES------------------------")
        pensiones()
    elif q == 3:
        print("-----------------------------MENU DE LA SEMANA----------------------------")
        menu()
    elif q == 4:
        print("------------------------------RESERVACION DE CUBICULOS------------------------------")
        cubiculos()


cur1 = ["CURSOS DE 1ER CICLO:\na) Matematica I\nb) Fisica I\nc) Intro. a la Ciencia de la computacion\nd) Desafios Globales\ne) Lab. de Comunicacion I\nf) Quimica General\ng) Quimica Experimental"]
cur2 = ["CURSOS DE 2DO CICLO:\na) Matematica II\nb) Fisica II\nc) Ciencias de los Materiales\nd) Programacion Orientada a Objetos\ne) Lab. de Comunicacion II\nf) Ingles I\ng) Proyecto Interdisciplinario I\nh) Intro. al Desarrollo de Empresas"]
cur3 = ["CURSOS DE 3ER CICLO:\na) Matematica III\nb) Termodinamica\nc) Estadistica y Probabilidades\nd) Ingles II\ne) Gestion de Empresas\nf) Proyecto Interdisciplinario II"]
mat = ["-----------------------------\nMatematica I vale 4 créditos\n-----------------------------"]
mat2 = ["-----------------------------\nMatematica II vale 4 créditos\n-----------------------------"]
mat3 = ["-----------------------------\nMatematica III vale 4 créditos\n-----------------------------"]
fis = ["-----------------------------\nFisica I vale 4 créditos\n-----------------------------"]
fis2 = ["-----------------------------\nFisica II vale 4 créditos\n-----------------------------"]
ter = ["-----------------------------\nTermodinamica vale 4 créditos\n-----------------------------"]
cm = ["--------------------------------------------\nCiencias de los Materiales vale 4 créditos\n--------------------------------------------"]
compu = ["------------------------------------------------------------\nIntroducción a la Ciencia de la Computación vale 4 créditos\n------------------------------------------------------------"]
po = ["--------------------------------------------------\nProgramacion Orientada a objetos vale 4 créditos\n--------------------------------------------------"]
glob = ["----------------------------------\nDesafíos Goblales vale 3 créditos\n----------------------------------"]
coe = ["----------------------------------------------\nLaboratorio de Comunicación I vale 3 créditos\n----------------------------------------------"]
coe2 = ["----------------------------------------------\nLaboratorio de Comunicacion II vale 3 créditos\n----------------------------------------------"]
quig = ["-------------------------------\nQuímica General vale 3 créditos\n-------------------------------"]
quie = ["------------------------------------\nQuímca Expermiental vale 3 créditos\n------------------------------------"]
ing = ["-------------------------\nIngles I vale 3 créditos\n-------------------------"]
ing2 = ["-------------------------\nIngles II vale 3 créditos\n-------------------------"]
pi = ["----------------------------------------------\nProyecto Interdisciplinario I vale 2 créditos\n----------------------------------------------"]
pi2 = ["----------------------------------------------\nProyecto Interdisciplinario II vale 2 créditos\n----------------------------------------------"]
ge = ["------------------------------------\nGestion de Empresas vale 2 créditos\n------------------------------------"]
ep = ["--------------------------------------------\nEstadistica y Probabilidades vale 4 créditos\n--------------------------------------------"]
ide = ["------------------------------------------------------\nIntroducción al Desarrollo de Empresas vale 2 creditos\n------------------------------------------------------"]


lu = [">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n--------------------------------\n Económico: \nPollo a la plancha  -   S/.7.50 \n--------------------------------\n Estudiantil: \nCausa de atún \t -  \tS/.8.50 \n--------------------------------\n Ejecutivo: \nLomo saltado \t - \tS/.7.50 \n-------------------------------- \n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"]
mar = [">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n--------------------------------\n Económico: \nAji de gallina \t   -\tS/.7.50 \n--------------------------------\n Estudiantil: \nChoclo con queso   - \tS/.8.50 \n--------------------------------\n Ejecutivo: \nChicarron de pescado - \tS/.7.50 \n-------------------------------- \n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"]
mier = [">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n-------------------------------------\n Económico: \nArroz con pollo \t-    S/.7.50 \n-------------------------------------\n Estudiantil: \nPapa a la huancaina \t-    S/.8.50 \n-------------------------------------\n Ejecutivo: \nOcopa \t\t  -\t     S/.7.50  \n------------------------------------- \n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"]
juev = [">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n--------------------------------\n Económico: \nMilanesa \t- \tS/.7.50 \n--------------------------------\n Estudiantil: \nSopa de casa \t- \tS/.8.50 \n--------------------------------\n Ejecutivo: \nArroz a la cubana  -\tS/.7.50 \n-------------------------------- \n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"]
vier = [">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n---------------------------------------- \nEconómico: \nArroz chaufa \t   -\t\tS/.7.50 \n---------------------------------------- \n Estudiantil: \nFrijoles rojos con carne    - \tS/.8.50 \n---------------------------------------- \n Ejecutivo: \nTallarines rojos \t- \tS/.7.50 \n---------------------------------------- \n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"]

cursos1 = [">> Matematica I ---------> vale 4 créditos \n>> Fisica I ---------> vale 4 créditos \n>> Intro. a la Ciencia de la Computación ---------> vale 4 créditos \n>> Desafios Globales ---------> vale 3 créditos \n>> Lab. de Comunicacion I ---------> vale 3 créditos \n>> Quimica General ---------> vale 3 créditos \n>> Quimica Experimental ---------> vale 3 créditos \n----------------------------\n   Total de creditos: 24\n----------------------------"]
cursos2=[">> Matematica I \n>> Fisica I \n>> Intro. a la Ciencia de la Computación \n>> Desafios Globales \n>> Lab. de Comunicación I \n>> Quimica General \n>> Quimica Experimental "]
cursos4 = ["a) Matematica I ---------> vale 4 créditos \nb) Fisica I ---------> vale 4 créditos "
           "\nc) Intro. a la Ciencia de la computacion ---------> vale 4 créditos \nd) Desafios Globales ---------> vale 3 créditos \ne) Lab. de Comunicacion I ---------> vale 3 créditos \nf) Quimica General ---------> vale 3 créditos \ng) Quimica Experimental ---------> vale 3 créditos "
           "\nh) Matematica II ---------> vale 4 créditos \ni) Fisica II ---------> vale 4 créditos \nj) Ciencias de los Materiales ---------> vale 4 créditos \nk) Programación Orientada a Objetos ---------> vale 4 créditos \nl) Lab. de Comunicación II ---------> vale 3 créditos "
           "\nm) Ingles I ---------> vale 3 créditos \nn) Proyecto Interdisciplinario I ---------> vale 2 créditos \no) Intro. al Desarrollo de Empresas ---------> vale 2 créditos \np) Matematica III ---------> vale 4 créditos \nq) Termodinamica ---------> vale 4 créditos "
           "\nr) Estadistica y Probabilidades ---------> vale 4 créditos \ns) Ingles II ---------> vale 3 créditos \nt) Gestion de Empresas ---------> vale 2 créditos \nu) Proyecto Interdisciplinario II ---------> vale 2 créditos"]

cubi = [">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n -------------------------------------------------------------------------------------------------- \n Cubiculos: \t    \t    \t  Horarios: "
        "\nI) E800------------------------> 11:00am a 1:00pm - 1:00pm a 3:00pm - 3:00pm a 5:00pm"
        "\nII) E801------------------------> 10:00am a 12:00pm - 12:00pm a 2:00pm - 2:00pm a 4:00pm - 4:00pm a 6:00pm"
        "\nIII) E802------------------------> 11:00pm a 1:00pm - 1:00pm a 3:00pm - 3:00pm a 5:00pm"
        "\nIV) E803------------------------> 9:00am a 11:00am - 11:00am a 1:00pm - 1:00pm a 3:00pm - 3:00pm a 5:00pm"
        "\nV) E804------------------------> 10:00am a 12:00pm - 12:00pm a 2:00pm - 2:00pm a 4:00pm - 4:00pm a 6:00pm"
        "\nVI) E805------------------------> 9:00am a 11:00am - 11:00am a 1:00pm - 1:00pm a 3:00pm - 3:00pm 5:00pm"
        "\nVII) E806------------------------> 10:00am a 12:00pm - 12:00pm a 2:00pm - 2:00pm a 4:00pm - 4:00pm a 6:00pm"
        "\nVIII) E807------------------------> 11:00pm a 1:00pm - 1:00pm a 3:00pm - 3:00pm a 5:00pm"
        "\nIX) E808------------------------> 9:00am a 11:00am - 11:00am a 1:00pm - 1:00pm a 3:00pm a 5:00pm\n >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n --------------------------------------------------------------------------------------------------"]

print("-----------Welcome to UTEC------------")
print(time.strftime("%d/%m/%y %H:%M"))
print("\n¡¡QUE TAL FUTURO INGENIERO DE UTEC!!\nCOMENZEMOS...\n¿Que accion quiere realizar?\n1. Registrarse \t   2. Iniciar Sesión")
var1 = input("-->", )
if var1 == "1":
    nomb = input("Para registrarse, por favor ingrese los siguientes datos:\n>> Nombre: ")
    print(registrar())
elif var1 == "2":
    nomb = input("Ingresa tu nombre de usuario: ")
    print(iniciar_sesion())
