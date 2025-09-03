#Caso 3. Registro de Ventas de una Tienda

class Venta:
    contador_id = 1 #el contador para asignarle un ID automatico y no tener que pedirlo

    def __init__(self, numero_venta, fecha, monto):
        self.numero_venta = numero_venta
        self.fecha = fecha
        self.monto = monto
        self.id = Venta.contador_id
        Venta.contador_id += 1

    def actualizar_monto(self, nuevo_monto):
        self.monto = nuevo_monto
        print(f"El monto de la venta {self.numero_venta} ha sido actualizado con exito.")

#nueva clase gestor para hacer cambios-----------------------

class Gestor:
    def __init__(self):
        self.ventas = []
        
    def agregar_venta(self,venta):
        self.ventas.append(venta)
        print(f"Ha agregado la venta {venta.numero_venta} con exito")
        self.agregar_txt()
        
    def eliminar_venta(self, numero_venta):
        for venta in self.ventas:
            if venta.numero_venta == numero_venta:
                self.ventas.remove(venta)
                print(f"Ha eliminado la venta {numero_venta} con exito.")
                self.agregar_txt() 
                break
            
    def actualizar_venta(self, numero_venta, nuevo_monto):
        for venta in self.ventas:
            if venta.numero_venta == numero_venta:
                venta.actualizar_monto(nuevo_monto)
                self.agregar_txt()
                break

    def mostrar_ventas(self):
        if self.ventas:
            print("Registro de Ventas:")
            for venta in self.ventas:
                print(f"ID: {venta.id}, Numero: {venta.numero_venta}, Fecha: {venta.fecha}, Monto: {venta.monto}")
        else:
            print("No hay ventas registradas.")
            
#metodo para el archivo de texto
    def agregar_txt(self):
        archivo = open('ventas.txt', 'w')
        for venta in self.ventas:
            archivo.write(f"ID: {venta.id} Numero: {venta.numero_venta} Fecha: {venta.fecha} Monto: {venta.monto}\n")
        archivo.close()
        print("Archivo creado y texto escrito exitosamente")
        
#prueba-------------------
gestor = Gestor()

#agregar ventas
v1 = Venta("1", "13/08/25", "$30")
gestor.agregar_venta(v1)

v2 = Venta("2", "13/08/25", "$70")
gestor.agregar_venta(v2)

#mostrar las ventas
gestor.mostrar_ventas()

#actualizar venta
gestor.actualizar_venta("1", "$28")

#eliminar venta
gestor.eliminar_venta("2")

#mostrar de nuevo 
gestor.mostrar_ventas()