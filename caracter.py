
class Caracter:

    def __init__(self, letra: str, letra_converter: str) -> None:
        self.letra = letra
        self.letra_converter = letra_converter

    def get_letra(self) -> str:
        return self.letra

    def get_letra_converter(self) -> str:
        return self.letra_converter
