import random

# Lista de palavras aleatórias
palavras = [
    "python", "programacao", "computador", "jogo", "forca",
    "desenvolvimento", "dados", "algoritmo", "tecnologia", "internet"
]


def escolher_palavra():
    return random.choice(palavras)


def exibir_forca(erros):
    estados = [
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """
    ]
    print(estados[erros])


def jogar():
    palavra = escolher_palavra()
    letras_adivinhadas = []
    tentativas = 6
    letras_erradas = []

    print("Bem-vindo ao Jogo da Forca!")

    while tentativas > 0:
        palavra_oculta = "".join([letra if letra in letras_adivinhadas else "_" for letra in palavra])

        print("\nPalavra: ", palavra_oculta)
        print("Letras erradas: ", " ".join(letras_erradas))
        print(f"Tentativas restantes: {tentativas}")

        letra = input("Digite uma letra: ").lower()

        if letra in letras_adivinhadas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra:
            letras_adivinhadas.append(letra)
            if all(letra in letras_adivinhadas for letra in palavra):
                print(f"Parabéns! Você adivinhou a palavra: {palavra}")
                break
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            exibir_forca(len(letras_erradas))

        if tentativas == 0:
            print(f"Você perdeu! A palavra era: {palavra}")


def main():
    while True:
        jogar()
        resposta = input("Deseja jogar novamente? (s/n): ").lower()
        if resposta != 's':
            print("Obrigado por jogar! Até a próxima.")
            break


if __name__ == "__main__":
    main()
