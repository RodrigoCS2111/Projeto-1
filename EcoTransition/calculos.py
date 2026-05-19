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
    

def calcular_eletrico(quilometragem_mensal, preco_energia, categoria_veiculo, ipva, seguro, anos, carros_eletricos):
   
    dados_categoria = carros_eletricos[categoria_veiculo]

    consumo_kwh_categoria = dados_categoria["consumo_kwh_km"]
    preco_carro_eletrico = dados_categoria["preco_medio"]
    manutencao_anual_eletrico = dados_categoria["manutencao_anual"]

    custo_eletrico_mensal = quilometragem_mensal * consumo_kwh_categoria * preco_energia

    custo_eletrico_anual = custo_eletrico_mensal * 12

    custo_total_eletrico = ( custo_eletrico_anual + ipva + seguro + manutencao_anual_eletrico) * anos

    return {
        "consumo_kwh_categoria": consumo_kwh_categoria,
        "preco_carro_eletrico": preco_carro_eletrico,
        "manutencao_anual_eletrico": manutencao_anual_eletrico,
        "custo_eletrico_mensal": custo_eletrico_mensal,
        "custo_eletrico_anual": custo_eletrico_anual,
        "custo_total_eletrico": custo_total_eletrico
    }
    

def calcular_economia(custo_combustivel_anual,custo_eletrico_anual,custo_total_combustao, custo_total_eletrico, manutencao_anual_combustao, manutencao_anual_eletrico, preco_carro_atual, preco_carro_eletrico, anos):
   

    economia_abastecimento_anual = custo_combustivel_anual - custo_eletrico_anual

    economia_manutencao_anual = manutencao_anual_combustao - manutencao_anual_eletrico

    diferenca_investimento = preco_carro_eletrico - preco_carro_atual

    economia_total = custo_total_combustao - custo_total_eletrico 

    economia_real = economia_total - diferenca_investimento ## Analisar se vai manter esse cálculo

    economia_anual = economia_total / anos

    if diferenca_investimento <= 0:
      tempo_retorno = 0
    elif economia_anual > 0:
     tempo_retorno = diferenca_investimento / economia_anual
    else:
      tempo_retorno = -1

    return {
        "economia_abastecimento_anual": economia_abastecimento_anual,
        "economia_manutencao_anual": economia_manutencao_anual,
        "diferenca_investimento": diferenca_investimento,
        "economia_total": economia_total,
        "economia_real": economia_real,
        "economia_anual": economia_anual,
        "tempo_retorno": tempo_retorno
    }
    
def calcular_impacto_ambiental(litros_por_mes, anos, fator_co2_gasolina, fator_arvore):

    co2_combustao_total = litros_por_mes * fator_co2_gasolina * 12 * anos

    co2_eletrico_total = 0

    economia_co2 = co2_combustao_total - co2_eletrico_total

    equivalencia_arvores = economia_co2 / fator_arvore

    return {
        "co2_combustao_total": co2_combustao_total,
        "co2_eletrico_total": co2_eletrico_total,
        "economia_co2": economia_co2,
        "equivalencia_arvores": equivalencia_arvores
    }
    

def calcular_score(tempo_retorno):
  

    if tempo_retorno == -1:
        score_viabilidade = 1
    elif tempo_retorno < 3:
        score_viabilidade = 5
    elif tempo_retorno < 5:
        score_viabilidade = 4
    elif tempo_retorno < 8:
        score_viabilidade = 3
    else:
        score_viabilidade = 2

    return score_viabilidade



def gerar_recomendacao(score_viabilidade, quilometragem_mensal, preco_gasolina, economia_anual, tempo_retorno):
   

    fatores = []

    if quilometragem_mensal > 1500:
        fatores.append("Alta quilometragem mensal")

    if preco_gasolina > 5.5:
        fatores.append("Alto custo da gasolina")

    if economia_anual > 5000:
        fatores.append("Economia anual significativa")

    if tempo_retorno == 0:
      fatores.append("Não há investimento adicional em relação ao carro atual")
    elif tempo_retorno != -1 and tempo_retorno < 5:
      fatores.append("Retorno rápido do investimento")

    if score_viabilidade == 5:
        recomendacao = "Vale muito a pena realizar a troca."
    elif score_viabilidade == 4:
        recomendacao = "Vale a pena realizar a troca."
    elif score_viabilidade == 3:
        recomendacao = "Pode valer a pena, mas exige atenção ao tempo de retorno."
    elif score_viabilidade == 2:
        recomendacao = "A troca é pouco vantajosa financeiramente no período analisado."
    else:
        recomendacao = "Não vale a pena realizar a troca, pois o investimento não se paga."

    return {
        "score_viabilidade": score_viabilidade,
        "recomendacao": recomendacao,
        "fatores": fatores
    }