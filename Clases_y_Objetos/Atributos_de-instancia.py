print("***********")
print("*  Tania Garcia Flores.      **")
print("*   6 de Marzo de 2025.      **")
print("***********")

class Estudiante:
    def _init_(self, nombre: str):
        self.nombre = nombre
        self.temas_aprendidos = []

    def aprender_tema(self, tema: str) -> None:
        self.temas_aprendidos.append(tema)
        print(f"{self.nombre} aprendió {tema}")

    def _str_(self) -> str:
        return f"Estudiante(nombre:{self.nombre}, temas aprendidos:{self.temas_aprendidos})"


class Profesor:
    def _init_(self, nombre: str, temas_dominados: list[str]):
        self.nombre = nombre
        self.temas_dominados = temas_dominados

    def dominar_tema(self, tema: str):
        self.temas_dominados.append(tema)
        print(f"{self.nombre} domina el tema {tema}")

    def ensenar_tema(self, no_tema: int) -> str:
        if 0 <= no_tema < len(self.temas_dominados):
            return self.temas_dominados[no_tema]
        else:
            return "fuera de rango"

    def _str_(self) -> str:
        return f"Profesor(nombre:{self.nombre}, temas dominados:{self.temas_dominados})"

if __name__ == '__main__':

    estudiante1 = Estudiante("tania")
    estudiante2 = Estudiante("pati")

    profesor1 = Profesor("alberto", ["paradigmas de programacion", "Base de datos"])

    estudiante1.aprender_tema("Evolucion sitios web")
    estudiante2.aprender_tema("Internet de las cosas")

    # Agregar un nuevo tema
    #profesor1.dominar_tema("inteligencia artificial")

    # Solicitar el subíndice al usuario
    indice = input("Ingrese su subíndice: ")
    if indice.isnumeric():
        enviar = int(indice)
        tema = profesor1.ensenar_tema(enviar)
        print(tema)
    else:
        print("Número no válido.")


    print(estudiante1)
    print(estudiante2)
    print(profesor1)


