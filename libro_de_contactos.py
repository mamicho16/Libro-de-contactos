#Instituto Tecnológico de Costa Rica
#Escuela de Computación
#Campus Tecnológico Central Cartago

#IC-1803 Taller de programación
#Prof. William Mata Rodriguez
#Programa #1
#LIBRO DE CONTACTOS

#Realizado por Greivin Mauricio Fernández Brizuela C.2022437510


#######################################################################
# MÓDULOS                                                             #
#######################################################################
import os
from pyisemail import is_email
import datetime
import re

#######################################################################
# FUNCIONES                                                           #
#######################################################################

#Verificar correo
def verificar_correo(correo):
    result=is_email(correo)
    if result==True:
        return True
    else:
        return False
    return 
        

# Buscar área en lista de áreas
def buscar_area(area, areas):
    if len(areas)==0:
        return False
    else:
        for info_area in areas:
            if info_area[0] == area:
                return True
        return False

# Buscar area en contactos
def area_contactos(area, contactos):
    if len(contactos)==0:
        print("NO HAY CONTACTOS, PRIMERO AGREGUE CONTACTOS")
    else:
        m=len(contactos)
        for f in range(m):
            if contactos[f][1]==area:
                return True

        return False
    return
    

# Buscar contacto en lista de contactos
def buscar_contacto(tel, area, contactos):
    if len(contactos)==0:
        return False
    m=len(contactos)
    n=len(contactos[0])
    for f in range(m):
        for c in range(n):
            if contactos[f][0]==tel and contactos[f][1]==area:
                return True
    return False
            
#Para buscar el nombre del área con respecto al código de área
def buscar_nombre_area(area, areas):
    if len(areas)==0:
        input("NO HAY ÁREAS, PRIMERO AGREGUE ÁREAS")
    else:
        for info_area in areas:
            if info_area[0] == area:
                return info_area[1]
    return

#Buscar grupos en lista grupos
def buscar_grupo(grupo, grupos):
    if len(grupos)==0:
        return False
    for i in grupos:
        if i==grupo:
            return True
    return False

#Buscar contacto en grupos
def contacto_grupos(tel, area, contactos_por_grupo):
    if len(contactos_por_grupo) == 0:
        input("NO HAY CONTACTOS EN LOS GRUPOS, PRIMERO AGREGUELOS ")
    else:
        for grupo in contactos_por_grupo:
            for contacto in grupo:
                if contacto[0]==tel and contacto[1]==area:
                    return True
        return False
    return 

#modificar nombre del area
def modificar_nombre_area(area, areas):
    if len(areas)==0:
        input("NO HAY ÁREAS, PRIMERO AGREGUE ÁREAS")
    else:
        cont=-1
        new_nombre=input("Nuevo valor del nombre del área ")
        if new_nombre == "\n":
            print("Nuevo valor " + area)
        else:
            print("Nuevo valor " + new_nombre)

        for info_area in areas:
            cont+=1
            if info_area[0] == area:
                opcion = input("\n   <A>ACEPTAR   <C>CANCELAR   OPCIÓN ")
                if opcion == "A":
                    areas[cont]=(area, new_nombre)
                    break
                elif opcion == "C":
                    break
                else:
                    input("OPCIÓN NO ES VÁLIDA ")
    return

#Validar fecha de nacimiento
def fecha_nacimiento(fecha):
    while True:
        try:
            fnacimiento=fecha
            fnacimiento=fnacimiento.split("/")
            dia=0
            mes=0
            año=0
            largo=len(fnacimiento)
            if largo == 3:
                dia=int(fnacimiento[0])
                mes=int(fnacimiento[1])
                año=int(fnacimiento[2])
                if año == 0:
                    fecha=str(dia)+"/"+str(mes)+"/"+"0000"
                else:
                    fecha=datetime.datetime.strftime(datetime.datetime(año,mes,dia), "%d/%m/%Y")
            if largo==2 or largo==1:
                fecha=0
            break
        except ValueError:
            input("Fecha invalida")
            break

# Configuración del libro de contactos
def configurar(area_por_omision, tipo_telefono_por_omision, lineas_desplegadas, areas):
    os.system("cls")
    print("LIBRO DE CONTACTOS\n")
    print("CONFIGURACIÓN DEL LIBRO DE CONTACTOS\n")
    
    # area por omisión
    while True:
        area = int(input("Área por omisión "))
        if buscar_area(area, areas) == True:
            break
        else:
            input("ESTA ÁREA NO EXISTE ")

    # tipo de teléfono por omisión     l   
    tipo = input("Tipo de teléfono por omisión (M:Móvil, C:Casa fijo, T:Trabajo, O:Otro) ")

    # cantidad de líneas desplegadas
    lineas = int(input("Cantidad de líneas desplegadas (5-30)"))
    while True:
        opcion = input("\n   <A>ACEPTAR   <C>CANCELAR   OPCIÓN ")
        if opcion == "A":
            return area, tipo, lineas
        elif opcion == "C":
            return area_por_omision, tipo_telefono_por_omision, lineas_desplegadas
        else:
            input("OPCIÓN NO ES VÁLIDA ")
    return
