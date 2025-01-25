
import pandas as pd
import csv
import json

# Nome do arquivo CSV de entrada
csv_file = 'etl.csv'
# Nome do arquivo JSON de saída
json_file = 'dump.json'

# Carregar o arquivo CSV
df = pd.read_csv(csv_file)

# Amostrar 1% dos dados (ajuste a proporção conforme necessário)
sampled_df = df.sample(frac=0.25, random_state=42)  # random_state para reprodutibilidade

# Salvar o novo arquivo CSV
sampled_df.to_csv('prepareted.csv', index=False)

csv_file= "prepareted.csv"
# Abrindo o arquivo CSV e lendo os dados
with open(csv_file, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    # Convertendo as linhas do CSV em uma lista de dicionários
    data = [row for row in csv_reader]

# Salvando os dados em JSON
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print(f"Arquivo JSON criado: {json_file}")
