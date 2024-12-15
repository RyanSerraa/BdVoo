import pandas as pd

# Ler o arquivo CSV
voos = pd.read_csv("voos.csv")
# Remover os números da coluna "Voos"
voos["Voos"] = voos["Voos"].str.replace(r'\d', '', regex=True)
# Obter os valores únicos da coluna "Voos"
unique_values = voos["Voos"].unique()
# Exibir os valores únicos
print(unique_values)

print('---------------------------------------------------------------------------') #alteração
companhiaAerea= pd.read_csv("companhiaAerea.csv")
companhiaAerea["Companhia.Aerea"] = companhiaAerea["Companhia.Aerea"].str.replace(r'\d', '', regex=True)
# Obter os valores únicos da coluna "Voos"
unique_values = companhiaAerea["Companhia.Aerea"].unique()
# Exibir os valores únicos
print(unique_values)

print('---------------------------------------------------------------------------')
aeroportoDestino= pd.read_csv("aeroportoDestino.csv")
unique_values=aeroportoDestino["Aeroporto.Destino"].unique()
print(unique_values)

print('---------------------------------------------------------------------------')
aeroportoOrigem= pd.read_csv("aeroportoOrigem.csv")
unique_values=aeroportoOrigem["Aeroporto.Origem"].unique()
print(unique_values)

print('---------------------------------------------------------------------------')
codigoJustificativa= pd.read_csv("codigoJustificativa.csv")
unique_values=codigoJustificativa["Codigo.Justificativa"].unique()
print(unique_values)

print('---------------------------------------------------------------------------')
paisOrigem= pd.read_csv("paisOrigem.csv")
unique_values=paisOrigem["Pais.Origem"].unique()
print(unique_values)


print('---------------------------------------------------------------------------')
paisDestino= pd.read_csv("paisDestino.csv")
unique_values=paisDestino["Pais.Destino"].unique()
print(unique_values)

print('---------------------------------------------------------------------------')
situacaoVoo= pd.read_csv("situacaoVoo.csv")
unique_values=situacaoVoo["Situacao.Voo"].unique()
print(unique_values)
