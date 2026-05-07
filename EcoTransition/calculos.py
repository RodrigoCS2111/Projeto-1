# Responsável pelos cálculos do sistema.
# Aqui ficarão as fórmulas de economia, custo, CO₂, payback, score e recomendação.

def calcular_combustao(quilometragem_mensal, consumo_km_l, preco_gasolina, ipva, seguro, manutencao_anual_combustao, anos):

    litros_por_mes = quilometragem_mensal / consumo_km_l

    custo_combustivel_mensal = litros_por_mes * preco_gasolina

    custo_combustivel_anual = custo_combustivel_mensal * 12

    custo_total_combustao = (custo_combustivel_anual + ipva + seguro + manutencao_anual_combustao) * anos

    return {
        "litros_por_mes": litros_por_mes,
        "custo_combustivel_mensal": custo_combustivel_mensal,
        "custo_combustivel_anual": custo_combustivel_anual,
        "custo_total_combustao": custo_total_combustao
    }