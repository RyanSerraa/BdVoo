import pandas as pd

# Ler o arquivo CSV
voos = pd.read_csv("voos.csv")
# Remover os números da coluna "Voos"
voos["Voos"] = voos["Voos"].str.replace(r'\d', '', regex=True)
# Obter os valores únicos da coluna "Voos"
unique_values = voos["Voos"].unique()
# Exibir os valores únicos
print('-------------------------------Código de VOO----------------------------------------') #alteração
print(unique_values)

print('-------------------------------------Companhia Aerea-------------------------------') #alteração
companhiaAerea= pd.read_csv("companhiaAerea.csv")
companhiaAerea["Companhia.Aerea"] = companhiaAerea["Companhia.Aerea"].str.replace(r'\d', '', regex=True)
# Obter os valores únicos da coluna "Voos"
unique_values = companhiaAerea["Companhia.Aerea"].unique()
# Exibir os valores únicos
print(unique_values)

print('--------------------------------------------Aeroporto Destino----------------------------')
aeroportoDestino= pd.read_csv("aeroportoDestino.csv")
unique_values=aeroportoDestino["Aeroporto.Destino"].unique()
print(unique_values)

print('------------------------------------------Aeroporto Origem-----------------------------')
aeroportoOrigem= pd.read_csv("aeroportoOrigem.csv")
unique_values=aeroportoOrigem["Aeroporto.Origem"].unique()
print(unique_values)

print('-----------------------------------------------Código Justificativa------------------------')
codigoJustificativa= pd.read_csv("codigoJustificativa.csv")
unique_values=codigoJustificativa["Codigo.Justificativa"].unique()
print(unique_values)

print('-------------------------------------------------Pais Origem---------------------')
paisOrigem= pd.read_csv("paisOrigem.csv")
unique_values=paisOrigem["Pais.Origem"].unique()
print(unique_values)


print('-------------------------------------------------------Pais Destino----------------')
paisDestino= pd.read_csv("paisDestino.csv")
unique_values=paisDestino["Pais.Destino"].unique()
print(unique_values)

print('------------------------------------Situação Voo---------------------------------')
situacaoVoo= pd.read_csv("situacaoVoo.csv")
unique_values=situacaoVoo["Situacao.Voo"].unique()
print(unique_values)


print('------------------------------------Cidade Origem---------------------------------')
cidadeOrigem= pd.read_csv("cidadeOrigem.csv")
unique_values=cidadeOrigem["Cidade.Origem"].unique()
print(unique_values)

print('------------------------------------Cidade Destino---------------------------------')
cidadeDestino= pd.read_csv("cidadeDestino.csv")
unique_values=cidadeDestino["Cidade.Destino"].unique()
print(unique_values)

print('------------------------------------Estado Origem---------------------------------')
EstadoOrigem= pd.read_csv("estadoOrigem.csv")
unique_values=EstadoOrigem["Estado.Origem"].unique()
print(unique_values)

print('------------------------------------Estado Destino---------------------------------')
EstadoDestino= pd.read_csv("estadoDestino.csv")
unique_values=EstadoDestino["Estado.Destino"].unique()
print(unique_values)
