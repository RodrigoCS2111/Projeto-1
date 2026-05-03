# Projeto-1
Repositório Projeto 1
# Equipe

**Eduardo Américo**
Líder Técnico

Responsabilidades:
Define a arquitetura e garante a viabilidade técnica
Valida a lógica dos cálculos e integrações
Orienta o desenvolvedor e revisa entregas críticas
Assegura qualidade, performance e coerência técnica da solução.
E-mail: eabs2@cesar.school

**Natan Araújo**
Desenvolvedor

Responsabilidades:
Implementar as funcionalidades e interfaces
Garantir o funcionamento dos cálculos
Realiza testes e correções contínuas
Assegura performance e estabilidade do sistema.

E-mail: nga@cesar.school

**Rodrigo Carvalho Silva**
Gerente de Projeto

Responsabilidades:
Planeja cronograma, prioridades e entregas
Garante alinhamento com requisitos e problema investigado
Facilita comunicação e remove impedimentos
Acompanha riscos, prazos e prepara materiais de apresentação

E-mail: rcs8@cesar.school

# Visão Geral
O EcoTransition é uma ferramenta em Python desenvolvida para ajudar usuários a avaliar se vale a pena trocar um veículo a combustão por um veículo elétrico.
O sistema realiza comparações financeiras, ambientais e operacionais, apresentando:

Economia total e anual

Economia de abastecimento e manutenção

Redução de CO₂ e equivalência em árvores

Score de viabilidade (1 a 5)

Recomendação final explicada

Tempo de retorno do investimento (payback)

Histórico de simulações (CRUD)

# Objetivo do Projeto

O objetivo é fornecer uma solução simples, funcional e acessível em ambiente de terminal, permitindo que qualquer usuário — mesmo leigo — consiga entender os impactos financeiros e ambientais da troca de veículo.

# Principais funcionalidades

**Calculadora de Comparação**

Cálculo de custos de combustível e energia

Economia anual e total

Economia de manutenção

Redução de CO₂ e equivalência em árvores

**Score de Viabilidade**

Nota de 1 a 5 baseada nos resultados

Explicação dos fatores que influenciaram a nota

**Sistema de Recomendação Explicada**

Indica se vale a pena trocar

Justifica com base no perfil e nos dados do usuário

**Classificação do Perfil do Usuário**

Econômico

Sustentável

Indeciso

**Histórico de Simulações (CRUD)**

Salvar

Visualizar

Atualizar

Excluir

**Cálculo de Payback**

Estima em quantos anos o investimento no carro elétrico se paga

# Dados de entrada

Preço do carro atual

Preço da gasolina

Preço da energia

Quilometragem mensal

Consumo do veículo (km/L)

Categoria do veículo elétrico (popular, intermediário, SUV)

Prioridade (econômica, ambiental, equilibrada)

IPVA, seguro e manutenção

Quantidade de anos para simulação

# Dados de saída

Economia geral (anual e total)

Economia de abastecimento

Economia de manutenção

Custo para abastecer o tanque

Custo para carregar a bateria

Redução de CO₂

Equivalência em árvores

Score de viabilidade

Recomendação final explicada

Tempo de retorno do investimento

# Requisitos funcionais (Resumo)

Entrada de dados do usuário

Seleção de categoria do veículo elétrico

Uso de valores médios pré-definidos

Cálculo de custos, economia, CO₂ e payback

Geração de score e recomendação

Classificação do perfil

CRUD de simulações

Armazenamento em JSON

# Requisitos não funcionais

Desenvolvido em Python

Interface via terminal

Respostas rápidas e claras

Código organizado e fácil de manter

Tratamento de erros

Dados armazenados em JSON

# Fluxo de funcionamento

1. Identificação do usuário

2. Menu principal

Nova simulação

Visualizar simulações

Sair

3. Entrada de dados

4. Processamento dos cálculos

5. Exibição dos resultados

6. Opção de salvar simulação

7. Gerenciamento de simulações (CRUD)

8. Encerramento