# Campagnaro Thiago - Dagostino Francesco 
from clases import Estudiante,Profesor,Curso
from contraseña import contrasenia_aleatoria

#----------------------------------------------------------------------------------------------------------------- 
   
estudiante1 = Estudiante ("1000", 2023, "Fran", "Dagostino", "alum1@gmail.com", "1234")
Estudiante.estudiantes.append(estudiante1)
estudiante2 = Estudiante ("1001", 2023, "Raul", "Perez", "alum2@gmail.com", "5678")
Estudiante.estudiantes.append(estudiante2)

profesor1 = Profesor ("Ingeniero civil", 2017, "Alberto", "Gonzalez", "profe1@gmail.com", "1234")
Profesor.profesores.append(profesor1)
profesor2 = Profesor ("Programador", 2010, "Jose", "Matuid", "profe2@gmail.com", "5678")
Profesor.profesores.append(profesor2)   


# -----------------------------------------------  Menu   ---------------------------------------------------------------

opcion = 0
while opcion != 4:
    print("Menu:")
    print("1- Ingresar cómo alumno")
    print("2- Ingresar cómo profesor")
    print("3- Ver cursos")
    print("4- Salir\n")
    
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        email = str(input("Ingrese el mail: "))
        contrasenia = str(input("Ingrese su contraseña: "))
        email_encontrado = False
        contrasenia_encontrada = False
        for e in Estudiante.estudiantes:
            if email == e.email:
                if e.validar_credenciales(email, contrasenia) == True:
                    print("\nSu acceso fue exitoso")
                    contrasenia_encontrada = True
                    
                    #----------------------------------- SUBMENU ALUMNO: -------------------------------------
                    sub_opcion = 0
                    while sub_opcion != 3:
                        print("\n1. Matricularse a un curso")
                        print("2. Ver curso") 
                        print("3. Volver al menu principal")
                        sub_opcion = int(input("Ingrese una opcion: "))
                        if sub_opcion == 1:
                            mis_cursos = Curso.cursos
                            #for para mostar cursos
                            print("\nCursos disponibles:")
                            for curso in Curso.cursos:
                                print(curso)
                            while True:
                                seleccion = input("\nIngrese la contraseña de matriculacion del curso al que desea inscribirse (o 'n' para salir): ")
                                if seleccion == 'n':
                                    break
                                elif seleccion == "n001" or seleccion == "n002" or seleccion == "n003" or seleccion == "n004" or seleccion == "n005" or seleccion == "n006":
                                    Curso.cursos.append(mis_cursos)    

                        elif sub_opcion == 2:
                            print("\nCursos en los que te inscribiste:")
                            print(mis_cursos)
                                
                        else:
                            print("\nLista de curso (seleccione el curso en que esta matriculado): \n")
                            print("1 Programación I")
                            print("2 Programación II")
                            print("3 Laboratorio II")
                            print("4 Ingles I")
                            print("5 Ingles II\n")
                            elegir = input("Eliga la materia: ")
                            if elegir == "1":
                              print("\nProgramacion I \ntpi.pdf\npractica1.pdf...\n")
                            elif elegir == "2":
                              print("\nLaboratorio I\ntpi.pdf\npractica 1...\n") 
                            elif elegir == "3":
                               print("\nLaboratorio II\ntpi.pdf\npractica 1...\n")  
                            elif elegir == "4":
                              print("\nIngles I\ntpi.pdf\npractica 1...\n") 
                            elif elegir == "5":
                              print("\nIngles II\ntpi.pdf\npractica 1...\n") 
                            else:
                             break 
                            print("\nVolviendo al menu principal.....\n") 
                            
                    
                if contrasenia_encontrada == False:
                    "Contraseña incorrecta"
                email_encontrado = True       
        if email_encontrado == False:
            print("Email inexistete. Comunicarse con alumnado")
                           
            
    elif opcion == 2:
        print("Ingresando como Profesor...")
        email = str(input("Ingrese email: "))
        contrasenia = str(input("Ingrese su contraseña: "))
        email_encontrado = False
        contrasenia_encontrada = False
        for p in Profesor.profesores:
            if email == p.email:
                if p.validar_credenciales(email, contrasenia) == True:
                    print("Su acceso fue exitoso\n")
                    contrasenia_encontrada = True
                if contrasenia_encontrada == False:
                    "Contraseña incorrecta"
        if email_encontrado == False:
            print("Email inexistete. Comunicarse con alumnado")  
            
            
            #--------------------------  SUBMENU PROFESOR    -----------------------------------: 
            sub_opcion = 0
            while sub_opcion != 3:
                print("\nSubmenu Profesor:")
                print("1. Dictar curso")
                print("2. Ver curso") 
                print("3. Volver al menú principal.")
                sub_opcion = int(input("Ingrese una opcion: "))
                if sub_opcion == 1:
                    nombre_curso = input("\nIngrese el nombre del nuevo curso: ")
                    contrasenia_aleatoria 
                    mis_cursos = Curso(nombre_curso, contrasenia_aleatoria)
                    Curso.cursos.append(mis_cursos)
                    if nombre_curso != mis_cursos:
                        print("\nCurso dado de alta exitosamente:")
                        print(f"Nombre del curso: {mis_cursos.nombre}")
                        print("Clave matriculacion: ", contrasenia_aleatoria, "\n")
                    elif nombre_curso == {mis_cursos.nombre_curso} : 
                        print("Curso ya ingresado.")
                        break
                    
                elif sub_opcion == 2:
                    print("\nEl Profesor dicta las siguientes materias: ")
                    print(mis_cursos.nombre)
                    if mis_cursos.nombre == None:
                        print("El profesor no tiene ningun curso dictado | Debe darse de alta en el alumnado!")
                else: 
                    print("\nVolviendo al menú principal....\n")       
        
                    
    elif opcion == 3:
        print("Cursos disponibles:\n")
        lista_curso_ordenada = sorted(Curso.cursos, key=lambda x: x.nombre) #ordena alfabeticamente!
        for curso in lista_curso_ordenada:
            print(f"{curso.nombre} | carrera: Tecnicatura Universitaria en Programación\n")
            
    else:
        print("Hasta luego...") 
        print("Saliendo del sistema")
        break