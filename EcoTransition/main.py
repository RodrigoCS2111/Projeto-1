# Arquivo principal do sistema.
# Responsável por iniciar o programa, exibir menus e conectar todas as funcionalidades.
from calculos import calcular_combustao, calcular_eletrico, calcular_economia, calcular_impacto_ambiental, calcular_score, gerar_recomendacao
from dados import CARROS_ELETRICOS, FATOR_CO2_GASOLINA, FATOR_ARVORE
from validacoes import ler_float, ler_int, ler_nome, ler_opcao, ler_email, ler_menu_opcoes
from crud import adicionar_simulacao, listar_simulacoes_usuario, atualizar_simulacao, excluir_simulacao
from interface import mostrar_titulo, pausar, loading, mostrar_resultado_simulacao, limpar_tela, formatar_moeda,formatar_score,formatar_numero, mostrar_boas_vindas, mostrar_progresso, mostrar_impacto_edicao

def coletar_dados_veiculo():
    limpar_tela()
    mostrar_titulo("NOVA SIMULAÇÃO")
    mostrar_progresso(1, 4, "🚗 Dados do veículo atual")

    preco_carro_atual = ler_float("Preço do carro atual (R$): ")
    consumo_km_l = ler_float("Consumo do veículo a combustão (km/L): ", permitir_zero=False)
    manutencao_anual_combustao = ler_float("Manutenção anual do carro atual (R$): ")

    return {
        "preco_carro_atual": preco_carro_atual,
        "consumo_km_l": consumo_km_l,
        "manutencao_anual_combustao": manutencao_anual_combustao
    }



def coletar_custos_fixos():
    limpar_tela()
    mostrar_titulo("NOVA SIMULAÇÃO")
    mostrar_progresso(2, 4, "💰 Custos fixos")

    preco_gasolina = ler_float("Preço do combustível (R$/L): ")
    ipva = ler_float("IPVA anual (R$): ")
    seguro = ler_float("Seguro anual (R$): ")

    return {
        "preco_gasolina": preco_gasolina,
        "ipva": ipva,
        "seguro": seguro
    }



def coletar_uso_energia():
    limpar_tela()
    mostrar_titulo("NOVA SIMULAÇÃO")
    mostrar_progresso(3, 4, "⚡ Uso e energia")

    quilometragem_mensal = ler_float("Quilometragem mensal (km): ")
    anos = ler_int("Quantidade de anos para simulação: ", permitir_zero=False)

    print("\nComo deseja informar o custo da energia?\n")
    print("1 - Usar média nacional (R$ 0,85/kWh)")
    print("2 - Informar manualmente\n")

    opcao_energia = ler_opcao("Escolha uma opção: ", ["1", "2"])

    if opcao_energia == "1":
        preco_energia = 0.85
        print("\n✅ Média nacional aplicada: R$ 0,85/kWh")
        pausar()

    else:
        preco_energia = ler_float("Informe o preço da energia (R$/kWh): ")

    return {
        "quilometragem_mensal": quilometragem_mensal,
        "anos": anos,
        "preco_energia": preco_energia
    }



def coletar_preferencias():
    limpar_tela()
    mostrar_titulo("NOVA SIMULAÇÃO")
    mostrar_progresso(4, 4, "🎯 Preferências da simulação")

    categoria_veiculo = ler_menu_opcoes(
    "Qual categoria de carro elétrico você pretende comparar?",
    {
        "1": {"label": "Popular", "valor": "popular"},
        "2": {"label": "SUV", "valor": "suv"},
        "3": {"label": "Luxo", "valor": "luxo"}
    }
    )

    prioridade_usuario = ler_menu_opcoes(
    "O que mais pesa na sua decisão?",
    {
        "1": {"label": "Economia", "valor": "economia"},
        "2": {"label": "Sustentabilidade", "valor": "sustentabilidade"},
        "3": {"label": "Equilíbrio", "valor": "equilibrio"}
    }
    )
    return {
        "categoria_veiculo": categoria_veiculo,
        "prioridade_usuario": prioridade_usuario
    }