# Registrar áreas
def registrar_areas():
    # Menú de opciones
    while True:
        os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
        print("LIBRO DE CONTACTOS\n")
        print("REGISTRAR ÁREAS")
        print()
        print("1. Agregar áreas")
        print("2. Consultar áreas")
        print("3. Modificar áreas")
        print("4. Eliminar áreas")
        print("0. Fin")
        opcion = input("\n   OPCIÓN ")
        if opcion == "1":
            #Agregar áreas
            agregar_areas()
        elif opcion == "2":
            #Consultar áreas
            consultar_areas()
        elif opcion == "3":
            #Modificar áreas
            modificar_areas()
        elif opcion == "4":
            #Eliminar áreas
            eliminar_areas()
        elif opcion == "0":
            #Fin
            break
        else:
            input("OPCIÓN NO ES VÁLIDA, POR FAVOR ELEGIR UNA DE LAS ANTERIORES ")
            
    return

#Agregar áreas
def agregar_areas():
    while True:
        os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
        print()
        print("LIBRO DE CONTACTOS\n")
        print("REGISTRAR ÁREAS: AGREGAR\n")
        area=input("Área ")
        if area == "C":
            break
        else:
            while True:
                try:
                    area=int(area)
                    if buscar_area(area, areas) == True:
                        input ("ESTA ÁREA YA ESTÁ REGISTRADA, NO SE PUEDE AGREGAR" )
                        break
                    else:
                        nombre_area=input("Nombre del área ")
                        while True:
                            opcion = input("\n   <A>ACEPTAR   <C>CANCELAR   OPCIÓN ")
                            if opcion == "A":
                                areas.append((area,nombre_area))
                                break
                            elif opcion == "C":
                                break
                            else:
                                input("OPCIÓN NO ES VÁLIDA ")
                                break
                

                
                except ValueError:
                    input("ÁREA NO VÁLIDA, DEBE SER UN NÚMERO NATURAL")
                    break
                break
    return

#Consultar áreas
def consultar_areas():
     while True:
        os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
        print()
        print("LIBRO DE CONTACTOS\n")
        print("REGISTRAR ÁREAS: CONSULTAR\n")
        if len(areas)==0:
            print("NO HAY ÁREAS, PRIMERO AGREGUE ÁREAS")
            break
        area=input("Área ")
        if area == "C":
            break
        else:
            while True:
                try:
                    area=int(area)
                    if buscar_area(area,areas) == True:
                        print(buscar_nombre_area(area, areas))
                        while True:
                            opcion = input("\n   <A>ACEPTAR   OPCIÓN ")
                            if opcion == "A":
                                break
                            else:
                                input("OPCIÓN NO ES VÁLIDA ")
                                break
                    else:
                        input("ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE CONSULTAR ")
                        break
                except ValueError:
                        input("ÁREA NO VÁLIDA, DEBE SER UN NÚMERO NATURAL")
                        break
                break
                    
        
        

#Modificar áreas
def modificar_areas():
    while True:
        try:
            os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
            print()
            print("LIBRO DE CONTACTOS\n")
            print("REGISTRAR ÁREAS: MODIFICAR\n")
            if len(areas)==0:
                print("NO HAY ÁREAS, PRIMERO AGREGUE ÁREAS")
                break
            area=input("Área ")
            if area == "C":
                break
            else:
                area=int(area)
            if buscar_area(area,areas) == True:
                print("Nombre del área " + buscar_nombre_area(area, areas))
                modificar_nombre_area(area, areas)
            else:
                input("ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE MODIFICAR ")
        except ValueError:
            input("ÁREA NO VÁLIDA, DEBE SER UN NÚMERO NATURAL")
    return

#Eliminar área
def eliminar_areas():
    cont=-1
    while True:
        try:
            os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
            print()
            print("LIBRO DE CONTACTOS\n")
            print("REGISTRAR ÁREAS: ELIMINAR\n")
            if len(areas)==0:
                print("NO HAY ÁREAS, PRIMERO AGREGUE ÁREAS")
                break
            area=input("Área ")
            if area == "C":
                break
            else:
                area=int(area)
            if buscar_area(area,areas) == True:
                while True:
                    if area_contactos(area, contactos)==True:
                        input("ESTA ÁREA TIENE CONTACTOS REGISTRADOS, NO SE PUEDE ELIMINAR")
                        break
                    else:
                        for info_area in areas:
                            cont+=1
                            if info_area[0] == area:
                                opcion = input("\n   <A>ACEPTAR   <C>CANCELAR   OPCIÓN ")
                                if opcion == "A":
                                    del areas[cont]
                                    break
                                elif opcion == "C":
                                    break
                                else:
                                    input("OPCIÓN NO ES VÁLIDA, POR FAVOR ELEGIR UNA DE LAS ANTERIORES ")
                        break
            else:
                input("ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE ELIMINAR ")
        except ValueError:
            input("ÄREA NO VÁLIDA, DEBE SER UN NÚMERO NATURAL")
    return

