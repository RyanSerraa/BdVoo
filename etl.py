import pandas as pd
import numpy as np

# Importação do DataFrame
csv = pd.read_csv("BrFlights2.csv", encoding="ISO-8859-1")
df = csv.copy()
# Normalização do Código de Voo
df["Voos"] = df["Voos"].str.replace("GLO", "GOL", regex=True)
df["Voos"] = df["Voos"].str.replace("DSM", "4M", regex=True)
df["Voos"] = df["Voos"].str.replace("LAP", "PZ", regex=True)
df["Voos"] = df["Voos"].str.replace("NLU", "O6", regex=True)
df["Voos"] = df["Voos"].str.replace("PTB", "QTR", regex=True)
# Modifica o que for Regional para Nacional
df["Codigo.Tipo.Linha"] = np.where(
    df["Codigo.Tipo.Linha"].str.contains("Regional"),
    "Nacional",
    df["Codigo.Tipo.Linha"],
)
# Normaliza cidades que na verdade são nacionais e estã listadas como internacionis
df["Codigo.Tipo.Linha"] = np.where(
    df["Pais.Origem"] == "Brasil", "Nacional", df["Codigo.Tipo.Linha"]
)
# Padroniza tudo para -
df["Aeroporto.Origem"] = df["Aeroporto.Origem"].str.replace("/", "-", regex=True)
df["Aeroporto.Destino"] = df["Aeroporto.Destino"].str.replace("/", "-", regex=True)
# Conserta o nome da cidade de Abu Dabhi
df["Cidade.Origem"] = df["Cidade.Origem"].str.replace(
    "Ab Dhabi International", "Abu Dhabi International", regex=True
)
df["Cidade.Destino"] = df["Cidade.Destino"].str.replace(
    "Ab Dhabi International", "Abu Dhabi International", regex=True
)
df["Aeroporto.Origem"] = df["Cidade.Origem"].str.replace(
    "Ab Dhabi International", "Abu Dhabi International", regex=True
)
df["Aeroporto.Destino"] = df["Cidade.Destino"].str.replace(
    "Ab Dhabi International", "Abu Dhabi International", regex=True
)
# Padroniza toda as cidades que não tinham estado de origem ou destino
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Luxemburgo", case=False),
    "LU",
    df["Estado.Origem"],
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Sao Domingo", case=False),
    "DO",
    df["Estado.Origem"],
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Cochabamba", case=False),
    "BO",
    df["Estado.Origem"],
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Charlotte", case=False),
    "NC",
    df["Estado.Origem"],
)  # Carolina do Norte
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Los Angeles", case=False),
    "CA",
    df["Estado.Origem"],
)  # Califórnia
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Dallas", case=False), "TX", df["Estado.Origem"]
)  # Texas
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Mexico", case=False), "MX", df["Estado.Origem"]
)  # México
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Houston", case=False), "TX", df["Estado.Origem"]
)  # Texas
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Abu Dhabi International"),
    "AUH",
    df["Estado.Origem"],
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Addis Ababa"), "ADD", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Amsterdam"), "NH", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Aruba"), "AW", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Assuncao"), "ASU", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Atlanta"), "GA", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Barcelona"), "CT", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Bogota"), "DC", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Bridgetown"), "BB", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Buenos Aires"), "CABA", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Cabo Verde"), "ST", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Caiena"), "GF", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Cancun"), "QR", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Caracas"), "LG", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Casablanca"), "CS", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Cheddi Jagan "), "DM", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Chicago"), "IL", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Cidade Del Este"), "AP", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Cordoba"), "CB", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Curacao"), "CW", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Detroit"), "MI", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Doha"), "DOH", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Dubai International"), "DXB", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Fort Lauderdale"), "FL", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Zurique"), "ZH", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Zandery"), "PM", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Washington/Dulles Intl"),
    "VA",
    df["Estado.Origem"],
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Viru Viru"), "SC", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Toronto"), "ON", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Santiago Do Chile"), "RM", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Rosario"), "SF", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Roma"), "LAZ", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Quito"), "PI", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Punta Cana"), "LA", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"] == "Porto", "POR", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Paris"), "IDF", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Panama"), "PN", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Orlando"), "FL", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Newark / Intl Nj"), "NJ", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("New York"), "NY", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Munchen"), "BY", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Montevideu"), "MVD", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Milao"), "LOM", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Miami"), "FL", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Mendoza"), "MZA", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Maldonado-Uruguai"), "MA", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Madrid"), "MD", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Luanda"), "LUA", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Londres"), "ENG", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Lome"), "MR", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Lisboa"), "LIS", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Lima"), "LMA", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Johannesburg"), "GP", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Istanbul/Ataturk"), "IST", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Ilha Do Sal"), "SAL", df["Estado.Origem"]
)
df["Estado.Origem"] = np.where(
    df["Cidade.Origem"].str.contains("Frankfurt"), "HE", df["Estado.Origem"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Amsterdam"), "NH", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Aruba"), "AW", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Atlanta"), "GA", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Barcelona"), "CT", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Bridgetown"), "BB", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Buenos Aires"), "CABA", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Cabo Verde"), "ST", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Caiena"), "GF", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Caracas"), "LG", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Casablanca"), "CS", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Cheddi Jagan "), "DM", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Chicago"), "IL", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Cidade Del Este"), "AP", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Detroit"), "MI", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Fort Lauderdale"), "FL", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Zandery"), "PM", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Washington/Dulles Intl"),
    "VA",
    df["Estado.Destino"],
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Toronto"), "ON", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Santiago Do Chile"), "RM", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Rosario"), "SF", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Roma"), "LAZ", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Quito"), "PI", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Punta Cana"), "LA", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Paris"), "IDF", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Panama"), "PN", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Orlando"), "FL", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Newark / Intl Nj"), "NJ", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("New York"), "NY", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Munchen"), "BY", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Montevideu"), "MVD", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Milao"), "LOM", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Miami"), "FL", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Mendoza"), "MZA", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Maldonado-Uruguai"), "MA", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Madrid"), "MD", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Luanda"), "LUA", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Londres"), "LDN", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Lome"), "MR", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Lisboa"), "LIS", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Lima"), "LMA", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Johannesburg"), "GP", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Istanbul/Ataturk"), "IST", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Ilha Do Sal"), "SAL", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Los Angeles"), "CA", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Dallas"), "TX", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Mexico"), "MX", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Houston"), "TX", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Rio grande Do Sul"), "RS", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Bahia"), "BA", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Rondonia"), "RO", df["Estado.Destino"]
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Luxemburgo", case=False),
    "LU",
    df["Estado.Destino"],
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Sao Domingo", case=False),
    "DO",
    df["Estado.Destino"],
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Cochabamba", case=False),
    "BO",
    df["Estado.Destino"],
)
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Charlotte", case=False),
    "NC",
    df["Estado.Destino"],
)  # Carolina do Norte
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Los Angeles", case=False),
    "CA",
    df["Estado.Destino"],
)  # Califórnia
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Dallas", case=False), "TX", df["Estado.Destino"]
)  # Texas
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Mexico", case=False), "MX", df["Estado.Destino"]
)  # México
df["Estado.Destino"] = np.where(
    df["Cidade.Destino"].str.contains("Houston", case=False), "TX", df["Estado.Destino"]
)  # Texas

# Normalização do Aeroporto
df["Cidade.Destino"] = np.where(
    df["Aeroporto.Destino"].str.contains("Placido de Castro"),
    "Rio Branco",
    df["Cidade.Destino"],
)

df["Companhia.Aerea"] = np.where(
    df["Companhia.Aerea"].str.contains("AUSTRAL LINEAS A"),
    "AUSTRAL LINEAS AEREAS CIELOS DEL SUR S.A",
    df["Companhia.Aerea"],
)
df["Companhia.Aerea"] = np.where(
    df["Companhia.Aerea"].str.contains("FRICAN AIRWAYS"),
    "SOUTH AFRICAN AIRWAYS",
    df["Companhia.Aerea"],
)
# Normalização código justificativa

df["Codigo.Justificativa"].fillna("Sem justificativa")

df.to_csv("etl.csv", index=False)