def mostrar_resumo_dados(dados):
    limpar_tela()
    mostrar_titulo("RESUMO DA SIMULAÇÃO")

    print("Confira os dados informados antes de gerar a análise:\n")

    print("🚗 Veículo atual")
    print(f"Preço do carro atual: {formatar_moeda(dados['preco_carro_atual'])}")
    print(f"Consumo: {dados['consumo_km_l']} km/L")
    print(f"Manutenção anual: {formatar_moeda(dados['manutencao_anual_combustao'])}")

    print("\n💰 Custos fixos")
    print(f"Preço da gasolina: {formatar_moeda(dados['preco_gasolina'])}")
    print(f"IPVA anual: {formatar_moeda(dados['ipva'])}")
    print(f"Seguro anual: {formatar_moeda(dados['seguro'])}")

    print("\n⚡ Uso e energia")
    print(f"Quilometragem mensal: {dados['quilometragem_mensal']} km")
    print(f"Anos simulados: {dados['anos']}")
    print(f"Preço da energia: {formatar_moeda(dados['preco_energia'])}/kWh")

    print("\n🎯 Preferências")
    print(f"Categoria desejada: {dados['categoria_veiculo']}")
    print(f"Prioridade: {dados['prioridade_usuario']}")

    print("\n1 - Confirmar e calcular")
    print("2 - Refazer preenchimento")

    opcao = ler_opcao("Escolha uma opção: ", ["1", "2"])

    return opcao == "1"



 
def coletar_dados_simulacao():
    while True:
        dados = {}

        dados.update(coletar_dados_veiculo())
        dados.update(coletar_custos_fixos())
        dados.update(coletar_uso_energia())
        dados.update(coletar_preferencias())

        confirmado = mostrar_resumo_dados(dados)

        if confirmado:
            return dados
        else:
            print("\nVamos refazer o preenchimento.")
            pausar()




def identificar_usuario():
    limpar_tela()
    mostrar_titulo("IDENTIFICAÇÃO DO USUÁRIO")

    print("Precisamos de algumas informações para personalizar sua experiência")
    print("e permitir que seu histórico de simulações fique salvo para consultas futuras.\n")

    print("🔒 Seus dados serão utilizados apenas para identificação dentro do sistema.\n")

    nome = ler_nome("👤 Como podemos te chamar? ")
    email = ler_email("📧 Informe seu melhor e-mail: ")

    loading("Preparando seu ambiente")

    return {
        "nome": nome,
        "email": email
    }

 
    
def menu_principal(usuario):
    while True:
        limpar_tela()
        mostrar_titulo("MENU PRINCIPAL")

        print(f"Seja bem-vindo, {usuario['nome']}!👋\n")
        print("O que você deseja fazer agora?\n")

        print("1 - 🚗 Nova simulação")
        print("   Compare seu veículo atual com um modelo elétrico.\n")

        print("2 - 📂 Ver histórico")
        print("   Consulte, edite ou exclua simulações salvas.\n")

        print("3 - 🚪 Sair")
        print("   Encerrar o sistema.\n")

        opcao = ler_opcao("Escolha uma opção: ", ["1", "2", "3"])

        if opcao == "1":
            simulacao = executar_simulacao(usuario)

            salvar = ler_opcao(
                "\nDeseja salvar esta simulação? (s/n): ",
                ["s", "n"]
            )

            if salvar == "s":
                adicionar_simulacao(simulacao)
                print("\n✅ Simulação salva com sucesso!")
            else:
                print("\nSimulação não foi salva.")

            print("\n✅ Simulação finalizada com sucesso!")
            pausar()

        elif opcao == "2":
            menu_historico(usuario)

        elif opcao == "3":
          if confirmar_saida():
             mostrar_tela_saida()
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
            print("📭 Você ainda não possui simulações salvas.")
            print("\nCrie uma nova simulação e salve o resultado para acompanhar seu histórico.")
            pausar()
            return

        print(f"👋 {usuario['nome']}, aqui estão suas simulações salvas:\n")

        for simulacao in historico:
            entradas = simulacao["entradas"]
            economia = simulacao["resultados"]["economia"]
            recomendacao = simulacao["resultados"]["recomendacao"]

            print("-" * 50)
            print(f"📄 SIMULAÇÃO #{simulacao['id']}")
            print(f"🚗 Categoria: {entradas['categoria_veiculo'].upper()}")
            print(f"🎯 Perfil: {recomendacao['perfil_usuario']}")
            print(f"💰 Economia total: {formatar_moeda(economia['economia_total'])}")
            print(f"⭐ Viabilidade: {formatar_score(recomendacao['score_viabilidade'])}")
            print("-" * 50)

        print("\nO que deseja fazer agora?")
        print("1 - Gerenciar uma simulação")
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
            print("\n⚠️ Simulação não encontrada.")
            print("Verifique o ID informado e tente novamente.")
            pausar()
            continue

        print("\nO que deseja fazer com esta simulação?\n")
        print("1 - 📊 Ver detalhes completos")
        print("2 - ✏️ Editar dados da simulação")
        print("3 - 🗑️ Excluir simulação")
        print("4 - ↩️ Voltar ao histórico")

        opcao = ler_opcao("Escolha uma opção: ", ["1", "2", "3", "4"])

        if opcao == "1":
            ver_detalhes_simulacao(simulacao_escolhida)
            pausar()

        elif opcao == "2":
            editar_simulacao(usuario, simulacao_escolhida)
            pausar()

        elif opcao == "3":
          excluir_simulacao_interface(usuario, simulacao_escolhida)
          pausar()
         
        elif opcao == "4":
            continue



   