# Registrar contactos
def registrar_contactos():
    # Menú de opciones
    while True:
        os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
        print("LIBRO DE CONTACTOS\n")
        print("REGISTRAR CONTACTOS")
        print()
        print("1. Agregar contactos")
        print("2. Consultar contactos")
        print("3. Modificar contactos")
        print("4. Eliminar contactos")
        print("0. Fin")
        opcion = input("\n   OPCIÓN ")
        if opcion == "1":
            #Agregar contactos
            agregar_contactos()
        elif opcion == "2":
            #Consultar contactos
            consultar_contactos()
        elif opcion == "3":
            #Modificar contactos
            modificar_contactos()
        elif opcion == "4":
            #Eliminar contactos
            eliminar_contactos()
        elif opcion == "0":
            #Fin
            break
        else:
            input("OPCIÓN NO ES VÁLIDA, POR FAVOR ELEGIR UNA DE LAS ANTERIORES ")
    return

#Agregar contactos
def agregar_contactos():
    while True:
        try:
            os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
            print()
            print("LIBRO DE CONTACTOS\n")
            print("REGISTRAR CONTACTOS: AGREGAR\n")
            tel=input("Teléfono ")
            if tel == "C":
                break
            else:
                tel=int(tel)
            if isinstance(tel, int) == True and tel > 9999 and tel < 1000000000000:
                area=input("Área ")
                if area == "":
                    area=area_por_omision
                else:
                    area=int(area)
                if buscar_contacto(tel, area, contactos) == True:
                    input("ESTE TELÉFONO YA ESTÁ REGISTRADO, NO SE PUEDE AGREGAR")
                else:
                    tp=input("Tipo de teléfono(M, C, T, O) ")
                    if tp == "":
                        tp=tipo_telefono_por_omision
                    nombre=input("Nombre ")
                    if len(nombre)>50:
                        input("El nombre no debe exceder los 50 caracteres")
                    else:
                        correo=input("Correo ")
                        if is_email(correo) == False:
                            input("El correo ingresado es inválido")
                        else:
                            df=input("Ingrese la dirección física ")
                            if len(df)>60:
                                input("La dirección física no debe exceder los 60 caracteres")
                            else:
                                fnacimiento=input("Ingrese la fecha de nacimineto (dd/mm/aaaa) ")
                                fecha_nacimiento(fnacimiento)
                                pasatiempo=input("Pasatiempos ")
                                if len(pasatiempo)>60:
                                    input("Los pasatiempos no deben exceder los 60 caracteres")
                                else:
                                    notas=input("Notas ")
                                    if len(notas)>60:
                                        input("Las notas no deben exceder los 60 caracteres")
                                    else:
                                        while True:
                                            opcion = input("\n   <A>ACEPTAR   <C>CANCELAR   OPCIÓN ")
                                            if opcion == "A":
                                                contactos.append([tel, area, tp, nombre, correo, df, fnacimiento, pasatiempo, notas])
                                                break
                                            
                                            elif opcion == "C":
                                                break
                                            else:
                                                input("OPCION NO ES VALIDA, POR FAVOR ELIJA UNA DE LAS ANTERIORES")
            else:
                input("EL TÉLEFONO DE SER UN NÚMERO NATURAL DE ENTRE 5 Y 12 DÍGITOS")                                 
        except ValueError:
            input("DATO NO VÁLIDO, DEBE SER UN NUMERO NATURAL")
    return               
#Consultar contactos
def consultar_contactos():
    while True:
        try:
            os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
            print()
            print("LIBRO DE CONTACTOS\n")
            print("REGISTRAR CONTACTOS: CONSULTAR\n")
            if len(contactos)==0:
                print("NO HAY CONTACTOS, PRIMERO AGREGUE CONTACTOS \n")
                break
            else:
                tel=input("Teléfono ")
                if tel == "C":
                    break
                else:
                    tel=int(tel)
                    area=int(input("Área "))
                    m=len(contactos)
                    n=len(contactos[0])
                    if buscar_contacto(tel,area,contactos) == True:
                        for f in range(m):
                            for c in range(n):
                                if contactos[f][0]==tel and contactos[f][1]==area:
                                    print("Tipo de teléfono " + contactos[f][2])
                                    print("Nombre " + contactos[f][3])
                                    print("Correo " + contactos[f][4])
                                    print("Dirección física " + contactos[f][5])
                                    print("Fecha de nacimiento " + contactos[f][6])
                                    print("Pasatiempos " + contactos[f][7])
                                    print("Notas " + contactos[f][8])
                                    while True:
                                        opcion = input("\n   <A>ACEPTAR   OPCIÓN ")
                                        if opcion == "A":
                                            break
                                    
                                        else:
                                            input("OPCIÓN NO ES VÁLIDA ")
                                    break
                    else:
                        print("ESTE CONTACTO NO ESTA REGISTRADO, NO SE PUEDE CONSULTAR ")
                        while True:
                            opcion = input("\n   <A>ACEPTAR   OPCIÓN ")
                            if opcion == "A":
                                break
                            else:
                                input("OPCIÓN NO ES VÁLIDA ")
        except ValueError:
            input("DATO NO VÁLIDO, DEBE SER UN NUMERO NATURAL")
    return

