# Arquivo que armazena dados fixos do sistema.

CARROS_ELETRICOS = {

    "popular": {
        "consumo_kwh_km": 0.12,
        "preco_medio": 120000.00,
        "manutencao_anual": 1500.00
    },

    "suv": {
        "consumo_kwh_km": 0.20,
        "preco_medio": 185000.00,
        "manutencao_anual": 2500.00
    },

    "luxo": {
        "consumo_kwh_km": 0.25,
        "preco_medio": 300000.00,
        "manutencao_anual": 4000.00
    }
}

FATOR_CO2_GASOLINA = 2.3
FATOR_ARVORE = 21


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


# Teste temporário
dados = coletar_dados_simulacao()
print("\nDados coletados:")
print(dados)