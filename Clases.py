from abc import ABC, abstractmethod
import random

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
        self._archivos = []
        self._codigo = self.generar_codigo()

    def __str__(self):
        return f"Nombre del curso: {self._nombre_Curso}\nContrasenia: {self._contrasenia_matriculacion}\n"

    def generar_contrasenia(self):
        import random
        import string

        self._contrasenia_matriculacion = "".join(
            random.choices(string.ascii_letters + string.digits, k=6)
        )
        
    def listar_archivos(self):
        return self._archivos
    
    def agregar_archivo(self, nombre_archivo, formato_archivo):
        nuevo_archivo = f"{nombre_archivo}.{formato_archivo}"
        self._archivos.append(nuevo_archivo)
        print(f"Se ha agregado el archivo {nuevo_archivo} al curso {self._nombre_Curso}")
        
    def generar_codigo(self):
        codigo = str(random.randint(10, 99))  #rango de creacion
        return codigo    
        
    
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
            
    def desmatricular_de_curso(self, curso):
        if curso in self.mis_cursos:
            self.mis_cursos.remove(curso)
            print(f"Te has desmatriculado de {curso._nombre_Curso}")
        else:
            print(f"No estás matriculado en {curso._nombre_Curso}")        
            
            
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

Usuario1 = Estudiante("Fran", "Joselu", "alum@gmail.com", "12", 111, 2020)
Usuario2 = Profesor("Alberto", "Gonzales", "profe@gmail.com", "12", "Programador", 2015,)

cursos_disponibles = []
cursos_de_la_carrera = [
    {"Materia": "Inglés I", "Carrera": "Tecnicatura Universitaria en Programacion"},                 #ORDENAR     yy ANTES/DESPUES
    {"Materia": "Programación II", "Carrera": "Tecnicatura Universitaria en Programacion"},
    {"Materia": "Inglés II", "Carrera": "Tecnicatura Universitaria en Programacion"},
    {"Materia": "Laboratorio II", "Carrera": "Tecnicatura Universitaria en Programacion"},
    {"Materia": "Programación I", "Carrera": "Tecnicatura Universitaria en Programacion"},
    {"Materia": "Laboratorio I", "Carrera": "Tecnicatura Universitaria en Programacion"},
]

#----------------------------------------------------------------------------------------------
from datetime import date, timedelta
    
class Archivo(Curso):
    def __init__(self, nombre, fecha, formato):
        self.nombre = nombre
        self.fecha = date.today()
        self.formato = formato
        
    def __str__(self):
        return f"{self.nombre}, {self.fecha}, {self.formato}"
    
class Carrera(Estudiante):
    def __init__(self, nombre, cant_anios):  
       self.nombre = nombre
       self.cant_anios = cant_anios
       
    def __str__(self):
        return f"{self.nombre}, {self.cant_anios}"
    
    def get_cant_materias() -> int:
        pass 