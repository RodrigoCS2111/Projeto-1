# Responsável por validar os dados digitados pelo usuário.
# Também fará o tratamento de erros usando try/except.

def ler_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))

            if valor < 0:
                print("Digite um valor positivo.")
            else:
                return valor

        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def ler_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))

            if valor < 0:
                print("Digite um valor positivo.")
            else:
                return valor

        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto == "":
            print("Este campo não pode ficar vazio.")
        elif texto.isdigit():
            print("Entrada inválida. Digite um texto válido.")
        else:
            return texto

def ler_nome(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto == "":
            print("Este campo não pode ficar vazio.")

        elif not texto.replace(" ", "").isalpha():
            print("Digite apenas letras.")

        else:
            return texto


def ler_opcao(mensagem, opcoes_validas):
    while True:
        opcao = input(mensagem).strip().lower()

        if opcao in opcoes_validas:
            return opcao
        else:
            print(f"Opção inválida. Escolha uma das opções: {', '.join(opcoes_validas)}")