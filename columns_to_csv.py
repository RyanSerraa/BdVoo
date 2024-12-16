import pandas as pd 
import numpy as np 

# Realiza toda a leitura dos dados do csv
df = pd.read_csv("etl.csv", encoding="ISO-8859-1")

#Trasnforma em csv apens os que são voos internacionais 
df_internacional= df.copy()
df_internacional = df_internacional = df[df["Codigo.Tipo.Linha"] == "Internacional"]
df_internacional.to_csv("BrFlights2_internacional.csv", index=False)

#Selecionar apenas a coluna "Voos"
voos= df.copy()
voos = df[["Voos"]]
voos.to_csv("voos.csv", index=False)

companhiaAerea= df.copy()
companhiaAerea = df[["Companhia.Aerea"]]
companhiaAerea.to_csv("companhiaAerea.csv", index=False)

situacaoVoo= df.copy()
situacaoVoo= df[["Situacao.Voo"]]
situacaoVoo.to_csv("situacaoVoo.csv", index= False)

codigoJustificativa= df.copy()
codigoJustificativa = df[["Codigo.Justificativa"]]
codigoJustificativa.to_csv("codigoJustificativa.csv", index=False)

aeroportoOrigem= df.copy()
aeroportoOrigem = df[["Aeroporto.Origem"]]
aeroportoOrigem.to_csv("aeroportoOrigem.csv", index=False)



aeroportoDestino= df.copy()
aeroportoDestino = df[["Aeroporto.Destino"]]
aeroportoDestino.to_csv("aeroportoDestino.csv", index=False)


paisDestino= df.copy()
paisDestino = df[["Pais.Destino"]]
paisDestino.to_csv("paisDestino.csv", index=False)


paisOrigem= df.copy()
paisOrigem = df[["Pais.Origem"]]
paisOrigem.to_csv("paisOrigem.csv", index=False)

cidadeOrigem= df.copy()
cidadeOrigem = df[["Cidade.Origem"]]
cidadeOrigem.to_csv("cidadeOrigem.csv", index=False)

cidadeDestino= df.copy()
cidadeDestino = df[["Cidade.Destino"]]
cidadeDestino.to_csv("cidadeDestino.csv", index=False)

EstadoOrigem= df.copy()
EstadoOrigem = df[["Estado.Origem"]]
EstadoOrigem.to_csv("estadoOrigem.csv", index=False)

EstadosDestino= df.copy()
EstadosDestino = df[["Estado.Destino"]]
EstadosDestino.to_csv("estadoDestino.csv", index=False)