def ver_detalhes_simulacao(simulacao):
    limpar_tela()

    entradas = simulacao["entradas"]
    combustao = simulacao["resultados"]["combustao"]
    eletrico = simulacao["resultados"]["eletrico"]
    economia = simulacao["resultados"]["economia"]
    impacto = simulacao["resultados"]["impacto_ambiental"]
    recomendacao = simulacao["resultados"]["recomendacao"]

    mostrar_titulo(f"DETALHES DA SIMULAÇÃO #{simulacao['id']}")

    print(f"⭐ Viabilidade: {formatar_score(recomendacao['score_viabilidade'])}")
    print(f"🎯 Perfil da simulação: {recomendacao['perfil_usuario']}")
    print(f"📌 Recomendação: {recomendacao['recomendacao']}")

    print("\n" + "-" * 50)
    print("🚗 DADOS DA SIMULAÇÃO")
    print("-" * 50)
    print(f"Categoria escolhida: {entradas['categoria_veiculo'].upper()}")
    print(f"Prioridade informada: {entradas['prioridade_usuario']}")
    print(f"Quilometragem mensal: {entradas['quilometragem_mensal']} km")
    print(f"Anos simulados: {entradas['anos']}")

    print("\n" + "-" * 50)
    print("💰 COMPARAÇÃO FINANCEIRA")
    print("-" * 50)
    print(f"Custo anual com combustível: {formatar_moeda(combustao['custo_combustivel_anual'])}")
    print(f"Custo anual com energia: {formatar_moeda(eletrico['custo_eletrico_anual'])}")
    print(f"Economia anual estimada: {formatar_moeda(economia['economia_anual'])}")
    print(f"Economia acumulada no período: {formatar_moeda(economia['economia_total'])}")
    print(f"Saldo final considerando diferença dos veículos: {formatar_moeda(economia['economia_real'])}")

    if economia["tempo_retorno"] == -1:
        print("Tempo de retorno: não se paga no período analisado")
    elif economia["tempo_retorno"] == 0:
        print("Tempo de retorno: imediato, pois não há investimento adicional")
    else:
        print(f"Tempo de retorno: aproximadamente {economia['tempo_retorno']:.1f} anos")

    print("\n" + "-" * 50)
    print("🌱 IMPACTO AMBIENTAL")
    print("-" * 50)
    print(f"CO₂ evitado: {formatar_numero(impacto['economia_co2'])} kg")
    print(f"Equivalência ambiental: aproximadamente {impacto['equivalencia_arvores']:.0f} árvores")

    print("\n" + "-" * 50)
    print("📌 FATORES DA RECOMENDAÇÃO")
    print("-" * 50)

    if recomendacao["fatores"]:
        for fator in recomendacao["fatores"]:
            print(f"• {fator}")
    else:
        print("• Nenhum fator de destaque identificado.")

    print("\n" + "-" * 50)
    print("🧠 INTERPRETAÇÃO")
    print("-" * 50)
    print(recomendacao["mensagem_prioridade"])




