from criptografia import CifraDeCesar
import re


def entrada_valida(mensagem: str) -> bool:
    return bool(re.fullmatch(r"[A-Z]+\s*[A-Z]+", mensagem))


if __name__ == "__main__":

    cifra_de_cesar = CifraDeCesar()

    opcao = 0

    while opcao != 3:
        print("=" * 50)
        print("1 - Cifrar")
        print("2 - Decifrar")
        print("3 - Sair")
        try:
            opcao = int(input("Opção desejada: "))
            if opcao != 3:
                mensagem = input("Digite a mensagem: ")
                if entrada_valida(mensagem):
                    if opcao == 1:
                        print("="*50)
                        print("Mensagem Cifrada")
                        print(cifra_de_cesar.cifrar(mensagem))

                    elif opcao == 2:
                        print("="*50)
                        print("Mensagem Decifrada")
                        print(cifra_de_cesar.decifrar(mensagem))

                else:
                    print("Entrada invalida")

        except Exception:
            print("Opção inválida")
