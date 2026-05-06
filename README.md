# EcoTransition 🌱⚡

Sistema de apoio à decisão para migração de veículos a combustão para veículos elétricos.

---

# 📖 Sobre o Projeto

O **EcoTransition** é uma aplicação desenvolvida em Python com o objetivo de auxiliar usuários na tomada de decisão sobre a troca de veículos a combustão por veículos elétricos.

O sistema realiza comparações financeiras e ambientais, utilizando dados fornecidos pelo usuário e valores médios previamente definidos para diferentes categorias de veículos elétricos.

A proposta do projeto é tornar a análise mais simples, acessível e compreensível, permitindo que usuários leigos consigam visualizar os impactos econômicos e sustentáveis da mudança de veículo.

---

# 🎯 Objetivo

Desenvolver uma ferramenta em Python capaz de:

- Comparar custos entre veículos a combustão e elétricos
- Estimar economia financeira
- Calcular impacto ambiental
- Gerar recomendações inteligentes
- Auxiliar o usuário na tomada de decisão

---

# 🚀 Funcionalidades

## 📊 Calculadora Comparativa
- Cálculo de custos de combustível e energia
- Economia anual e total
- Economia de manutenção
- Comparação de custo operacional

---

## ⭐ Score de Viabilidade
O sistema gera uma nota de viabilidade de aquisição baseada em:
- Tempo de retorno do investimento
- Economia total
- Perfil do usuário

---

## 🧠 Sistema de Recomendação
Além de informar se vale a pena ou não realizar a troca, o sistema também explica os principais fatores que influenciaram a decisão.

Exemplo:
> “Vale a pena devido à alta quilometragem mensal e ao elevado custo atual com combustível.”

---

## 🌱 Impacto Ambiental
- Estimativa de redução de emissão de CO₂
- Equivalência em árvores preservadas

---

## 👤 Perfil do Usuário
Classificação automática baseada nas escolhas do usuário:
- Econômico
- Sustentável
- Equilibrado

---

## 💾 Histórico de Simulações (CRUD)
O sistema permite:
- Salvar simulações
- Visualizar histórico
- Atualizar simulações
- Excluir simulações

---

# 📥 Informações Utilizadas

O sistema utiliza informações financeiras e operacionais do veículo do usuário, como:

- Custos de combustível e energia
- Quilometragem mensal
- Consumo do veículo
- Custos anuais
- Categoria do veículo elétrico

---

# 📤 Resultados Gerados

O sistema apresenta:

- Economia financeira
- Tempo de retorno do investimento
- Score de viabilidade
- Recomendação personalizada
- Impacto ambiental

---

# 🛠 Tecnologias Utilizadas

- Python
- JSON
- Figma
- Git & GitHub

---

# 🧱 Estrutura do Projeto

EcoTransition/
│
├── database/
│   └── simulacoes.json
│
├── main.py
├── calculos.py
├── crud.py
├── dados.py
└── validacoes.py

# 🔄 Fluxo de Funcionamento

```plaintext
Usuário → Entrada de Dados → Processamento →
Resultados → Recomendação → Histórico
```

---

# 🖥 Como Executar o Projeto

## 1. Clone o repositório

```bash
git clone https://github.com/RodrigoCS2111/Projeto-1.git
```

---

## 2. Acesse a pasta do projeto

```bash
cd EcoTransition
```

---

## 3. Execute o sistema

```bash
python main.py
```

---

# 🎨 Protótipo

O protótipo da interface foi desenvolvido no Figma, contemplando:

- Home
- Menu principal
- Entrada de dados
- Resultado da análise
- Recomendação
- Impacto ambiental
- CRUD de simulações

---

# 👥 Equipe

## Eduardo Américo — Líder Técnico

Responsável por:

- Arquitetura do sistema
- Modelagem lógica
- Integração dos módulos
- Revisão técnica
- Garantia da viabilidade da solução

📧 eabs2@cesar.school

---

## Natan Araújo — Desenvolvedor

Responsável por:

- Desenvolvimento das funcionalidades
- Implementação dos cálculos
- Testes e correções
- Estabilidade do sistema

📧 nga@cesar.school

---

## Rodrigo Carvalho Silva — Gerente de Projeto

Responsável por:

- Planejamento do projeto
- Organização das entregas
- Gestão de cronograma
- Comunicação da equipe
- Preparação da apresentação

📧 rcs8@cesar.school

---

# 📌 Status do Projeto

🚧 Em desenvolvimento

---

# 🌍 Impacto Esperado

O EcoTransition busca incentivar decisões mais conscientes relacionadas à mobilidade sustentável, contribuindo para a transição energética e para a redução do impacto ambiental causado por veículos a combustão.