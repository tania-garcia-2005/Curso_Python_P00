"""
Nombre: Tania Garcia Flores
Fecha:12/03/25
Descripción:
Crea una clase llamada Personaje que simule los movimientos de un personaje de videojuegos en una ventana.

1. El personaje se moverá por una ventana de tamaño máximo (x, y) = (10, 10) y podrá realizar los siguientes movimientos si no supera el límite de la ventana:
      * Avanzar (caracteres 'A' o 'a'): aumenta en 1 la posición en y,
      * Retroceder (caracteres 'R' o 'r'): disminuye en 1 la posición en y,
      * Derecha (caracteres 'D' o 'd'): aumenta en 1 la posición en x,
      * Izquierda (caracteres 'I' o 'i'): disminuye en 1 la posición en x.

2. El personaje tendrá los siguientes métodos (además de los métodos mágicos):
      * moverse() que recibe la orden como parámetro,
      * posicion_actual() que muestra en consola la posición en (x,y).

3. Se debe llevar un registro del ID de los personajes creados, por lo que se debe utilizar un atributo de clase.

4. Al crear los objetos de la clase, inicialmente deben establecerse en el origen (x, y) = (0, 0).

5. Se debe solicitar iterativamente la secuencia de movimientos e indicar la posición final de la secuencia.

6. El programa se detendrá con los caracteres 'S' o 's'.
"""
class Personaje:
    """
    Clase que representa un personaje.
    Sus atributos son: id (atributo de clase), x y y.
    Sus métodos son: __init__(), __str__(), moverse(), posicion_actual().
    """

    # Atributo de mi clase.(como está en el diagrama)
    contador_id = 1

    def __init__(self):
        """
        Constructor de personaje.
        """
        # Atributos de instancia
        self.x = 0
        self.y = 0

        # Se asigna el atributo de clase como atributo de instancia y luego se incrementa
        self.id = Personaje.contador_id
        Personaje.contador_id += 1

    def moverse(self, orden: str) -> None:
        """
         mueve el personaje según la orden dada.
        :param orden: Letra que indica el movimiento.
        """
        if orden in ('A', 'a') and self.y < 10:
            self.y += 1
        elif orden in ('R', 'r') and self.y > 0:
            self.y -= 1
        elif orden in ('D', 'd') and self.x < 10:
            self.x += 1
        elif orden in ('I', 'i') and self.x > 0:
            self.x -= 1

    def posicion_actual(self) -> None:
        """
        Muestra la posición actual del personaje.
        """
        print(f"Posición actual: ({self.x}, {self.y})")

    def __str__(self) -> str:
        """
        Representación en cadena del personaje.
        :return: Información del personaje en forma de cadena.
        """
        return f"Personaje(id: {self.id}, Posición: ({self.x}, {self.y}))"

if __name__ == "__main__":
    #Aquí creo a mi  personaje
    personaje = Personaje()
    print("  -- Simulación de movimiento del personaje.")
    print(personaje)

    orden = ""
    while orden not in ('S', 's'):
        orden = input("Ingrese un movimiento (A, R, D, I) o 'S' para salir: ")
        if orden not in ('S', 's'):
            personaje.moverse(orden)
            personaje.posicion_actual()

    print("Posición final:")
    personaje.posicion_actual()