def editar_simulacao(usuario, simulacao_escolhida):
    limpar_tela()

    id_simulacao = simulacao_escolhida["id"]
    dados = simulacao_escolhida["entradas"].copy()
    simulacao_antiga = simulacao_escolhida

    campo_alterado = ""
    valor_antigo = None
    valor_novo = None

    mostrar_titulo(f"EDITAR SIMULAÇÃO #{id_simulacao}")

    print("Você pode alterar uma informação da simulação por vez.")
    print("Após a alteração, os resultados serão recalculados automaticamente.\n")

    print("-" * 50)
    print("📌 DADOS ATUAIS")
    print("-" * 50)
    print(f"Preço do carro atual: {formatar_moeda(dados['preco_carro_atual'])}")
    print(f"Preço da gasolina: {formatar_moeda(dados['preco_gasolina'])}")
    print(f"Preço da energia: {formatar_moeda(dados['preco_energia'])}")
    print(f"Quilometragem mensal: {dados['quilometragem_mensal']} km")
    print(f"Consumo do veículo atual: {dados['consumo_km_l']} km/L")
    print(f"Manutenção anual: {formatar_moeda(dados['manutencao_anual_combustao'])}")
    print(f"IPVA anual: {formatar_moeda(dados['ipva'])}")
    print(f"Seguro anual: {formatar_moeda(dados['seguro'])}")
    print(f"Categoria do veículo: {dados['categoria_veiculo'].upper()}")
    print(f"Prioridade: {dados['prioridade_usuario']}")
    print(f"Anos simulados: {dados['anos']}")

    print("\nO que deseja alterar?\n")
    print("1 - 🚗 Preço do carro atual")
    print("2 - ⛽ Preço da gasolina")
    print("3 - ⚡ Preço da energia")
    print("4 - 📍 Quilometragem mensal")
    print("5 - ⛽ Consumo do veículo atual")
    print("6 - 🛠️ Manutenção anual")
    print("7 - 💸 IPVA anual")
    print("8 - 🛡️ Seguro anual")
    print("9 - 🚙 Categoria do veículo elétrico")
    print("10 - 🎯 Prioridade da simulação")
    print("11 - 📅 Quantidade de anos")
    print("12 - ↩️ Cancelar edição")

    opcao = ler_opcao(
        "Escolha uma opção: ",
        ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
    )

    if opcao == "1":
        campo_alterado = "Preço do carro atual"
        valor_antigo = dados["preco_carro_atual"]
        dados["preco_carro_atual"] = ler_float("Novo valor aproximado do carro atual (R$): ")
        valor_novo = dados["preco_carro_atual"]

    elif opcao == "2":
        campo_alterado = "Preço da gasolina"
        valor_antigo = dados["preco_gasolina"]
        dados["preco_gasolina"] = ler_float("Novo preço da gasolina por litro (R$): ")
        valor_novo = dados["preco_gasolina"]

    elif opcao == "3":
        campo_alterado = "Preço da energia"
        valor_antigo = dados["preco_energia"]
        dados["preco_energia"] = ler_float("Novo preço da energia (R$/kWh): ")
        valor_novo = dados["preco_energia"]

    elif opcao == "4":
        campo_alterado = "Quilometragem mensal"
        valor_antigo = dados["quilometragem_mensal"]
        dados["quilometragem_mensal"] = ler_float("Quantos km, em média, você roda por mês com seu carro? ")
        valor_novo = dados["quilometragem_mensal"]

    elif opcao == "5":
        campo_alterado = "Consumo do veículo atual"
        valor_antigo = dados["consumo_km_l"]
        dados["consumo_km_l"] = ler_float(
            "Quantos km seu carro faz com 1 litro de Combustível? ",
            permitir_zero=False,
        )
        valor_novo = dados["consumo_km_l"]

    elif opcao == "6":
        campo_alterado = "Manutenção anual"
        valor_antigo = dados["manutencao_anual_combustao"]
        dados["manutencao_anual_combustao"] = ler_float("Quanto você gasta, em média, por ano com manutenção? R$ ")
        valor_novo = dados["manutencao_anual_combustao"]

    elif opcao == "7":
        campo_alterado = "IPVA anual"
        valor_antigo = dados["ipva"]
        dados["ipva"] = ler_float("Novo valor anual do IPVA (R$): ")
        valor_novo = dados["ipva"]

    elif opcao == "8":
        campo_alterado = "Seguro anual"
        valor_antigo = dados["seguro"]
        dados["seguro"] = ler_float("Novo valor anual do seguro (R$): ")
        valor_novo = dados["seguro"]

    elif opcao == "9":
        campo_alterado = "Categoria do veículo elétrico"
        valor_antigo = dados["categoria_veiculo"]
        dados["categoria_veiculo"] = ler_menu_opcoes(
            "Qual categoria de carro elétrico você pretende comparar?",
            {
                "1": {"label": "Popular", "valor": "popular"},
                "2": {"label": "SUV", "valor": "suv"},
                "3": {"label": "Luxo", "valor": "luxo"},
            },
        )
        valor_novo = dados["categoria_veiculo"]

    elif opcao == "10":
        campo_alterado = "Prioridade da simulação"
        valor_antigo = dados["prioridade_usuario"]
        dados["prioridade_usuario"] = ler_menu_opcoes(
            "O que mais pesa na sua decisão?",
            {
                "1": {"label": "Economia", "valor": "economia"},
                "2": {"label": "Sustentabilidade", "valor": "sustentabilidade"},
                "3": {"label": "Equilíbrio", "valor": "equilibrio"},
            },
        )
        valor_novo = dados["prioridade_usuario"]

    elif opcao == "11":
        campo_alterado = "Quantidade de anos"
        valor_antigo = dados["anos"]
        dados["anos"] = ler_int(
            "Por quantos anos você quer simular essa comparação? ",
            permitir_zero=False,
        )
        valor_novo = dados["anos"]

    elif opcao == "12":
        print("\nEdição cancelada.")
        return

    nova_simulacao = processar_simulacao(usuario, dados)

    sucesso = atualizar_simulacao(
        email=usuario["email"],
        id_simulacao=id_simulacao,
        nova_simulacao=nova_simulacao,
    )

    if sucesso:
        print("\n✅ Simulação atualizada com sucesso!")
        loading("Recalculando impacto da alteração")
        mostrar_impacto_edicao(
            simulacao_antiga,
            nova_simulacao,
            campo_alterado,
            valor_antigo,
            valor_novo,
        )
    else:
        print("\n❌ Erro ao atualizar simulação.")




