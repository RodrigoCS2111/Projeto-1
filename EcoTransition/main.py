# Arquivo principal do sistema.
# Responsável por iniciar o programa, exibir menus e conectar todas as funcionalidades.
from calculos import calcular_combustao, calcular_eletrico, calcular_economia, calcular_impacto_ambiental, calcular_score, gerar_recomendacao
from dados import CARROS_ELETRICOS, FATOR_CO2_GASOLINA, FATOR_ARVORE
from validacoes import ler_float, ler_int, ler_nome, ler_opcao


def coletar_dados_simulacao():
    print("\n=== DADOS DA SIMULAÇÃO ===\n")

    preco_carro_atual = ler_float("Preço do carro atual (R$): ")
    preco_gasolina = ler_float("Preço da gasolina (R$/L): ")
    preco_energia = ler_float("Preço da energia (R$/kWh): ")
    quilometragem_mensal = ler_float("Quilometragem mensal (km): ")
    consumo_km_l = ler_float("Consumo do veículo a combustão (km/L): ")

    categoria_veiculo = ler_opcao(
        "Categoria do veículo elétrico desejado (popular/suv/luxo): ",
        ["popular", "suv", "luxo"]
    )

    prioridade_usuario = ler_opcao(
        "Sua prioridade (economia/sustentabilidade/equilibrio): ",
        ["economia", "sustentabilidade", "equilibrio"]
    )

    ipva = ler_float("IPVA anual (R$): ")
    seguro = ler_float("Seguro anual (R$): ")
    manutencao_anual_combustao = ler_float("Manutenção anual do carro atual (R$): ")
    anos = ler_int("Quantidade de anos para simulação: ")

    return {
        "preco_carro_atual": preco_carro_atual,
        "preco_gasolina": preco_gasolina,
        "preco_energia": preco_energia,
        "quilometragem_mensal": quilometragem_mensal,
        "consumo_km_l": consumo_km_l,
        "categoria_veiculo": categoria_veiculo,
        "prioridade_usuario": prioridade_usuario,
        "ipva": ipva,
        "seguro": seguro,
        "manutencao_anual_combustao": manutencao_anual_combustao,
        "anos": anos
    }


dados = coletar_dados_simulacao()
print("\nDados coletados:")
print(dados)
