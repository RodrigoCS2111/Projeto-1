# Arquivo principal do sistema.
# Responsável por iniciar o programa, exibir menus e conectar todas as funcionalidades.
from calculos import calcular_combustao, calcular_eletrico, calcular_economia, calcular_impacto_ambiental, calcular_score, gerar_recomendacao
from dados import CARROS_ELETRICOS, FATOR_CO2_GASOLINA, FATOR_ARVORE
from validacoes import ler_float, ler_int, ler_nome, ler_opcao

Combustao = calcular_combustao(
    
    quilometragem_mensal = 1100,
    consumo_km_l = 13,
    preco_gasolina =6.75,
    ipva = 3000,
    seguro = 2000,
    manutencao_anual_combustao = 1500,
    anos = 5       
)

eletrico = calcular_eletrico(
    quilometragem_mensal = 1100,
    preco_energia = 0.90,
    categoria_veiculo = "suv",
    ipva = 3000,
    seguro = 2000,
    anos = 5,
    carros_eletricos = CARROS_ELETRICOS
)


economia = calcular_economia(
    custo_combustivel_anual = Combustao["custo_combustivel_anual"],
    custo_eletrico_anual = eletrico["custo_eletrico_anual"],
    custo_total_combustao = Combustao["custo_total_combustao"], 
    custo_total_eletrico =eletrico["custo_total_eletrico"], 
    manutencao_anual_combustao = 1500, 
    manutencao_anual_eletrico =eletrico["manutencao_anual_eletrico"] , 
    preco_carro_atual = 110000, 
    preco_carro_eletrico =eletrico["preco_carro_eletrico"], 
    anos = 5
)

print(economia)