# Arquivo principal do sistema.
# Responsável por iniciar o programa, exibir menus e conectar todas as funcionalidades.
from calculos import calcular_combustao, calcular_eletrico, calcular_economia, calcular_impacto_ambiental, calcular_score, gerar_recomendacao
from dados import CARROS_ELETRICOS, FATOR_CO2_GASOLINA, FATOR_ARVORE
from validacoes import ler_float, ler_int, ler_nome, ler_opcao, ler_email
from crud import adicionar_simulacao, listar_simulacoes_usuario, atualizar_simulacao, excluir_simulacao
from interface import mostrar_titulo, pausar, loading, mostrar_resultado_simulacao, limpar_tela, formatar_moeda, mostrar_boas_vindas


def coletar_dados_simulacao():
    mostrar_titulo("DADOS DA SIMULAÇÃO")

    preco_carro_atual = ler_float("Preço do carro atual (R$): ")
    preco_gasolina = ler_float("Preço da gasolina (R$/L): ")
    preco_energia = ler_float("Preço da energia (R$/kWh): ")
    quilometragem_mensal = ler_float("Quilometragem mensal (km): ")
    consumo_km_l = ler_float("Consumo do veículo a combustão (km/L): ", permitir_zero=False)

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
    anos = ler_int("Quantidade de anos para simulação: ", permitir_zero=False)

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
    limpar_tela()
    mostrar_titulo("IDENTIFICAÇÃO DO USUÁRIO")

    nome = ler_nome("Digite seu nome: ")
    email = ler_email("Digite seu e-mail: ")

    return {
        "nome": nome,
        "email": email
    }


 
    
def menu_principal(usuario):
    
    while True:
        limpar_tela()
        mostrar_titulo("MENU PRINCIPAL")
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
         menu_historico(usuario)
         
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
     tempo_retorno=economia["tempo_retorno"],
     prioridade_usuario=dados["prioridade_usuario"]
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
    limpar_tela()
    dados = coletar_dados_simulacao()
    simulacao = processar_simulacao(usuario, dados)

    loading("Calculando sua análise")
    mostrar_resultado_simulacao(simulacao)
    pausar()

    return simulacao




def menu_historico(usuario):
    while True:
        limpar_tela()
        historico = listar_simulacoes_usuario(usuario["email"])

        mostrar_titulo("HISTÓRICO DE SIMULAÇÕES")

        if not historico:
            print("Nenhuma simulação encontrada.")
            pausar()
            return

        for simulacao in historico:
            print(f"\nID: {simulacao['id']}")
            print(f"Categoria: {simulacao['entradas']['categoria_veiculo']}")
            print(f"Economia total: {formatar_moeda(simulacao['resultados']['economia']['economia_total'])}")
            print(f"Score: {simulacao['resultados']['recomendacao']['score_viabilidade']}/5")
            print(f"Perfil: {simulacao['resultados']['recomendacao']['perfil_usuario']}")
            
        print("\n1 - Gerenciar simulação")
        print("2 - Voltar ao menu principal")

        escolha = ler_opcao("Escolha uma opção: ", ["1", "2"])

        if escolha == "2":
            return

        id_simulacao = ler_int("\nDigite o ID da simulação que deseja gerenciar: ")

        simulacao_escolhida = None

        for simulacao in historico:
            if simulacao["id"] == id_simulacao:
                simulacao_escolhida = simulacao
                break

        if simulacao_escolhida is None:
            print("\nSimulação não encontrada.")
            pausar()
            continue

        print("\n=== GERENCIAR SIMULAÇÃO ===")
        print("1 - Ver detalhes")
        print("2 - Editar simulação")
        print("3 - Excluir simulação")
        print("4 - Voltar ao histórico")

        opcao = ler_opcao("Escolha uma opção: ", ["1", "2", "3", "4"])

        if opcao == "1":
            ver_detalhes_simulacao(simulacao_escolhida)
            pausar()

        elif opcao == "2":
            editar_simulacao(usuario, simulacao_escolhida)
            pausar()

        elif opcao == "3":
            confirmar = ler_opcao("Tem certeza que deseja excluir? (s/n): ", ["s", "n"])

            if confirmar == "s":
                sucesso = excluir_simulacao(usuario["email"], id_simulacao)

                if sucesso:
                    print("\nSimulação excluída com sucesso!")
                else:
                    print("\nErro ao excluir simulação.")
            else:
                print("\nExclusão cancelada.")

            pausar()

        elif opcao == "4":
            continue



   
