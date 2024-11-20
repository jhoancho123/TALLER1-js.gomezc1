class Concentrado:
    def __init__(self, nombre: str, precio: float, calorias: int, registro_invima: str):
        self.nombre = nombre
        self.precio = precio
        self.calorias = calorias
        self._registro_invima = registro_invima

    @property
    def get_nombre(self) -> str:
        return self.nombre

    @property
    def get_precio(self) -> float:
        return self.precio

    @property
    def get_calorias(self) -> int:
        return self.calorias

    @property
    def get_informacion(self) -> str:
        return f"{self.nombre} (${self.precio})"

    @property
    def calcular_rentabilidad(self) -> float:
        return round(self.precio / self.calorias, 2)
