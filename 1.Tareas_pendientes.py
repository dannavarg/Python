#Caso 1. Gestión de tareas pendientes

class Tarea:
    contador_id = 1   
    
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False
        self.id = Tarea.contador_id
        
        Tarea.contador_id = Tarea.contador_id + 1
        
    def completar_tarea(self):
        self.completada = True
        print(f"Ha completado la tarea {self.titulo}")
        
#-----------------------

class Gestor:
    def __init__(self):
        self.tareas = []
        
    def agregar_tarea(self,tarea):
        self.tareas.append(tarea)
        print(f"Ha agregado la tarea {tarea.titulo} con exito")
        self.agregar_txt()
            
    def eliminar_tarea(self,titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                self.tareas.remove(tarea)
                print(f"Ha eliminado la tarea {titulo} con exito.")
                self.agregar_txt()
                break
    
    def completar_tarea(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                tarea.completar_tarea()
                print(f"Ha completado la tarea '{titulo}' con exito.")
                self.agregar_txt()
                break

    def mostrar_tareas(self):
        if self.tareas:
            print("Tareas:")
            for tarea in self.tareas:
                print(f"La tarea de ID: {tarea.id}, titulo: {tarea.titulo}, sobre: {tarea.descripcion} se encuentra: {'Completada' if tarea.completada else 'Pendiente'}")
        else:
            print("No ha ingresado ninguna tarea.")
            
            
            
    def agregar_txt(self):

        archivo = open('tareas.txt', 'w')
        
        for tarea in self.tareas:
            if tarea.completada:
                estado = "Completada"
            else:
                estado = "Pendiente"
            archivo.write(f"(ID: {tarea.id} nombre: {tarea.titulo} descripcion: {tarea.descripcion} estado: {estado}\n")
        
        archivo.close()
        
        print("Archivo creado y texto escrito exitosamente")

#---------------
gestor = Gestor()

t1 = Tarea("Lavar ropa", "lavar la ropa sucia")
gestor.agregar_tarea(t1)

gestor.completar_tarea("Lavar ropa")

gestor.mostrar_tareas()

gestor.eliminar_tarea("Cocinar")

gestor.mostrar_tareas()


   