#Modificar contactos
def modificar_contactos():
    while True:
        try:
            os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
            print()
            print("LIBRO DE CONTACTOS\n")
            print("REGISTRAR CONTACTOS: MODIFICAR\n")
            if len(contactos)==0:
                    print("NO HAY CONTACTOS, PRIMERO AGREGUE CONTACTOS \n")
                    break
            else:
                tel=input("Teléfono ")
                if tel == "C":
                    break
                else:
                    tel=int(tel)
                    area=int(input("Área "))
                    m=len(contactos)
                    n=len(contactos[0])
                    if buscar_contacto(tel,area,contactos)==True:    
                       for f in range(m):
                            for c in range(n):
                                if contactos[f][0]==tel and contactos[f][1]==area:
                                    print("Nombre " + contactos[f][3])
                                    nombre=input("Nuevo valor ")
                                    if nombre == "":
                                        nombre=contactos[f][3]
                                    if len(nombre)>50:
                                        print("El nombre no debe exceder los 50 caracteres")
                            
                                    else:
                                        print("Correo " + contactos[f][4])
                                        correo=input("Nuevo valor ")
                                        if correo == "":
                                            correo=contactos[f][4]
                                        if is_email(correo) == False:
                                            print("El correo ingresado es inválido")
                                        else:
                                            print("Dirección física " + contactos[f][5])
                                            df=input("Nuevo valor ")
                                            if df == "":
                                                df=contactos[f][5]
                                            if len(df)>60:
                                                print("La dirección física no debe exceder los 60 caracteres")
                                    
                                            else:
                                                print("Fecha de nacimiento " + contactos[f][6])
                                                fnacimiento=input("Nuevo valor ")
                                                if fnacimiento=="":
                                                    fnacimiento=contactos[f][6]
                                                else:
                                                    fecha_nacimiento(fnacimiento)
                                                print("Pasatiempos " + contactos[f][7])
                                                pasatiempos=input("Nuevo valor ")
                                                if pasatiempos=="":
                                                    pasatiempos=contactos[f][7]
                                                if len(pasatiempos)>60:
                                                    print("Los pasatiempos no deben exceder los 60 caracteres")
                                                else:
                                                    print("Notas " + contactos[f][8])
                                                    notas=input("Nuevo valor ")
                                                    if notas =="": 
                                                        notas=contactos[f][8]
                                                    if len(notas)>60:
                                                        print("Las notas no deben exceder los 60 caracteres")
                                                    else:
                                                        while True:
                                                            opcion = input("\n   <A>ACEPTAR   <C>CANCELAR   OPCIÓN ")
                                                            if opcion == "A":
                                                                contactos[f][3]=nombre
                                                                contactos[f][4]=correo
                                                                contactos[f][5]=df
                                                                contactos[f][6]=fnacimiento
                                                                contactos[f][7]=pasatiempos
                                                                contactos[f][8]=notas
                                                                break
                                                            elif opcion == "C":
                                                                break
                                                            else:
                                                                input("OPCION NO ES VALIDA, POR FAVOR ELIJA UNA DE LAS ANTERIORES")
                                                            break
                                                        break
                                                    break
                    else:
                        input("ESTE CONTACTO NO ESTA REGISTRADO, NO SE PUEDE MODIFICAR ")
        except ValueError:
            input("DATO NO VÁLIDO, DEBE SER UN NUMERO NATURAL")
    return

#Eliminar contactos
def eliminar_contactos():
    cont=-1
    while True:
        try:
            os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
            print()
            print("LIBRO DE CONTACTOS\n")
            print("REGISTRAR CONTACTOS: ELIMINAR\n")
            if len(contactos)==0:    
                print("NO HAY CONTACTOS, PRIMERO AGREGUE CONTACTOS \n")
                break
            else:
                tel=input("Teléfono ")
                if tel == "C":
                    break
                else:
                    tel=int(tel)
                    area=int(input("Área "))
                    m=len(contactos)
                    n=len(contactos[0])
                    if buscar_contacto(tel,area,contactos)==True:    
                       for f in range(m): 
                          cont+=1
                          for c in range(n):
                          
                              if contactos[f][0]==tel and contactos[f][1]==area:
                                  
                                  print("Tipo de teléfono " + contactos[f][2])
                                  print("Nombre " + contactos[f][3])
                                  print("Correo " + contactos[f][4])
                                  print("Dirección física " + contactos[f][5])
                                  print("Fecha de nacimiento " + contactos[f][6])
                                  print("Pasatiempos " + contactos[f][7])
                                  print("Notas " + contactos[f][8])
                              
                                  while True:
                                  
                                     opcion = input("\n   <A>ACEPTAR   <C>CANCELAR   OPCIÓN ")
                                     if opcion == "A":
                                         print("Si el contacto pertenece a algún grupo este se eliminará del grupo")
                                         confirmacion=input("Los cambios son irreversibles. ¿Está seguro? (A/C)")
                                         if confirmacion == "A":
                                             del contactos[cont]
                                             for f in range(len(contactos_por_grupos)):
                                                 for c in range(len(contactos_por_grupos[f])):
                                                     if (tel, area)==contactos_por_grupos[f][c]:
                                                         del contactos_por_grupos[f][c]
                                             break
                                         elif confirmacion == "C":
                                             break
                                         else:
                                             input("OPCION NO ES VALIDA, POR FAVOR ELIJA UNA DE LAS ANTERIORES ")
                                     
                                     elif opcion == "C":
                                         break
                                     else:
                                         input("OPCION NO ES VALIDA, POR FAVOR ELIJA UNA DE LAS ANTERIORES ")

                    else:
                        input("ESTE CONTACTO NO ESTA REGISTRADO, NO SE PUEDE ELIMINAR ")
        except ValueError:
            input("DATO NO VÁLIDO, DEBE SER UN NUMERO NATURAL")
        except IndexError:
            break
    return

