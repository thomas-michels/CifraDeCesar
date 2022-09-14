from caracter import Caracter
from banco_de_caracteres import BancoDeCaracteres


class CifraDeCesar:
    def __init__(self) -> None:
        self.banco_de_caracteres = BancoDeCaracteres(
            [
                Caracter("A", "D"),
                Caracter("B", "E"),
                Caracter("C", "F"),
                Caracter("D", "G"),
                Caracter("E", "H"),
                Caracter("F", "I"),
                Caracter("G", "J"),
                Caracter("H", "K"),
                Caracter("I", "L"),
                Caracter("J", "M"),
                Caracter("K", "N"),
                Caracter("L", "O"),
                Caracter("M", "P"),
                Caracter("N", "Q"),
                Caracter("O", "R"),
                Caracter("P", "S"),
                Caracter("Q", "T"),
                Caracter("R", "U"),
                Caracter("S", "V"),
                Caracter("T", "W"),
                Caracter("U", "X"),
                Caracter("V", "Y"),
                Caracter("W", "Z"),
                Caracter("X", "A"),
                Caracter("Y", "B"),
                Caracter("Z", "C"),
            ]
        )

    def cifrar(self, mensagem: str) -> str:
        mensagem_cifrada = ""
        tamanho = len(mensagem)

        for i in range(tamanho):
            letra = mensagem[i]
            if letra != " ":
                caracter = self.banco_de_caracteres.buscar_caracter(letra, False)
                mensagem_cifrada += caracter.get_letra_converter()

            else:
                mensagem_cifrada += " "

        return mensagem_cifrada

    def decifrar(self, mensagem) -> str:
        mensagem_cifrada = ""
        tamanho = len(mensagem)

        for i in range(tamanho):
            letra = mensagem[i]
            if letra != " ":
                caracter = self.banco_de_caracteres.buscar_caracter(letra, True)
                mensagem_cifrada += caracter.get_letra()

            else:
                mensagem_cifrada += " "

        return mensagem_cifrada
