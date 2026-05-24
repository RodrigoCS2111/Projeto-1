# interface.py
import subprocess
import platform
import time


def limpar_tela():
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)


def mostrar_linha():
    print("=" * 50)


def mostrar_titulo(titulo):
    print("\n" + "=" * 50)
    print(titulo.center(50))
    print("=" * 50)


def mostrar_subtitulo(subtitulo):
    print("\n" + "-" * 50)
    print(subtitulo)
    print("-" * 50)


def pausar():
    input("\nPressione ENTER para continuar...")


def loading(mensagem="Processando dados"):
    print(f"\n{mensagem}", end="")

    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")

    print("\n")


def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def formatar_numero(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def mostrar_boas_vindas():
    limpar_tela()

    logo = r"""
  ______        _______                    __   _             
 |  ____|      |__   __|                 (_) | (_)            
 | |__   ___ ___  | |_ __ __ _ _ __  ___  _| |_ _  ___  _ __  
 |  __| / __/ _ \ | | '__/ _` | '_ \/ __|| | __| |/ _ \| '_ \ 
 | |___| (_| (_) || | | | (_| | | | \__ \| | |_| | (_) | | | |
 |______\___\___/ |_|_|  \__,_|_| |_|___/|_|\__|_|\___/|_| |_|
    """

    print(logo)
    print("🌱 Mobilidade inteligente começa com boas decisões.⚡".center(61))

    print("\nBem-vindo ao EcoTransition!\n")

    print("Descubra se migrar de um veículo a combustão para um elétrico")
    print("realmente vale a pena para o seu perfil de uso.\n")

    print("Aqui você poderá:")
    print("💰 Comparar custos entre combustão e elétrico")
    print("🌱 Visualizar o impacto ambiental da troca")
    print("📊 Receber uma análise personalizada")
    print("⭐ Obter uma recomendação final de viabilidade\n")

    input("Pressione ENTER para começar...")

    loading("Inicializando EcoTransition")


def mostrar_progresso(etapa_atual, total_etapas, titulo_etapa):
    tamanho_barra = 20
    progresso = int((etapa_atual / total_etapas) * tamanho_barra)

    barra_preenchida = "█" * progresso
    barra_vazia = "░" * (tamanho_barra - progresso)

    print(f"[{barra_preenchida}{barra_vazia}] Etapa {etapa_atual}/{total_etapas}")
    print(f"{titulo_etapa}\n")


def formatar_score(score):
    estrelas_preenchidas = "⭐" * score
    estrelas_vazias = "☆" * (5 - score)

    return f"{estrelas_preenchidas}{estrelas_vazias} {score}/5"


def gerar_headline(score):
    if score == 5:
        return "Excelente cenário para migração elétrica"
    elif score == 4:
        return "Bom cenário para considerar a troca"
    elif score == 3:
        return "Cenário moderado, exige análise cuidadosa"
    elif score == 2:
        return "Migração pouco vantajosa neste cenário"
    else:
        return "Troca não recomendada financeiramente"


def mostrar_resultado_simulacao(simulacao):
    limpar_tela()
    combustao = simulacao["resultados"]["combustao"]
    eletrico = simulacao["resultados"]["eletrico"]
    economia = simulacao["resultados"]["economia"]
    impacto = simulacao["resultados"]["impacto_ambiental"]
    recomendacao = simulacao["resultados"]["recomendacao"]

    score = recomendacao["score_viabilidade"]

    mostrar_titulo("RESULTADO DA ANÁLISE")

    print(formatar_score(score).center(50))
    print(recomendacao["recomendacao"].upper().center(50))
    print(gerar_headline(score).center(50))

    mostrar_subtitulo("💰 IMPACTO FINANCEIRO")

    print(f"Hoje com seu veículo atual:")
    print(f"{formatar_moeda(combustao['custo_combustivel_anual'])} por ano\n")

    print(f"Com veículo elétrico:")
    print(f"{formatar_moeda(eletrico['custo_eletrico_anual'])} por ano\n")

    print(f"Economia estimada:")
    print(f"💰 {formatar_moeda(economia['economia_anual'])} por ano\n")

    print(f"Economia acumulada no período:")
    print(f"{formatar_moeda(economia['economia_total'])}\n")

    print(f"Saldo final após considerar a diferença de preço dos veículos:")
    print(f"{formatar_moeda(economia['economia_real'])}\n")

    if economia["tempo_retorno"] == -1:
        print(
            "⚠️ Dentro do período analisado, o investimento não se paga financeiramente."
        )
    elif economia["tempo_retorno"] == 0:
        print(
            "⏳ Retorno imediato, pois não há investimento adicional em relação ao carro atual."
        )
    else:
        print(
            f"⏳ O investimento pode se pagar em aproximadamente {economia['tempo_retorno']:.1f} anos."
        )

    mostrar_subtitulo("🌱 IMPACTO AMBIENTAL")

    print(f"CO₂ evitado:")
    print(f"{formatar_numero(impacto['economia_co2'])} kg\n")

    print(f"Equivalente ambiental:")
    print(f"🌳 Aproximadamente {impacto['equivalencia_arvores']:.0f} árvores\n")

    mostrar_subtitulo("🎯 PERFIL DA SIMULAÇÃO")

    print(f"Perfil identificado: {recomendacao['perfil_usuario']}")
    print(f"{recomendacao['mensagem_prioridade']}")

    mostrar_subtitulo("📌 POR QUE CHEGAMOS NESSA CONCLUSÃO")

    if recomendacao["fatores"]:
        for fator in recomendacao["fatores"]:
            print(f"• {fator}")
    else:
        print("• Nenhum fator de destaque identificado.")


def calcular_diferenca(valor_antigo, valor_novo):
    return valor_novo - valor_antigo


def mostrar_variacao_moeda(label, valor_antigo, valor_novo):
    diferenca = calcular_diferenca(valor_antigo, valor_novo)

    print(f"{label}:")
    print(f"Antes: {formatar_moeda(valor_antigo)}")
    print(f"Depois: {formatar_moeda(valor_novo)}")

    if diferenca > 0:
        print(f"Diferença: +{formatar_moeda(diferenca)}\n")
    elif diferenca < 0:
        print(f"Diferença: -{formatar_moeda(abs(diferenca))}\n")
    else:
        print("Diferença: sem alteração\n")


def mostrar_impacto_edicao(
    simulacao_antiga, nova_simulacao, campo_alterado, valor_antigo, valor_novo
):
    economia_antiga = simulacao_antiga["resultados"]["economia"]
    economia_nova = nova_simulacao["resultados"]["economia"]

    recomendacao_antiga = simulacao_antiga["resultados"]["recomendacao"]
    recomendacao_nova = nova_simulacao["resultados"]["recomendacao"]

    mostrar_titulo("IMPACTO DA ALTERAÇÃO")

    print(f"Campo alterado: {campo_alterado}")
    print(f"Valor anterior: {valor_antigo}")
    print(f"Novo valor: {valor_novo}\n")

    mostrar_subtitulo("COMPARAÇÃO DOS RESULTADOS")

    mostrar_variacao_moeda(
        "Economia anual",
        economia_antiga["economia_anual"],
        economia_nova["economia_anual"],
    )

    mostrar_variacao_moeda(
        "Economia total",
        economia_antiga["economia_total"],
        economia_nova["economia_total"],
    )

    mostrar_variacao_moeda(
        "Saldo final", economia_antiga["economia_real"], economia_nova["economia_real"]
    )

    print("Tempo de retorno:")
    print(
        f"Antes: {economia_antiga['tempo_retorno']:.1f} anos"
        if economia_antiga["tempo_retorno"] != -1
        else "Antes: não se paga"
    )
    print(
        f"Depois: {economia_nova['tempo_retorno']:.1f} anos"
        if economia_nova["tempo_retorno"] != -1
        else "Depois: não se paga"
    )

    print("\nScore:")
    print(f"Antes: {formatar_score(recomendacao_antiga['score_viabilidade'])}")
    print(f"Depois: {formatar_score(recomendacao_nova['score_viabilidade'])}")