#Administrar grupos de contactos
def administrar_grupos_contactos():
    while True:
        os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
        print()
        print("LIBRO DE CONTACTOS\n")
        print("ADMINISTRAR GRUPOS DE CONTACTOS\n")
        print("1. Agregar grupos")
        print("2. Agregar contactos a los grupos")
        print("3. Modificar grupos")
        print("4. Eliminar grupos")
        print("5. Eliminar contactos de los grupos")
        print("0. Fin")
        opcion = input("\n   OPCIÓN ")
        if opcion == "1":
            #Agregar grupos
            agregar_grupos()
        elif opcion == "2":
            #Agregar contactos a los grupos
            agrega_contactos_grupos()
        elif opcion == "3":
            #Modificar grupos
            modificar_grupos()
        elif opcion == "4":
            #Eliminar grupos
            eliminar_grupos()
        elif opcion == "5":
            #Eliminar contactos de los grupos
            eliminar_contacto_grupo()
        elif opcion == "0":
            #Fin
            break
        else:
            input("OPCIÓN NO ES VÁLIDA, POR FAVOR ELEGIR UNA DE LAS ANTERIORES ")
    return

#Agregar grupos
def agregar_grupos():
    while True:
        os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
        print()
        print("LIBRO DE CONTACTOS\n")
        print("ADMINISTRAR GRUPOS DE CONTACTOS")
        print("Agregar grupos\n")
        grupo=input("Nombre del grupo ")
        if grupo == "C":
            break
        if buscar_grupo(grupo, grupos) == True:
            print("ESTE GRUPO YA ESTÁ REGISTRADO, NO SE PUEDE AGREGAR")
        else:
            while True:    
                opcion = input("\n   <A>ACEPTAR   <C>CANCELAR   OPCIÓN ")
                if opcion == "A":
                    grupos.append(grupo)
                    indice=grupos.index(grupo)
                    contactos_por_grupos.insert(indice, [])
                    break
                elif opcion == "C":
                    break
                else:
                    input("OPCION NO ES VALIDA, POR FAVOR ELIJA UNA DE LAS ANTERIORES")
    return

#Agrega contactos a los grupos
def agrega_contactos_grupos():
    while True:
        os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
        print()
        print("LIBRO DE CONTACTOS\n")
        print("ADMINISTRAR GRUPOS DE CONTACTOS")
        print("Agregar contactos a los grupos\n")
        if len(grupos)==0:
            print("NO HAY GRUPOS REGISTRADOS, PRIMERO AGREGUE GRUPOS ")
            break
        else:
            grupo=input("Nombre del grupo ")
            print()
            if grupo == "C":
                break
            if buscar_grupo(grupo,grupos)==True:
                indice=grupos.index(grupo)
                tel=int(input("Telefono "))
                area=int(input("Área "))
                if buscar_contacto(tel,area,contactos)==True:
                    if contacto_grupos(tel, area, contactos_por_grupos) == True:
                        print("ESTE CONTACTO YA ESTÁ EN EL GRUPO, AGREGUE OTRO CONTACTO")
                    else:
                        m=len(contactos)
                        n=len(contactos[0])
                        for f in range(m):
                            for c in range(n):
                                if contactos[f][0]==tel and contactos[f][1]==area:
                                    print ("Nombre del contacto " + str(contactos[f][3]))
                                    while True:    
                                        opcion = input("\n   <A>ACEPTAR   <C>CANCELAR   OPCIÓN ")
                                        if opcion == "A":
                                            contactos_por_grupos[indice].append((tel, area))
                                            break
                                        elif opcion == "C":
                                            break
                                        else:
                                            input("OPCION NO ES VALIDA, POR FAVOR ELIJA UNA DE LAS ANTERIORES")

                                    break
                                else:
                                    pass
                else:
                    input("ESTE CONTACTO NO EXISTE, NO PUEDE AGREGARLO AL GRUPO")
            else:
                input("ESTE GRUPO NO EXISTE, NO PUEDE AGREGARLE CONTACTOS ")
    return

