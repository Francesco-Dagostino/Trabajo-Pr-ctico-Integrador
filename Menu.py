# Campagnaro Thiago - Dagostino Francesco 
import Clases as C

# ---------------------------------------------  MENU  ---------------------------------------------------------

def menu():
    while True:
        print("\nMenú Principal\n")
        print("1. Ingresar como alumno")
        print("2. Ingresar como profesor")
        print("3. Ver cursos")
        print("4. Salir")
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
                    print("2. Ver cursos matriculados")
                    print("3. Volver al menú principal")
                    sub_opcion = input("Seleccione una opción: ")

                    if sub_opcion == "1":
                        if len(C.cursos_disponibles) > 0:
                            print("\n1 Programación I")
                            print("2 Programación II")
                            print("3 Laboratorio II")
                            print("4 Ingles I")
                            print("5 Ingles II\n")
                            sub_opcion2 = input("Seleccione un curso: ")
                            if sub_opcion2 == "1":
                                C.Usuario1.matricular_en_curso(C.cursos_disponibles[0])
                            if sub_opcion2 == "2":
                                C.Usuario1.matricular_en_curso(C.cursos_disponibles[1])
                            if sub_opcion2 == "3":
                                C.Usuario1.matricular_en_curso(C.cursos_disponibles[2])
                            if sub_opcion2 == "4":
                                C.Usuario1.matricular_en_curso(C.cursos_disponibles[3])
                            if sub_opcion2 == "5":
                                C.Usuario1.matricular_en_curso(C.cursos_disponibles[4])
                            else:
                                print("\nSeleccione una opcion correcta\n")
                        else:
                            print("\nTodavia no hay ningun curso dado de alta\n")
                    elif sub_opcion == "2":
                        if len(C.cursos_disponibles) > 0:
                            cont = 0
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
                    elif sub_opcion == "3":
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
                            C.Usuario2.dictar_curso(nuevo_curso)
                            print(f"Curso dado de alta: {nuevo_curso._nombre_Curso}")
                            print(
                                f"Contraseña de matriculación: {nuevo_curso._contrasenia_matriculacion}"
                            )
                        else:
                            print(
                                "\nEsta materia no esta en la carrera | Volviendo al menu.."
                            )
                    elif sub_opcion == "2":
                        cont = 0
                        for i in C.Usuario2.mis_cursos:
                            cont = cont + 1
                            print(f"{cont} {i}")
                    elif sub_opcion == "3":
                        break
                    else:
                        print("\nSeleccione una opcion correcta\n")
            else:
                print("\nEmail no registrado, debe de darse de alta en el alumnado\n")
                
                
        elif opcion == "3":
            lista_ordenada = sorted(C.cursos_de_la_carrera, key=lambda x: x["Materia"])
            for diccionario in lista_ordenada:
                print(diccionario)
                
        elif opcion == "4": 
            print("\nHasta luego!") 
            print("Cerrando el sitema......\n")
            break     
            
menu()              

