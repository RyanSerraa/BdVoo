import pandas as pd 
import numpy as np 
df = pd.read_csv("/home/ryan/Downloads/BrFlights2.csv", encoding="ISO-8859-1")
df_internacional= df.copy()
df_internacional = df_internacional = df[df["Codigo.Tipo.Linha"] == "Internacional"]
df_internacional.to_csv("/home/ryan/trabBD3/BrFlights2_internacional.csv", index=False)