#Modificar grupos
def modificar_grupos():
    while True:
        try:
            os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
            print()
            print("LIBRO DE CONTACTOS\n")
            print("ADMINISTRAR GRUPOS DE CONTACTOS")
            print("Modificar grupos\n")
            if len(grupos)==0:
                print("NO HAY GRUPOS REGISTRADOS, PRIMERO AGREGUE GRUPOS ")
                break
            else:
                grupo=input("Nombre del grupo ")
                print()
                if grupo == "C":
                    break
                if buscar_grupo(grupo,grupos)==True:
                    new_grupo=input("Nuevo valor ")
                    if new_grupo=="":
                        new_grupo=grupo
                        print("Nuevo valor ", new_grupo)

                    else:
                        print("Nuevo valor ", new_grupo)
                        if buscar_grupo(new_grupo, grupos)==True:
                            print("GRUPO YA EXISTE, EN CASO DE ACEPTAR LA OPERACIÓN LOS CONTACTOS SE LE AGREGARÁN")
                            while True:    
                                opcion = input("\n   <A>ACEPTAR   <C>CANCELAR   OPCIÓN ")
                                if opcion == "A":
                                    indice=grupos.index(new_grupo)
                                    indice2=grupos.index(grupo)
                                    for contacto in contactos_por_grupos[indice2]:
                                        if contacto_grupos(contacto[0], contacto[1], contactos_por_grupos[indice])==True:
                                            del contacto
                                        else:
                                            if contactos_por_grupos[indice2]==[]:
                                                pass
                                            else:
                                                contactos_por_grupos[indice].append(contacto)         
                                    del grupos[indice2]
                                    del contactos_por_grupos[indice2]
                                    break
                                elif opcion == "C":
                                    break
                                else:
                                    input("OPCION NO ES VALIDA, POR FAVOR ELIJA UNA DE LAS ANTERIORES")

                        else:
                            while True:    
                                opcion = input("\n   <A>ACEPTAR   <C>CANCELAR   OPCIÓN ")
                                if opcion == "A":
                                    indice3=grupos.index(grupo)
                                    grupos[indice3]=new_grupo
                                    break
                                elif opcion == "C":
                                    break
                                else:
                                    input("OPCION NO ES VALIDA, POR FAVOR ELIJA UNA DE LAS ANTERIORES")

                else:
                    input("GRUPO NO ESTÁ REGISTRADO, NO SE PUEDE MODIFICAR")
        except:
            pass
    return

#Eliminar grupos
def eliminar_grupos():
    while True:
        try:
            os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
            print()
            print("LIBRO DE CONTACTOS\n")
            print("ADMINISTRAR GRUPOS DE CONTACTOS")
            print("Eliminar grupos\n")
            if len(grupos)==0:
                print("NO HAY GRUPOS REGISTRADOS, PRIMERO AGREGUE GRUPOS ")
                break
            else:
                grupo=input("Nombre del grupo ")
                print()
                if grupo == "C":
                    break
                if buscar_grupo(grupo,grupos)==True:
                    indice=grupos.index(grupo)
                    while True:    
                        opcion = input("\n   <A>ACEPTAR   <C>CANCELAR   OPCIÓN ")
                        if opcion == "A":
                            confirmacion=input("Los cambios son irreversibles. ¿Está seguro? (A/C)")
                            if confirmacion == "A":
                                 del grupos[indice]
                                 del contactos_por_grupos[indice]
                                 break
                            elif confirmacion == "C":
                                 break
                            else:
                                 input("OPCION NO ES VALIDA, POR FAVOR ELIJA UNA DE LAS ANTERIORES ")
                        elif opcion == "C":
                            break
                        else:
                            input("OPCION NO ES VALIDA, POR FAVOR ELIJA UNA DE LAS ANTERIORES")
                else:
                    input("GRUPO NO ESTÁ REGISTRADO, NO SE PUEDE MODIFICAR")
        except:
            pass
    return

#Eliminar contactos de los grupos
def eliminar_contacto_grupo():
    while True:
        m = len(contactos)
        n = len(contactos[0])
        os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
        print()
        print("LIBRO DE CONTACTOS\n")
        print("ADMINISTRAR GRUPOS DE CONTACTOS")
        print("Eliminar contactos de los grupos\n")
        if len(grupos)==0:
            print("NO HAY GRUPOS REGISTRADOS, PRIMERO AGREGUE GRUPOS ")
            break
        else:
            grupo=input("Nombre del grupo ")
            print()
            if grupo == "C":
                break
            if buscar_grupo(grupo,grupos)==True:
                indice=grupos.index(grupo)
                while True:
                    try:
                        tel=int(input("Teléfono "))
                        area=int(input("Área "))
                        if contacto_grupos(tel, area, contactos_por_grupos)==True:
                            for f in range(m):
                                for c in range(n):
                                    if contactos[f][0]==tel and contactos[f][1]==area:
                                        print("Nombre ", contactos[f][3])
                                        while True:    
                                            opcion = input("\n   <A>ACEPTAR   <C>CANCELAR   OPCIÓN ")
                                            if opcion == "A":
                                                confirmacion=input("Los cambios son irreversibles. ¿Está seguro? (A/C)")
                                                if confirmacion == "A":
                                                    del contactos_por_grupos[indice][f]
                                                    break
                                                elif confirmacion == "C":
                                                    break
                                                else:
                                                    input("OPCION NO ES VALIDA, POR FAVOR ELIJA UNA DE LAS ANTERIORES ")
                                            elif opcion == "C":
                                                break
                                            else:
                                                input("OPCION NO ES VALIDA, POR FAVOR ELIJA UNA DE LAS ANTERIORES")
                                    break
                                break
                        else:
                            input("ESTE CONTACTO NO EXISTE EN EL GRUPO, NO PUEDE ELIMINARLO")
                        break
                    except ValueError:
                        input("DATO INVÁLIDO, DEBE SER UN NÚMERO NATURAL")
            else:
                input("ESTE GRUPO NO EXISTE, NO PUEDE ELIMINARLE CONTACTOS")
    return

