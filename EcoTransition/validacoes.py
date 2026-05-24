# Responsável por validar os dados digitados pelo usuário.
# Também fará o tratamento de erros usando try/except.
import re


def ler_float(mensagem, permitir_zero=True):
    while True:
        try:
            valor = float(input(mensagem))

            if valor < 0:
                print("Digite um valor positivo.")

            elif valor == 0 and not permitir_zero:
                print("Digite um valor maior que zero.")

            else:
                return valor

        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def ler_int(mensagem, permitir_zero=True):
    while True:
        try:
            valor = int(input(mensagem))

            if valor < 0:
                print("Digite um valor positivo.")

            elif valor == 0 and not permitir_zero:
                print("Digite um valor maior que zero.")

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


def ler_email(mensagem):
    while True:
        email = input(mensagem).strip().lower()

        padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if email == "":
            print("Este campo não pode ficar vazio.")

        elif not re.match(padrao_email, email):
            print("Digite um e-mail válido.")

        else:
            return email


def ler_opcao(mensagem, opcoes_validas):
    while True:
        opcao = input(mensagem).strip().lower()

        if opcao in opcoes_validas:
            return opcao
        else:
            print(
                f"Opção inválida. Escolha uma das opções: {', '.join(opcoes_validas)}"
            )


def ler_menu_opcoes(titulo, opcoes):
    print(f"\n{titulo}\n")

    for numero, texto in opcoes.items():
        print(f"{numero} - {texto['label']}")

    while True:
        escolha = input("\nEscolha uma opção: ").strip()

        if escolha in opcoes:
            return opcoes[escolha]["valor"]

        print("Opção inválida. Digite o número correspondente à opção desejada.")
