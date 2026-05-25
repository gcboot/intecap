class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_info(self):
        print(f"Libro: {self.titulo}, Autor: {self.autor}")

# Ejemplo de uso
mi_libro = Libro("Cien años de soledad", "Gabriel García Márquez")
mi_libro.mostrar_info()