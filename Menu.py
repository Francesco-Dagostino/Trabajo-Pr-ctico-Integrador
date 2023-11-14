# Campagnaro Thiago - Dagostino Francesco 
import Clases as C
# Importas la clase y la renombras con as "c"

# ---------------------------------------------  MENU  ---------------------------------------------------------
def menu():
    while True:
        print("\nMenú Principal")
        print("-------------------------")
        print("1. Ingresar como alumno")
        print("2. Ingresar como profesor")
        print("3. Ver cursos")
        print("4. Salir")
        print("-------------------------")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            email_a_validar = str(input("Ingrese su mail: "))
            contrasenia_a_validar = str(input("Ingrese su contraseña: "))
            validacion = C.Estudiante.validar_credenciales(
                email_a_validar, contrasenia_a_validar
            )
            if validacion == True:
                # ------------------------ MENU ALUMNO ---------------------------
                print("\nAcceso Exitoso")
                while True:
                    print("\nSub menú alumno")
                    print("1. Matricularse a un curso")
                    print("2. Desmatricularse a un curso")
                    print("3. Ver cursos matriculados")
                    print("4. Volver al menú principal\n")
                    sub_opcion = input("Ingrese una opción: ")

                    if sub_opcion == "1":
                        if len(C.cursos_disponibles) > 0:
                            print("\n Programación I")
                            print(" Programación II")
                            print(" Laboratorio II")
                            print(" Ingles I")
                            print(" Ingles II\n")
                            sub_opcion2 = input("Ingrese por teclado el número (según el orden en el que registro el dictado del profesor, es decir, 1...2...3): ")
                            if sub_opcion2 == "1":
                                C.Usuario1.matricular_en_curso(C.cursos_disponibles[0])
                            elif sub_opcion2 == "2":
                                C.Usuario1.matricular_en_curso(C.cursos_disponibles[1])
                            elif sub_opcion2 == "3":
                                C.Usuario1.matricular_en_curso(C.cursos_disponibles[2])
                            elif sub_opcion2 == "4":
                                C.Usuario1.matricular_en_curso(C.cursos_disponibles[3])
                            elif sub_opcion2 == "5":
                                C.Usuario1.matricular_en_curso(C.cursos_disponibles[4])
                            else:
                                print("\nSeleccione una opcion correcta\n")
                        else:
                            print("\nTodavia no hay ningun curso dado de alta\n")
                            
                    elif sub_opcion == "2":
                        print("Desmatriculación!!") 
                        if len(C.Usuario1.mis_cursos) > 0: #Se está comprobando si la longitud de la lista C.Usuario1.mis_cursos es mayor que cero. 
                            for i, curso in enumerate(C.Usuario1.mis_cursos, 1):  #Al usar enumerate con un segundo argumento de 1, el primer valor de i será 1, el segundo será 2, y así sucesivamente
                                print(f"{i}. {curso._nombre_Curso}")              #1 se utiliza para indicar que el contador i debe comenzar desde 1 en lugar de 0 al enumerar los elementos
                            sub_opcion2 = input("Ingrese el número del curso para desmatricularse: ")
                            try:
                                sub_opcion2 = int(sub_opcion2)
                                if 1 <= sub_opcion2 <= len(C.Usuario1.mis_cursos):
                                        curso_a_desmatricular = C.Usuario1.mis_cursos[sub_opcion2 - 1]
                                        C.Usuario1.desmatricular_de_curso(curso_a_desmatricular)
                                else:
                                    print("Número de curso no válido.")
                            except ValueError:
                                print("Ingrese un número válido.")
                        else:
                            print("No estás matriculado en ningún curso.")
                       
                        
                    elif sub_opcion == "3":
                        if len(C.cursos_disponibles) > 0: #El len verifica si hay cursos disponibles para mostrar. 
                            cont = 0                      #contador se usa para numerar los cursos cuando se imprimen más adelante.
                            for i in C.Usuario1.mis_cursos:
                                cont = cont + 1
                                print(f"\n{cont} {i}")
                            sub_opcion3 = int(
                                input("Ingrese numero de la materia para verla: ")
                            )
                            if sub_opcion3 == cont:
                                print(i)
                                print("tpi.pdf")
                                print("practica1.pdf")
                        else:
                            print("\nNo hay cursos dados de alta\n")
                    elif sub_opcion == "4":
                        break
                    else:
                        print("\nSeleccione una opcion correcta\n")
            else:
                print("\nEmail no registrado, debe de darse de alta en el alumnado\n")
                
                
        elif opcion == "2":
            email_a_validar = str(input("Ingrese su mail: "))
            contrasenia_a_validar = str(input("ingrese su contraseña: "))
            validacion = C.Profesor.validar_credenciales(
                email_a_validar, contrasenia_a_validar
            )
            if validacion == True:
                #---------------------- MENU PROFESOR ---------------------------------------
                
                print("\nAcceso exitoso como Profesor")
                while True:
                    print("\nSub menú Profesor")
                    print("1. Dictar curso")
                    print("2. Ver cursos")
                    print("3. Volver al menú principal")
                    sub_opcion = input("\nSeleccione una opción: ")

                    if sub_opcion == "1":
                        nombre_curso = input(
                            "Ingrese el nombre del curso a dictar(Ingrese la primer letra en mayuscula): "
                        )
                        if (
                            nombre_curso == "Ingles I"
                            or nombre_curso == "Ingles II"
                            or nombre_curso == "Laboratorio I"
                            or nombre_curso == "Laboratorio II"
                            or nombre_curso == "Programacion I"
                            or nombre_curso == "Programacion II"
                        ):
                            nuevo_curso = C.Curso(nombre_curso)
                            C.cursos_disponibles.append(nuevo_curso)
                            C.Usuario2.dictar_curso(nuevo_curso)  #llama a la funcion para crear contraseña. 
                            print(f"Curso dado de alta: {nuevo_curso._nombre_Curso}")
                            print(
                                f"Contraseña de matriculación: {nuevo_curso._contrasenia_matriculacion}"
                            )
                        else:
                            print(
                                "\nEsta materia no esta en la carrera | Volviendo al menu.."
                            )
                    elif sub_opcion == "2":
                        print("\nCursos disponibles:")
                        if len(C.cursos_disponibles) > 0:
                            for i, curso in enumerate(C.cursos_disponibles): #verifica curso disponibles.
                                print(f"{i + 1}. {curso._nombre_Curso}")
                                curso_seleccionado = input("Seleccione un curso para ver información detallada (ingrese el número): ")
                            try:
                                curso_seleccionado = int(curso_seleccionado)
                                if 1 <= curso_seleccionado <= len(C.cursos_disponibles):
                                    curso = C.cursos_disponibles[curso_seleccionado - 1]
                                    print(f"\nInformación del curso:")
                                    print(f"Nombre: {curso._nombre_Curso}")
                                    print(f"Código: {curso._codigo}")
                                    print(f"Contraseña de matriculación: {curso._contrasenia_matriculacion}")
                                    print(f"Cantidad de archivos: {len(curso.listar_archivos())}")
                                    agregar_archivo = input("\nDesea agregar algun archivo nuevo (si/no): ")
                                    if agregar_archivo == "si" or agregar_archivo == "sí":
                                        nombre_archivo = input("Ingrese el nombre del archivo: ")
                                        formato_archivo = input("Ingrese el formato del archivo: ")
                                        curso.agregar_archivo(nombre_archivo, formato_archivo)  
                                    else: 
                                        print("\nVolviendo al menu ")    
                                else:
                                    print("Número de curso no válido.")
                            except ValueError:
                                print("Ingrese un número válido.")
                        else:
                            print("No hay cursos disponibles.")   
                       
                    elif sub_opcion == "3":
                        break
                    else:
                        print("\nSeleccione una opcion correcta\n")
            else:
                print("\nEmail no registrado, debe de darse de alta en el alumnado\n")
                
                
        elif opcion == "3":
            lista_ordenada = sorted(C.cursos_de_la_carrera, key=lambda x: x["Materia"]) #Usa la clave "Materia" para ordenar. 
            for diccionario in lista_ordenada:   #Itera sobre cada diccionario en la lista ordenada.
                print(diccionario)            #La función sorted se utiliza con una función lambda como argumento key, que especifica cómo debe ordenarse la lista.
                
        elif opcion == "4": 
            print("\nHasta luego!") 
            print("Cerrando el sitema......\n")
            break              
        
        
menu()              