#Consultar contactos
def consultar():
    while True:
        try:
            if len(contactos)==0:
                input("NO HAY CONTACTOS, PRIMERO AGREGUE CONTACTOS")
            m=len(contactos)
            n=len(contactos[0])
            os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
            print()
            print("LIBRO DE CONTACTOS\n")
            print("CONSULTAR CONTACTOS\n")
            print("FILTROS: ")
            nombre=input("Nombre contacto ")
            if nombre == "C":
                break
            tel=input("Teléfono ")
            area=input("Área ")
            fnacimiento=input("Fecha de nacimiento ")
            pasatiempos=input("Pasatiempos ")
            grupo=input("Grupo ")
            
            print()
            print(busqueda(nombre,tel, area, fnacimiento,pasatiempos,grupo))
            
        except:
            break
    return
            
            

def busqueda(nombre,numero,area,fecha,pasatiempo,grupo):

    # primer filtro "mas importante, el más complejo"
    #lista de usuarios encontrados por grupo
    listaEncontradaPorGrupo = []
    for i in grupos:
        if i.lower()==grupo.lower():
            grupo=i
    
    if grupo != "":
        # lista de numeros
        numeros = contactos_por_grupos[grupos.index(grupo)]
        for contacto in contactos:
            if (contacto[0],contacto[1]) in numeros:
                listaEncontradaPorGrupo+=[contacto]
                
    if listaEncontradaPorGrupo != []:
        return busqueda_aux(listaEncontradaPorGrupo,[nombre,numero,area,fecha,pasatiempo])
    else:
        return busqueda_aux(contactos,[nombre,numero,area,fecha,pasatiempo])

# parametros = ["mauricio%","2%222","506%","22/04/22"]
def busqueda_aux(contactos,parametros):
    resultado = []
    cont=0
    new_contactos=[]
    for contacto in contactos:
        new_contactos.append([contacto[3],contacto[0],contacto[1],contacto[6],contacto[7]])
        
    for contacto in new_contactos:
        comparacion = []
        for p in range(len(parametros)):


            #verificando si el parametro es vacio
            if parametros[p] ==  "":
                comparacion += [contacto]
            else:
                
            # creando los 5 casos posibles
            
        
                # caso 1 , busqueda sin %
                if "%" not in parametros[p]:
                    if parametros[p].lower() == str(contacto[p]).lower():
                        comparacion += [contacto]
                    
                        
                    
                # los otros 4 casos
                else:
                    num_porcentaje = parametros[p].count("%")
                    if num_porcentaje == 1:
                        # caso "%case"
                        if parametros[p].index("%") == 0:
                            listn = parametros[p].replace("%","").lower().split(" ")[::-1]
                            n = len(listn)
                            data = str(contacto[p]).lower().split(" ")[::-1]
                            nd = len(data)
                            if nd >= n:
                                flag = True
                                for i in range(n):
                                    if data[i] != listn[i]:
                                        flag = False
                                if flag:
                                    comparacion += [contacto]
                                
                                
                        # caso "case%"
                        elif parametros[p].index("%") == [len(parametros[p])-1]:
                            listn = parametros[p].replace("%","").lower().split(" ")
                            n = len(listn)
                            data = str(contacto[p]).lower().split(" ")
                            nd = len(data)
                            if nd >= n:
                                flag = True
                                for i in range(n):
                                    if data[i] != listn[i]:
                                        flag = False
                                if flag:
                                    comparacion += [contacto]
                        # caso "hola % adios"
                        else:
                            data = parametros[p].lower().split("%")
                            flag = True
                            for d in data:
                                if d not in str(contacto[p]).lower():
                                    flag = False
                            if flag:
                                comparacion += [contacto]
                    elif num_porcentaje == 2:
                        # caso "%asdsad%"
                        if parametros[p].index("%") == parametros[p][::-1].index("%") == 0:
                            data = parametros[p].replace("%","").lower()
                            if data in str(contacto[p]):
                                comparacion += [contacto]
                            
                        # caso "%asd % asd" o "asda % as%"
                        else:
                            index1 = parametros[p].index("%")
                            index2 = parametros[p].index("%",index1+1,len(parametros[p])-1)
                            data = parametros[p][index1+1,index2]
                            if data in str(contacto[p]):
                                comparacion += [contacto]
                            
        if len(comparacion) == 5:
            resultado += [comparacion[0]]
            

    for x in resultado:
        print(x[0], x[1], x[2], x[3], x[4])
        cont+=1
        if cont == lineas_desplegadas:
            input("\n      OPCION     <A>  ")
            cont=0
        else:
            pass
    return

    

