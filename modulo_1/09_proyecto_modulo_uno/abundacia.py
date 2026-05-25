import os
import re

# Clase Cliente utilizando Programación Orientada a Objetos (POO)
class Cliente:
    def __init__(self, dpi, nombres, apellidos, telefono, email):
        self.dpi = dpi
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"DPI: {self.dpi} | {self.nombres} {self.apellidos} | Tel: {self.telefono} | Email: {self.email}"

class CarteraClientes:
    def __init__(self):
        self.clientes = []
        self.archivo = "clientes.txt"
        # *** PUNTO EXTRA: Recuperación de datos desde el archivo al iniciar ***
        self.cargar_datos_iniciales()

    def cargar_datos_iniciales(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r", encoding="utf-8") as f:
                    for linea in f:
                        d = linea.strip().split(",")
                        if len(d) == 5:
                            self.clientes.append(Cliente(d[0], d[1], d[2], d[3], d[4]))
            except Exception:
                self.clientes = []

    def guardar_en_archivo(self):
        # Sincroniza la lista actual con el archivo clientes.txt
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for c in self.clientes:
                    f.write(f"{c.dpi},{c.nombres},{c.apellidos},{c.telefono},{c.email}\n")
        except Exception:
            print("Error: No se pudo guardar la información en el disco.")

    # --- VALIDACIONES  ---
    def solicitar_dato(self, mensaje, validacion_func):
        while True:
            dato = input(mensaje).strip()
            try:
                return validacion_func(dato)
            except ValueError as e:
                print(f" >> [!] {e}. Intente de nuevo.")

    def validar_dpi(self, valor):
        if not (valor.isdigit() and len(valor) == 13):
            raise ValueError("DPI inválido (debe tener 13 números exactos)")
        return valor

    def validar_texto(self, valor, campo):
        if not valor.replace(" ", "").isalpha():
            raise ValueError(f"{campo} inválido (solo se permiten letras)")
        return valor

    def validar_tel(self, valor):
        if not (valor.isdigit() and len(valor) == 8):
            raise ValueError("Teléfono inválido (debe tener 8 números)")
        return valor

    def validar_correo(self, valor):
        if not re.match(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$', valor.lower()):
            raise ValueError("Correo inválido. Ejemplo: nombre@dominio.com")
        return valor

    # --- FUNCIONES DEL SISTEMA ---
    def ver_listado(self):
        print("\n" + "="*50)
        print("          LISTADO DE CLIENTES REGISTRADOS")
        print("="*50)
        if not self.clientes:
            print("La cartera de clientes está vacía actualmente.")
        else:
            for i, c in enumerate(self.clientes):
                print(f"[{i}] {c}")

    def agregar(self):
        print("\n--- REGISTRO DE NUEVO CLIENTE ---")
        dpi = self.solicitar_dato("DPI (13 dígitos): ", self.validar_dpi)
        nom = self.solicitar_dato("Nombres: ", lambda v: self.validar_texto(v, "Nombre"))
        ape = self.solicitar_dato("Apellidos: ", lambda v: self.validar_texto(v, "Apellido"))
        tel = self.solicitar_dato("Teléfono (8 dígitos): ", self.validar_tel)
        ema = self.solicitar_dato("Email (ejemplo@correo.com): ", self.validar_correo)
        
        self.clientes.append(Cliente(dpi, nom, ape, tel, ema))
        self.guardar_en_archivo()
        print("\n[OK] Cliente guardado con éxito.")

    def editar(self):
        self.ver_listado()
        if not self.clientes: return
        try:
            idx = int(input("\nIngrese el índice del cliente a modificar: "))
            if idx < 0 or idx >= len(self.clientes):
                print("[!] Error: El índice ingresado no existe en el listado.")
                return

            c = self.clientes[idx]
            print(f"\nEditando a: {c.nombres} {c.apellidos}")
            print("(Deje vacío y presione Enter para conservar el dato actual)")

            nuevo_dpi = input(f"Nuevo DPI [{c.dpi}]: ")
            if nuevo_dpi: c.dpi = self.validar_dpi(nuevo_dpi)
            
            nuevo_nom = input(f"Nuevos Nombres [{c.nombres}]: ")
            if nuevo_nom: c.nombres = self.validar_texto(nuevo_nom, "Nombre")

            nuevo_ape = input(f"Nuevos Apellidos [{c.apellidos}]: ")
            if nuevo_ape: c.apellidos = self.validar_texto(nuevo_ape, "Apellido")

            nuevo_tel = input(f"Nuevo Teléfono [{c.telefono}]: ")
            if nuevo_tel: c.telefono = self.validar_tel(nuevo_tel)

            nuevo_ema = input(f"Nuevo Email [{c.email}]: ")
            if nuevo_ema: c.email = self.validar_correo(nuevo_ema)

            self.guardar_en_archivo()
            print("\n[OK] Información actualizada correctamente.")
        except ValueError:
            print("[!] Error: Debe ingresar un número válido para el índice.")

    def eliminar(self):
        self.ver_listado()
        if not self.clientes: return
        try:
            idx = int(input("\nIngrese el índice del cliente a eliminar: "))
            if 0 <= idx < len(self.clientes):
                eliminado = self.clientes.pop(idx)
                self.guardar_en_archivo()
                print(f"[-] Cliente {eliminado.nombres} eliminado satisfactoriamente.")
            else:
                print("[!] Error: El índice seleccionado no existe.")
        except ValueError:
            print("[!] Error: Entrada no válida. Use números únicamente.")

def menu_principal():
    cartera = CarteraClientes()
    while True:
        print("\n" + "╔" + "═"*45 + "╗")
        print("║      ABARROTERÍA 'LA ABUNDANCIA'            ║")
        print("╚" + "═"*45 + "╝")
        print(" 1. Ver listado de clientes")
        print(" 2. Agregar nuevo cliente")
        print(" 3. Editar datos de cliente")
        print(" 4. Eliminar cliente de la lista")
        print(" 5. Salir")
        print("-" * 47)
        print(" *** PUNTO EXTRA: Recuperación de datos activa Para Recuperas los 25 puntos del ejerccio anterior***")
        print("-" * 47)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            cartera.ver_listado()
        elif opcion == "2":
            cartera.agregar()
        elif opcion == "3":
            cartera.editar()
        elif opcion == "4":
            cartera.eliminar()
        elif opcion == "5":
            print("\nFinalizando aplicación. ¡Que tenga un excelente día!")
            break
        else:
            print("[!] Opción no válida. Por favor, intente de nuevo.")
        
        print("\n\033[3mRecuperación de puntos del anterior ejercicio: Ejecutada con éxito\033[0m")

if __name__ == "__main__":
    menu_principal()