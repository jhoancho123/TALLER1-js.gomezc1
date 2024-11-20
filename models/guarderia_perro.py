from typing import List, Tuple
from models.concentrado import Concentrado

class Perro:
    def __init__(self, nombre: str, raza: str, peso: float, edad: int):
        self.nombre = nombre
        self.raza = raza
        self.peso = peso
        self.edad = edad

    def dar_info(self) -> dict:
        return {
            "nombre": self.nombre,
            "raza": self.raza,
            "peso": self.peso,
            "edad": self.edad
        }

class Guarderia:
    def __init__(self):
        self.concentrados: List[Concentrado] = []  # Lista de concentrados
        self.perros: List[Perro] = []  # Lista de perros

        # Crear los perros
        self.perros.append(Perro("Rufo", "Labrador", 22, 7))
        self.perros.append(Perro("Bingo", "Pug", 6, 2))
        self.perros.append(Perro("Lassie", "Collie", 27, 5))

    def agregar_concentrado(self, concentrado: Concentrado):
        self.concentrados.append(concentrado)

    def listar_concentrados(self) -> List[str]:
        return [concentrado.get_nombre for concentrado in self.concentrados]

    def retornar_perros(self) -> Tuple[Perro, Perro, Perro]:
        return tuple(self.perros)
