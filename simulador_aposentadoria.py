import math

def formatar_moeda(valor):
    """
    Formata um número como moeda brasileira (R$) de forma manual,
    sem depender do pacote de localização do sistema.
    """
    if not math.isfinite(valor):
        return "R$ (valor inválido)"
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# --- ALTERAÇÃO 1: Função modificada para aceitar um valor padrão ---
def obter_input_numerico(pergunta, padrao=None):
    """
    Função para garantir que o usuário insira um número válido.
    Aceita um valor padrão que é usado se o usuário apenas pressionar Enter.
    """
    while True:
        # Mostra o valor padrão na pergunta, se ele existir
        prompt = pergunta
        if padrao is not None:
            prompt = f"{pergunta} (padrão: {padrao}): "
        else:
            prompt = f"{pergunta}: "

        entrada = input(prompt)
        # Se a entrada for vazia e houver um padrão, usa o padrão
        if not entrada and padrao is not None:
            return float(padrao)

        try:
            valor = float(entrada)
            if valor < 0:
                print("Por favor, insira um valor positivo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira apenas números.")

def simulador_aposentadoria():
    """
    Função principal que coleta dados e simula o planejamento de aposentadoria.
    """
    print("-" * 50)
    print("      SIMULADOR DE APOSENTADORIA      ")
    print("-" * 50)
    print("Vamos descobrir se você está no caminho certo para a sua aposentadoria!")
    print("Por favor, preencha os dados abaixo.\n")

    idade_atual = int(obter_input_numerico("Qual é a sua idade atual? "))
    idade_aposentadoria = int(obter_input_numerico("Com que idade você planeja se aposentar? "))
    patrimonio_atual = obter_input_numerico("Quanto você já tem guardado/investido para a aposentadoria? R$ ")
    aporte_mensal = obter_input_numerico("Quanto você investe por mês para a aposentadoria? R$ ")
    salario_desejado_aposentadoria = obter_input_numerico("Qual a renda mensal que você deseja ter na aposentadoria? R$ ")
    expectativa_vida = int(obter_input_numerico("Até que idade você estima viver (para calcular a duração dos seus fundos)? "))

    print("\n--- Parâmetros Financeiros (Estimativas) ---")
    
    # --- ALTERAÇÃO 2: Usando o valor padrão de 4% nas perguntas ---
    rentabilidade_anual_acumulacao = obter_input_numerico("Rentabilidade anual REAL ANTES de se aposentar (%)", padrao=4.0) / 100
    rentabilidade_anual_retirada = obter_input_numerico("Rentabilidade anual REAL DEPOIS de se aposentar (%)", padrao=4.0) / 100

    # --- O restante do código permanece o mesmo ---
    anos_para_aposentar = idade_aposentadoria - idade_atual
    meses_para_aposentar = anos_para_aposentar * 12
    anos_aposentado = expectativa_vida - idade_aposentadoria
    meses_aposentado = anos_aposentado * 12

    if anos_para_aposentar <= 0:
        print("\nA idade de aposentadoria deve ser maior que a idade atual.")
        return

    taxa_mensal_acumulacao = (1 + rentabilidade_anual_acumulacao)**(1/12) - 1
    vf_patrimonio_atual = patrimonio_atual * ((1 + taxa_mensal_acumulacao) ** meses_para_aposentar)

    vf_aportes = 0
    if taxa_mensal_acumulacao > 0:
        vf_aportes = aporte_mensal * ((((1 + taxa_mensal_acumulacao) ** meses_para_aposentar) - 1) / taxa_mensal_acumulacao)
    else:
        vf_aportes = aporte_mensal * meses_para_aposentar

    patrimonio_total_ao_aposentar = vf_patrimonio_atual + vf_aportes

    taxa_mensal_retirada = (1 + rentabilidade_anual_retirada)**(1/12) - 1
    
    patrimonio_necessario = 0
    if taxa_mensal_retirada > 0:
        patrimonio_necessario = salario_desejado_aposentadoria * ((1 - (1 + taxa_mensal_retirada)**-meses_aposentado) / taxa_mensal_retirada)
    else:
        patrimonio_necessario = salario_desejado_aposentadoria * meses_aposentado

    print("\n" + "="*50)
    print("         RESULTADO DA SIMULAÇÃO         ")
    print("="*50)
    print(f"\nVocê planeja se aposentar em {anos_para_aposentar} anos, aos {idade_aposentadoria} anos.")
    print(f"Sua aposentadoria precisará durar por {anos_aposentado} anos (até os {expectativa_vida} anos).")
    
    print("\n--- Projeção do seu Patrimônio ---")
    print(f"Com seus aportes e rentabilidade estimada, seu patrimônio ao se aposentar será de: {formatar_moeda(patrimonio_total_ao_aposentar)}")

    print("\n--- Sua Meta de Aposentadoria ---")
    print(f"Para ter uma renda de {formatar_moeda(salario_desejado_aposentadoria)} por mês, você precisaria de um patrimônio de: {formatar_moeda(patrimonio_necessario)}")

    print("\n--- Conclusão ---")
    diferenca = patrimonio_total_ao_aposentar - patrimonio_necessario
    if diferenca >= 0:
        print("✅ PARABÉNS! Você está no caminho certo!")
        print(f"Sua projeção indica um SUPERÁVIT de {formatar_moeda(diferenca)}.")
        print("Você pode até mesmo considerar se aposentar mais cedo ou com uma renda maior.")
    else:
        print("❌ ATENÇÃO! Seu plano atual pode não ser suficiente.")
        print(f"Sua projeção indica um DÉFICIT de {formatar_moeda(abs(diferenca))}.")
        
        aporte_ideal = 0
        if taxa_mensal_acumulacao > 0:
            denominador = ((((1 + taxa_mensal_acumulacao) ** meses_para_aposentar) - 1) / taxa_mensal_acumulacao)
            if denominador > 0:
                 aporte_ideal = (patrimonio_necessario - vf_patrimonio_atual) / denominador
        else:
            if meses_para_aposentar > 0:
                aporte_ideal = (patrimonio_necessario - vf_patrimonio_atual) / meses_para_aposentar

        print("\nPara atingir sua meta, você poderia:")
        if aporte_ideal > aporte_mensal:
            print(f"  - Aumentar seu aporte mensal para aproximadamente {formatar_moeda(aporte_ideal)}.")
        print("  - Buscar uma rentabilidade maior nos seus investimentos.")
        print("  - Ajustar a idade de aposentadoria ou a renda mensal desejada.")

    print("\n" + "-"*50)
    print("Lembre-se: esta é uma simulação simplificada e não constitui uma recomendação financeira.")
    print("-" * 50)

if __name__ == "__main__":
    simulador_aposentadoria()