#Ayuda
def ayuda():
    os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
    print("                                                                  Libro de contactos")
    print("                                                                       Versión: 1.00")
    print("                                                       Creado el 10 de abril de 2022")
    print("                                     Creado por: Greivin Mauricio Fernández Brizuela")
    print()
    print("                          Características generales")
    print()
    print("Este programa está hecho en la aplicación Python, por lo que para correr el programa")
    print("necesitará la misma para poder utilizarlo. En general el programa es una lista de c-")
    print("ontactos, en la cual puede configurar su lista (área por omisión, tipo de teléfono y")
    print("las líneas a desplegar), agregar áreas (agregar, consultar, modificar y eliminar),  ")
    print("agregar contactos (agregar, consultar, modificar y eliminar), administrar grupos de ")
    print("contactos (agregar grupos, agregar contactos a los grupos, modificar grupos, eliminar")
    print("grupos, eliminar contactos en los grupos) y consultar contactos.")
    print()
    print("1.	Configuración del libro de contactos")
    print("Esta opción define el área por omisión y el tipo de teléfono por omisión, es decir al")
    print("agregar contactos si no introduce ningún valor el programa asume que se trata de esta")
    print("área y ese tipo. Además, solicita la cantidad de líneas a desplegar para la opción de")
    print("consultar contactos.")
    print()
    print("2.	Registrar áreas")
    print("Esta opción cuenta con 4 opciones:")
    print("1. Agregar áreas: esta opción agrega áreas a la lista de áreas junto al nombre del")
    print("área y valida que esta área no esté en la lista.")
    print("2. Consultar áreas: esta opción localiza el área e imprime su nombre.")
    print("3. Modificar áreas: esta opción cambia el nombre del área introducida.")
    print("4. Eliminar áreas: esta opción elimina áreas siempre y cuando no tenga contactos re-")
    print("gistrados con este nombre.")
    print()
    print("3.	Registrar contactos")
    print("Esta opción cuenta con 4 opciones:")
    print("1. Agregar contactos: agrega contactos a la lista de contactos siempre y cuando el")
    print("número no exista.")
    print("2. Consultar contactos: despliega los datos del contacto solicitado.")
    print("3. Modificar contactos: despliega los datos y pregunta por su nuevo valor, de que-")
    print("rer dejar el mismo valor se deja el espacio en blanco.")
    print("4. Eliminar contactos: solicita el número del contacto a eliminar y si existe soli")
    print("cita al usuario si borrarlo o no.")
    print()
    print("4.	Administrar grupos de contactos")
    print("Esta opción cuenta con 5 opciones:")
    print("1. Agregar grupos: solicita el nombre del grupo a crear, si el grupo ya existe no")
    print("lo crea.")
    print("2. Agregar contactos a los grupos: solicita el grupo y el teléfono del contacto a")
    print("agregar.")
    print("3. Modificar grupos: cambia el nombre del grupo, si ya existe añade los contactos")
    print("al grupo.")
    print("4. Eliminar grupos: elimina el grupo y los contactos que tiene el grupo.")
    print("5. Eliminar contactos de los grupos: solicita el nombre del grupo y el teléfono a")
    print("eliminar.")
    print()
    print("5.	Consultar contactos")
    print("Esta opción busca contactos dependiendo de filtros, además se usa % para represen-")
    print("tar si antes, después, las dos o en medio hay otros caracteres.")
    print("Muestra los contactos dependiendo de los filtros seleccionados")
    print()
    print("6.	Ayuda")
    print("Se despliega este manual de usuario.")
    print()
    print("7.	Acerca de")
    print("Se despliegan los datos del programa.")
    print()
    print("Pasos para utilizar el programa")
    print("1. Se debe agregar mínimo un área para poder utilizar las otras opciones.")
    print("2. Se debe realizar la configuración de la lista de contactos.")
    print("3. Se deben agregar contactos.")
    print("4. Se pueden crear grupos.")
    print("5. Todas las opciones ya están habilitadas.")
    print("6. Para salirse de alguna opción se debe ingresar una C.")
    input("Estos son los pasos generales para usar correctamente la lista de contactos.")
    return

#Acerca de
def acerca_de():
    os.system("cls")
    print("Libro de contactos")
    print("Versión: 1.00")
    print("Creado el 10 de abril de 2022")
    input("Creado por: Greivin Mauricio Fernández Brizuela")
    return
    
#######################################################################
# PROGRAMA PRINCIPAL                                                  #
#######################################################################

# lista de areas
areas = []

#lista de contactos
contactos=[]

#lista de grupos
grupos=[]

#lista de contactos por grupos
contactos_por_grupos=[]

# datos de la configuración
area_por_omision = 0
tipo_telefono_por_omision = ""
lineas_desplegadas = 0


while True:
    os.system("cls") # cls: clear screen (borra pantalla)-funciona ejecutando el programa fuera del IDE
    print()
    print("LIBRO DE CONTACTOS\n")
    print("1. Configuración del libro de contactos")
    print("2. Registrar áreas")
    print("3. Registrar contactos")
    print("4. Administrar grupos de contactos")
    print("5. Consultar contactos")
    print("6. Ayuda")
    print("7. Acerca de")
    print("0. Fin")
    opcion = input("\n   OPCIÓN ")
    if opcion == "1":
        # Configuración del libro de contactos
        area_por_omision, tipo_telefono_por_omision, lineas_desplegadas = configurar(area_por_omision, tipo_telefono_por_omision, lineas_desplegadas, areas)
    elif opcion == "2":
        # Registrar áreas
        registrar_areas()
    elif opcion == "3":
        #Registrar contactos
        registrar_contactos()
    elif opcion == "4":
        #Administrar grupos de contactos
        administrar_grupos_contactos()
    elif opcion == "5":
        #Consultar contactos
        consultar()
    elif opcion == "6":
        #Ayuda
        ayuda()
    elif opcion == "7":
        #Acerca de
        acerca_de()
    elif opcion == "0":
        break
        #Fin del programa
    else:
        input("OPCIÓN NO ES VÁLIDA, POR FAVOR ELEGIR UNA DE LAS ANTERIORES ")
print("FIN DEL PROGRAMA")