def ver_detalhes_simulacao(simulacao):
    limpar_tela()
    entradas = simulacao["entradas"]
    economia = simulacao["resultados"]["economia"]
    impacto = simulacao["resultados"]["impacto_ambiental"]
    recomendacao = simulacao["resultados"]["recomendacao"]

    mostrar_titulo("DETALHES DA SIMULAÇÃO")
    print(f"Categoria: {entradas['categoria_veiculo']}")
    print(f"Quilometragem mensal: {entradas['quilometragem_mensal']} km")
    print(f"Preço da gasolina: {formatar_moeda(entradas['preco_gasolina'])}")
    print(f"Preço da energia: {formatar_moeda(entradas['preco_energia'])}")
    print(f"Anos simulados: {entradas['anos']}")

    print("\n--- Resultados ---")
    print(f"Economia anual: {formatar_moeda(economia['economia_anual'])}")
    print(f"Economia total: {formatar_moeda(economia['economia_total'])}")
    print(f"Economia real: {formatar_moeda(economia['economia_real'])}")

    if economia["tempo_retorno"] == -1:
        print("Tempo de retorno: não se paga")
    else:
        print(f"Tempo de retorno: {economia['tempo_retorno']:.1f} anos")

    print(f"CO₂ evitado: {impacto['economia_co2']:.2f} kg")
    print(f"Equivalência em árvores: {impacto['equivalencia_arvores']:.0f}")
    print(f"Score: {recomendacao['score_viabilidade']}/5")
    print(f"Perfil da simulação: {recomendacao['perfil_usuario']}")
    print(f"Prioridade informada: {entradas['prioridade_usuario']}")
    print(f"Recomendação: {recomendacao['recomendacao']}")
    print(f"Mensagem personalizada: {recomendacao['mensagem_prioridade']}")




def editar_simulacao(usuario, simulacao_escolhida):
    limpar_tela()
    id_simulacao = simulacao_escolhida["id"]

    dados = simulacao_escolhida["entradas"].copy()

    mostrar_titulo("EDITAR SIMULAÇÃO")

    print("\nO que deseja alterar?")
    print("1 - Preço da gasolina")
    print("2 - Preço da energia")
    print("3 - Quilometragem mensal")
    print("4 - Categoria do veículo")
    print("5 - Quantidade de anos")
    print("6 - Cancelar")

    opcao = ler_opcao("Escolha uma opção: ", ["1", "2", "3", "4", "5", "6"])

    if opcao == "1":
        dados["preco_gasolina"] = ler_float("Novo preço da gasolina (R$/L): ")

    elif opcao == "2":
        dados["preco_energia"] = ler_float("Novo preço da energia (R$/kWh): ")

    elif opcao == "3":
        dados["quilometragem_mensal"] = ler_float("Nova quilometragem mensal (km): ")

    elif opcao == "4":
        dados["categoria_veiculo"] = ler_opcao(
            "Nova categoria (popular/suv/luxo): ",
            ["popular", "suv", "luxo"]
        )

    elif opcao == "5":
        dados["anos"] = ler_int("Nova quantidade de anos para simulação: ", permitir_zero=False)

    elif opcao == "6":
        print("\nEdição cancelada.")
        return

    nova_simulacao = processar_simulacao(usuario, dados)

    sucesso = atualizar_simulacao(
        email=usuario["email"],
        id_simulacao=id_simulacao,
        nova_simulacao=nova_simulacao
    )

    if sucesso:
     print("\nSimulação atualizada com sucesso!")
     loading("Recalculando sua análise")
     mostrar_resultado_simulacao(nova_simulacao)
    else:
     print("\nErro ao atualizar simulação.")

if __name__ == "__main__":
    mostrar_boas_vindas()
    usuario = identificar_usuario()
    menu_principal(usuario)
