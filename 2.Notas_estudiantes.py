#Caso 2. Sistema de Gestión de Notas de Estudiantes

class Estudiante:
    contador_id = 1 #el contador para asignarle un ID automatico y no tener que pedirlo

    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas 
        self.id = Estudiante.contador_id
        Estudiante.contador_id += 1

    def actualizar_notas(self, notas_actualizadas):
        self.notas = notas_actualizadas
        print(f"Las notas del estudiante {self.nombre} han sido actualizadas con exito.")

#nueva clase gestor para hacer cambios-----------------------

class Gestor:
    def __init__(self):
        self.estudiantes = []
        
    def agregar_estudiante(self,estudiante):
        self.estudiantes.append(estudiante)
        print(f"Ha agregado al estudiante {estudiante.nombre} con exito")
        self.agregar_txt()

    def eliminar_estudiante(self, nombre):
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre:
                self.estudiantes.remove(estudiante)
                print(f"Ha eliminado al estudiante {nombre} con exito.")
                self.agregar_txt() 
                break
    
    def actualizar_notas(self, nombre, notas_actualizadas):
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre:
                estudiante.actualizar_notas(notas_actualizadas)
                self.agregar_txt()  
                break

    def mostrar_estudiantes(self):
        if self.estudiantes:
            print("Registro de Estudiantes: ")
            for estudiante in self.estudiantes:
                print(f"ID: {estudiante.id}, Nombre: {estudiante.nombre}, Notas: {estudiante.notas}")
        else:
            print("No hay estudiantes registrados.")

#metodo para el archivo de texto
    def agregar_txt(self):
        archivo = open('notas.txt', 'w')
        for estudiante in self.estudiantes:
            archivo.write(f"ID: {estudiante.id} Nombre: {estudiante.nombre} Notas: {estudiante.notas}\n")
        archivo.close()
        print("Archivo creado y texto escrito exitosamente")
    
#prueba -----------------------
gestor = Gestor()

#agregar estudiante
e1 = Estudiante("Danna", [8, 9, 7])
gestor.agregar_estudiante(e1)

e2 = Estudiante("Fernanda", [6, 7, 8])
gestor.agregar_estudiante(e2)

#mostrar estudiantes
gestor.mostrar_estudiantes()

#actualizar notas de Danna
gestor.actualizar_notas("Danna", [9, 9, 10])

#eliminar estudiante
gestor.eliminar_estudiante("Fernanda")

#mostrar estudiantes
gestor.mostrar_estudiantes()
