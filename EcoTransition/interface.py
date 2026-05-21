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
  ______          _______                    __   _             
 |  ____|        |__   __|                 (_) | (_)            
 | |__   ___ ___    | |_ __ __ _ _ __  ___  _| |_ _  ___  _ __  
 |  __| / __/ _ \   | | '__/ _` | '_ \/ __|| | __| |/ _ \| '_ \ 
 | |___| (_| (_) |  | | | | (_| | | | \__ \| | |_| | (_) | | | |
 |______\___\___/   |_|_|  \__,_|_| |_|___/|_|\__|_|\___/|_| |_|
    """

    print(logo)
    print("🌱 Mobilidade inteligente começa com boas decisões.⚡".center(62))

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




def mostrar_resultado_simulacao(simulacao):
    combustao = simulacao["resultados"]["combustao"]
    eletrico = simulacao["resultados"]["eletrico"]
    economia = simulacao["resultados"]["economia"]
    impacto = simulacao["resultados"]["impacto_ambiental"]
    recomendacao = simulacao["resultados"]["recomendacao"]

    mostrar_titulo("RESULTADO DA SIMULAÇÃO")

    mostrar_subtitulo("RESULTADOS FINANCEIROS")
    print(f"Custo anual com combustível: {formatar_moeda(combustao['custo_combustivel_anual'])}")
    print(f"Custo anual com energia: {formatar_moeda(eletrico['custo_eletrico_anual'])}")
    print(f"Economia anual estimada: {formatar_moeda(economia['economia_anual'])}")
    print(f"Economia total no período: {formatar_moeda(economia['economia_total'])}")
    print(f"Economia real considerando investimento: {formatar_moeda(economia['economia_real'])}")

    if economia["tempo_retorno"] == -1:
      print("Tempo de retorno: não se paga no período analisado")
    elif economia["tempo_retorno"] == 0:
     print("Tempo de retorno: imediato, pois não há investimento adicional")
    else:
     print(f"Tempo de retorno: {economia['tempo_retorno']:.1f} anos")

    mostrar_subtitulo("IMPACTO AMBIENTAL")
    print(f"Redução estimada de CO₂: {formatar_numero(impacto['economia_co2'])} kg")
    print(f"Equivalente a aproximadamente {impacto['equivalencia_arvores']:.0f} árvores")

    mostrar_subtitulo("RECOMENDAÇÃO")
    
    print(f"Score de viabilidade: {recomendacao['score_viabilidade']}/5")
    print(f"Perfil da simulação: {recomendacao['perfil_usuario']}")
    print(f"Recomendação: {recomendacao['recomendacao']}")
    print(f"Mensagem: {recomendacao['mensagem_prioridade']}")

    print("\nPrincipais fatores:")
    if recomendacao["fatores"]:
        for fator in recomendacao["fatores"]:
            print(f"- {fator}")
    else:
        print("- Nenhum fator de destaque identificado.")