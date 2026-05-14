# Aqui ficarão as funções de salvar, listar, atualizar e excluir dados do JSON.
import json

CAMINHO_ARQUIVO = "database/simulacoes.json"


def carregar_simulacoes():
    try:
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def salvar_simulacoes(simulacoes):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(simulacoes, arquivo, indent=4, ensure_ascii=False)

def adicionar_simulacao(simulacao):
    simulacoes = carregar_simulacoes()

    simulacao["id"] = len(simulacoes) + 1

    simulacoes.append(simulacao)

    salvar_simulacoes(simulacoes)

def listar_simulacoes_usuario(email):
    simulacoes = carregar_simulacoes()

    simulacoes_usuario = []

    for simulacao in simulacoes:
        if simulacao["usuario"]["email"] == email:
            simulacoes_usuario.append(simulacao)

    return simulacoes_usuario