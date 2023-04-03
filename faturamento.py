import json

# Ler o arquivo JSON com os dados de faturamento
with open('dados.json') as f:
    data = json.load(f)

# Filtrar os dias úteis (de segunda a sexta-feira)
dias_uteis = [d for d in data if d['dia'] >= 1 and d['dia'] <= 30 and d['dia'] % 7 not in [0, 6]]

# Calcular a média mensal de faturamento
media_mensal = sum(d['valor'] for d in dias_uteis) / len(dias_uteis)

# Encontrar o menor e maior valor de faturamento diário
valores_faturamento = [d['valor'] for d in dias_uteis]
menor_valor = min(valores_faturamento)
maior_valor = max(valores_faturamento)

# Contar o número de dias em que o valor de faturamento diário foi superior à média mensal
dias_acima_media = len([d for d in dias_uteis if d['valor'] > media_mensal])

# Imprimir os resultados
print("Menor valor de faturamento diário:", menor_valor)
print("Maior valor de faturamento diário:", maior_valor)
print("Número de dias com faturamento acima da média mensal:", dias_acima_media)