def excluir_simulacao_interface(usuario, simulacao_escolhida):
    limpar_tela()

    id_simulacao = simulacao_escolhida["id"]
    entradas = simulacao_escolhida["entradas"]
    economia = simulacao_escolhida["resultados"]["economia"]
    recomendacao = simulacao_escolhida["resultados"]["recomendacao"]

    mostrar_titulo(f"EXCLUIR SIMULAÇÃO #{id_simulacao}")

    print("⚠️ Atenção: esta ação não poderá ser desfeita.\n")
    print("Você está prestes a excluir a seguinte simulação:\n")

    print("-" * 50)
    print(f"🚗 Categoria: {entradas['categoria_veiculo'].upper()}")
    print(f"🎯 Perfil: {recomendacao['perfil_usuario']}")
    print(f"💰 Economia total: {formatar_moeda(economia['economia_total'])}")
    print(f"⭐ Viabilidade: {formatar_score(recomendacao['score_viabilidade'])}")
    print("-" * 50)

    print("\nDeseja realmente excluir esta simulação?")
    print("1 - Sim, excluir definitivamente")
    print("2 - Não, voltar ao histórico")

    opcao = ler_opcao("Escolha uma opção: ", ["1", "2"])

    if opcao == "1":
        sucesso = excluir_simulacao(usuario["email"], id_simulacao)

        if sucesso:
            print("\n✅ Simulação excluída com sucesso!")
        else:
            print("\n❌ Erro ao excluir simulação.")
    else:
        print("\nExclusão cancelada.")



        
def confirmar_saida():
    limpar_tela()
    mostrar_titulo("ENCERRAR ECOTRANSITION")

    print("Você está prestes a sair do sistema.\n")
    print("Deseja realmente encerrar agora?")
    print("1 - Sim, sair")
    print("2 - Não, voltar ao menu")

    opcao = ler_opcao("Escolha uma opção: ", ["1", "2"])

    return opcao == "1"




def mostrar_tela_saida():
    limpar_tela()

    print("=" * 60)
    print("ECOTRANSITION 🌱⚡".center(60))
    print("=" * 60)

    print("\nObrigado por usar o EcoTransition!\n")
    print("Esperamos que a análise tenha ajudado você")
    print("a tomar uma decisão mais consciente sobre")
    print("mobilidade, economia e sustentabilidade.\n")

    print("Pequenas escolhas hoje podem gerar")
    print("grandes impactos amanhã. 🌱\n")




if __name__ == "__main__":
    mostrar_boas_vindas()
    usuario = identificar_usuario()
    menu_principal(usuario)