# Arquivo principal do sistema.
# Responsável por iniciar o programa, exibir menus e conectar todas as funcionalidades.
from calculos import calcular_combustao, calcular_eletrico, calcular_economia, calcular_impacto_ambiental, calcular_score, gerar_recomendacao
from dados import CARROS_ELETRICOS, FATOR_CO2_GASOLINA, FATOR_ARVORE
from validacoes import ler_float, ler_int, ler_nome, ler_opcao, ler_email
from crud import adicionar_simulacao, carregar_simulacoes, salvar_simulacoes, listar_simulacoes_usuario

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

def identificar_usuario():
    print("\n=== IDENTIFICAÇÃO DO USUÁRIO ===\n")

    nome = ler_nome("Digite seu nome: ")
    email = ler_email("Digite seu e-mail: ")

    return {
        "nome": nome,
        "email": email
    }
    
def menu_principal(usuario):
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print(f"Usuário: {usuario['nome']} | {usuario['email']}")
        print("1 - Nova simulação")
        print("2 - Ver histórico")
        print("3 - Sair")

        opcao = ler_opcao("Escolha uma opção: ", ["1", "2", "3"])

        if opcao == "1":
         simulacao = executar_simulacao(usuario)

         salvar = ler_opcao("\nDeseja salvar esta simulação? (s/n): ",["s", "n"])

         if salvar == "s":
          adicionar_simulacao(simulacao)
          print("\nSimulação salva com sucesso!")
         else:
          print("\nSimulação não foi salva.")

          print("\nSimulação finalizada com sucesso!")

        elif opcao == "2":
         historico = listar_simulacoes_usuario(usuario["email"])

         print("\n=== HISTÓRICO DE SIMULAÇÕES ===")
 
         if not historico:
            print("Nenhuma simulação encontrada.")
            
         else:
           for simulacao in historico:
            print(f"\nID: {simulacao['id']}")
            print(f"Categoria: {simulacao['entradas']['categoria_veiculo']}")
            print(f"Economia total: R$ {simulacao['resultados']['economia']['economia_total']:.2f}")
            print(f"Score: {simulacao['resultados']['recomendacao']['score_viabilidade']}/5")

        elif opcao == "3":
            print("\nEncerrando o EcoTransition. Até logo!")
            break

def processar_simulacao(usuario, dados):
    combustao = calcular_combustao(
        quilometragem_mensal=dados["quilometragem_mensal"],
        consumo_km_l=dados["consumo_km_l"],
        preco_gasolina=dados["preco_gasolina"],
        ipva=dados["ipva"],
        seguro=dados["seguro"],
        manutencao_anual_combustao=dados["manutencao_anual_combustao"],
        anos=dados["anos"]
    )

    eletrico = calcular_eletrico(
        quilometragem_mensal=dados["quilometragem_mensal"],
        preco_energia=dados["preco_energia"],
        categoria_veiculo=dados["categoria_veiculo"],
        ipva=dados["ipva"],
        seguro=dados["seguro"],
        anos=dados["anos"],
        carros_eletricos=CARROS_ELETRICOS
    )

    economia = calcular_economia(
        custo_combustivel_anual=combustao["custo_combustivel_anual"],
        custo_eletrico_anual=eletrico["custo_eletrico_anual"],
        custo_total_combustao=combustao["custo_total_combustao"],
        custo_total_eletrico=eletrico["custo_total_eletrico"],
        manutencao_anual_combustao=dados["manutencao_anual_combustao"],
        manutencao_anual_eletrico=eletrico["manutencao_anual_eletrico"],
        preco_carro_atual=dados["preco_carro_atual"],
        preco_carro_eletrico=eletrico["preco_carro_eletrico"],
        anos=dados["anos"]
    )

    impacto = calcular_impacto_ambiental(
        litros_por_mes=combustao["litros_por_mes"],
        anos=dados["anos"],
        fator_co2_gasolina=FATOR_CO2_GASOLINA,
        fator_arvore=FATOR_ARVORE
    )

    score = calcular_score(economia["tempo_retorno"])

    recomendacao = gerar_recomendacao(
        score_viabilidade=score,
        quilometragem_mensal=dados["quilometragem_mensal"],
        preco_gasolina=dados["preco_gasolina"],
        economia_anual=economia["economia_anual"],
        tempo_retorno=economia["tempo_retorno"]
    )

    simulacao = {
        "usuario": usuario,
        "entradas": dados,
        "resultados": {
            "combustao": combustao,
            "eletrico": eletrico,
            "economia": economia,
            "impacto_ambiental": impacto,
            "recomendacao": recomendacao
        }
    }

    return simulacao

def executar_simulacao(usuario):
    dados = coletar_dados_simulacao()
    simulacao = processar_simulacao(usuario, dados)

    combustao = simulacao["resultados"]["combustao"]
    eletrico = simulacao["resultados"]["eletrico"]
    economia = simulacao["resultados"]["economia"]
    impacto = simulacao["resultados"]["impacto_ambiental"]
    recomendacao = simulacao["resultados"]["recomendacao"]

    print("\n=== RESULTADO DA SIMULAÇÃO ===\n")
    print(f"Custo anual com combustível: R$ {combustao['custo_combustivel_anual']:.2f}")
    print(f"Custo anual com energia: R$ {eletrico['custo_eletrico_anual']:.2f}")
    print(f"Economia anual estimada: R$ {economia['economia_anual']:.2f}")
    print(f"Economia total no período: R$ {economia['economia_total']:.2f}")
    print(f"Economia real considerando investimento: R$ {economia['economia_real']:.2f}")

    if economia["tempo_retorno"] == -1:
        print("Tempo de retorno: não se paga no período analisado")
    else:
        print(f"Tempo de retorno: {economia['tempo_retorno']:.1f} anos")

    print(f"Redução estimada de CO₂: {impacto['economia_co2']:.2f} kg")
    print(f"Equivalente a aproximadamente {impacto['equivalencia_arvores']:.0f} árvores")
    print(f"Score de viabilidade: {recomendacao['score_viabilidade']}/5")
    print(f"Recomendação: {recomendacao['recomendacao']}")

    print("\nPrincipais fatores:")
    if recomendacao["fatores"]:
        for fator in recomendacao["fatores"]:
            print(f"- {fator}")
    else:
        print("- Nenhum fator de destaque identificado.")

    return simulacao

if __name__ == "__main__":
    usuario = identificar_usuario()
    menu_principal(usuario)
