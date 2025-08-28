# simulador-aposentadoria-python.
simulador de aposentadoria feito em Python que calcula o patrimônio necessário com base em metas e rentabilidade.
# Simulador de Aposentadoria em Python

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Um script de linha de comando (CLI) interativo para simular e planejar a aposentadoria. A ferramenta ajuda a determinar se seu plano de investimentos atual é suficiente para atingir suas metas financeiras, calculando o patrimônio futuro e o valor necessário para a renda desejada.

O grande diferencial desta calculadora é o uso da **rentabilidade real** (juros reais), que representa o rendimento dos investimentos já descontando a inflação. Isso proporciona uma projeção mais realista e alinhada ao poder de compra futuro.

## 🚀 Funcionalidades

-   **Interface Interativa:** Coleta de dados através de perguntas simples no terminal.
-   **Projeção de Patrimônio:** Calcula o valor total que você terá acumulado na data da aposentadoria, considerando seu patrimônio atual, aportes mensais e rentabilidade.
-   **Cálculo da Meta Financeira:** Determina o montante necessário para sustentar a renda mensal desejada durante todo o período da aposentadoria.
-   **Análise de Superávit/Déficit:** Compara o valor projetado com a meta necessária e informa claramente se você está no caminho certo.
-   **Sugestão de Aporte Ideal:** Caso haja um déficit, o script calcula o aporte mensal ideal para você atingir sua meta.
-   **Valores Padrão:** Para facilitar o uso, a rentabilidade real já vem com o valor padrão de 4% ao ano, que pode ser alterado durante a execução.

## 🛠️ Como Usar

### Pré-requisitos

-   [Python 3](https://www.python.org/downloads/) instalado em sua máquina.

### Execução

1.  Clone este repositório para o seu computador:
    ```bash
    git clone [https://github.com/seu-usuario/simulador-aposentadoria-python.git](https://github.com/seu-usuario/simulador-aposentadoria-python.git)
    ```

2.  Navegue até a pasta do projeto:
    ```bash
    cd simulador-aposentadoria-python
    ```

3.  Execute o script:
    ```bash
    python simulador_aposentadoria.py
    ```

4.  Responda às perguntas no terminal para obter sua simulação personalizada.

## 📋 Exemplo de Uso

Abaixo, um exemplo de interação com o programa:

```text
--------------------------------------------------
      SIMULADOR DE APOSENTADORIA      
--------------------------------------------------
Vamos descobrir se você está no caminho certo para a sua aposentadoria!
Por favor, preencha os dados abaixo.

Qual é a sua idade atual? : 30
Com que idade você planeja se aposentar? : 65
Quanto você já tem guardado/investido para a aposentadoria? R$ : 50000
Quanto você investe por mês para a aposentadoria? R$ : 1000
Qual a renda mensal que você deseja ter na aposentadoria? R$ : 8000
Até que idade você estima viver (para calcular a duração dos seus fundos)? : 85

--- Parâmetros Financeiros (Estimativas) ---
Rentabilidade anual REAL ANTES de se aposentar (%) (padrão: 4.0): 
Rentabilidade anual REAL DEPOIS de se aposentar (%) (padrão: 4.0): 

==================================================
         RESULTADO DA SIMULAÇÃO         
==================================================

Você planeja se aposentar em 35 anos, aos 65 anos.
Sua aposentadoria precisará durar por 20 anos (até os 85 anos).

--- Projeção do seu Patrimônio ---
Com seus aportes e rentabilidade estimada, seu patrimônio ao se aposentar será de: R$ 1.097.350,91

--- Sua Meta de Aposentadoria ---
Para ter uma renda de R$ 8.000,00 por mês, você precisaria de um patrimônio de: R$ 1.324.018,63

--- Conclusão ---
❌ ATENÇÃO! Seu plano atual pode não ser suficiente.
Sua projeção indica um DÉFICIT de R$ 226.667,72.

Para atingir sua meta, você poderia:
  - Aumentar seu aporte mensal para aproximadamente R$ 1.282,12.
  - Buscar uma rentabilidade maior nos seus investimentos.
  - Ajustar a idade de aposentadoria ou a renda mensal desejada.
