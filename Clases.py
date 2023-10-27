from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre, apellido, email, contrasenia):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia

    @abstractmethod
    def __str__(self):
        return f"Nombre: {self._nombre} Apellido: {self._apellido} Email: {self._email} Contrasenia: {self._contrasenia}"

    @abstractmethod
    def validar_credenciales(self, email, contrasenia):
        pass

#--------------------------------------------------------------------------------------------------------------------------------------

class Curso:
    def __init__(self, nombre_Curso):
        self._nombre_Curso = nombre_Curso
        self._contrasenia_matriculacion = None

    def __str__(self):
        return f"Nombre del curso: {self._nombre_Curso}\nContrasenia: {self._contrasenia_matriculacion}\n"

    def generar_contrasenia(self):
        import random
        import string

        self._contrasenia_matriculacion = "".join(
            random.choices(string.ascii_letters + string.digits, k=6)
        )

#-------------------------------------------------------------------------------------------------------------------------------

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anioInscripcion):
        super().__init__(nombre, apellido, email, contrasenia)
        self._legajo = legajo
        self._anio_inscripcion_carrera = anioInscripcion
        listadeAlumnos.append(self)
        self.mis_cursos = []

    def validar_credenciales(email, contrasenia):
        for estudiante in listadeAlumnos:
            if estudiante._email == email and estudiante._contrasenia == contrasenia:
                return True
            else:
                return False

    def __str__(self):
        return f" Nombre : {self._nombre} Apellido: {self._apellido} Legajo: {self._legajo} Año de la inscripcion de la carrera: {self._anio_inscripcion_carrera}"

    def matricular_en_curso(self, curso):
        if curso not in self.mis_cursos:
            matriculacion = input(
                f"Ingrese la contraseña de matriculación para {curso._nombre_Curso}: "
            )
            if matriculacion == curso._contrasenia_matriculacion:
                self.mis_cursos.append(curso)
                print(f"Te has matriculado en {curso._nombre_Curso}")
            else:
                print("Contraseña de matriculación incorrecta.")
        else:
            print(f"Ya estás matriculado en {curso._nombre_Curso}")
            
            
#-----------------------------------------------------------------------------------------------------------------------------------

class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, titulo, anio_egreso):
        super().__init__(nombre, apellido, email, contrasenia)
        self._titulo = titulo
        self._anio_egreso = anio_egreso
        listadeProfesores.append(self)
        self.mis_cursos = []

    def validar_credenciales(email, contrasenia):
        for profes in listadeProfesores:
            if profes._email == email and profes._contrasenia == contrasenia:
                return True
            else:
                return False

    def dictar_curso(self, curso: Curso):
        curso.generar_contrasenia()
        self.mis_cursos.append(curso)

    def __str__(self):
        return f" Nombre: {self._nombre} Apellido: {self._apellido}"


#------------------------------------------------------------------------------------------------------------------------

listadeAlumnos = []
listadeProfesores = []

Usuario1 = Estudiante(
    "Fran", "Joselu", "alum1@gmail.com", "1234", 111, 2020
)
Usuario2 = Profesor(
    "Alberto",
    "Gonzales",
    "profe1@gmail.com",
    "12345",
    "Programador",
    "2015",
)
carrera = "Tecnicatura Universitaria en Programacion"
cursos_disponibles = []
cursos_de_la_carrera = [
    {"Materia": "Inglés I"},  #ORDENAR
    {"Materia": "Programación II"},
    {"Materia": "Inglés II"},
    {"Materia": "Laboratorio II"},
    {"Materia": "Programación I"},
    {"Materia": "Laboratorio I"},
]