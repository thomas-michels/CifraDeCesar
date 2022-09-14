from typing import List
from caracter import Caracter


class BancoDeCaracteres:

    def __init__(self, caracteres: List[Caracter] = []) -> None:
        self.caracteres = caracteres

    def add_caracter(self, caracter: Caracter):
        self.caracteres.append(caracter)

    def buscar_caracter(self, letra: str, convertido: bool) -> Caracter:
        for caracter in self.caracteres:
            if convertido and letra == caracter.get_letra_converter():
                return caracter

            elif not convertido and letra == caracter.get_letra():
                return caracter
