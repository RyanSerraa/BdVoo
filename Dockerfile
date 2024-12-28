# Use uma imagem base leve com Python
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o script e o arquivo CSV para o container
COPY etl.py .
COPY BrFlights2.csv .

# Instale as dependências necessárias
RUN pip install --no-cache-dir pandas numpy

# Defina o comando padrão para rodar o script
CMD ["python", "etl.py"]
