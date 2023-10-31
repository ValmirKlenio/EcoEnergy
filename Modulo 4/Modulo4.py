import random as rd
import pandas as pd
import os

# Informações iniciais
print("Geração média anual esperada: 15.000 kWh")

# Variáveis iniciais
geracao_mensal = 0
meses = {"jan":1,"fev":2,"mar":3,
         "abr":4,"mai":5,"jun":6,
         "jul":7,"ago":8,"set":9,
         "out":10,"nov":11,"dez":12}
alertas_log = {}
eventos_ponderados = [1, 0.8, 0.4, 0.2, 0.0]  # Coeficientes e suas probabilidades
pesos = [0.4, 0.20, 0.20, 0.15, 0.05]         # Pesos dos coeficientes
data = []
anos = [23, 24, 25, 26]
geracao_anual = []
eficiencia_anual = []
total_alertas = 0
baixa_producao = 0
economia = 0

# Cálculo do preço da eletricidade da CELPE
parcelas_financiamento_solar = 60
preco_solar = parcelas_financiamento_solar * 15000
preco_celpe_mensal = 15000 * 1.25

# Loop pelos anos
for ano in anos:
    # Loop pelos meses
    for mes_nome, mes_numero in meses.items():
        # Verificação para meses de inverno
        if mes_numero in [12, 1, 2]:
            for dia in range(1, 30):
                # Geração aleatória
                eventos_aleatorios = rd.choices(eventos_ponderados, weights=pesos)
                aleatoriedade = eventos_aleatorios[0]

                # Verificação e registro de alertas
                if aleatoriedade == 0:
                    total_alertas += 1
                    if mes_nome not in alertas_log:
                        alertas_log[mes_nome] = 1
                    else:
                        alertas_log[mes_nome] += 1

                # Cálculo da eficiência e geração mensal
                eficiencia = rd.uniform(0.9, 0.95)
                geracao_base_dia = 1000 * eficiencia * aleatoriedade
                geracao_mensal += geracao_base_dia
                eficiencia_anual.append(eficiencia)

            # Cálculo da economia e registro dos dados mensais
            economia += preco_celpe_mensal - 15000
            data.append({
                'Mês': f"{mes_nome}/{ano}",
                'Geração Mensal (kWh)': geracao_mensal,
                'Eficiência Média Mensal': sum(eficiencia_anual) / len(eficiencia_anual),
                'Dias com Falha / Geração Comprometida': total_alertas,
                'Economia Mensal': economia
            })

            # Verificação de baixa produção
            if geracao_mensal <= 15000:
                baixa_producao += 1

            # Impressão da geração mensal
            print(f"Geração em {mes_nome}: {geracao_mensal:.0f} kWh")
            geracao_anual.append(geracao_mensal)
            geracao_mensal = 0  # Reiniciar a geração mensal para o próximo mês.

        # Verificação para meses de primavera
        elif mes_numero in [3, 4, 5]:
            for dia in range(1, 30):
                eventos_aleatorios = rd.choices(eventos_ponderados, weights=pesos)
                aleatoriedade = eventos_aleatorios[0]

                if aleatoriedade == 0:
                    total_alertas += 1

                    if mes_nome not in alertas_log:
                        alertas_log[mes_nome] = 1
                    else:
                        alertas_log[mes_nome] += 1

                eficiencia = rd.uniform(0.75, 0.85)
                geracao_base_dia = 1000 * eficiencia * aleatoriedade
                geracao_mensal += geracao_base_dia
                eficiencia_anual.append(eficiencia)
