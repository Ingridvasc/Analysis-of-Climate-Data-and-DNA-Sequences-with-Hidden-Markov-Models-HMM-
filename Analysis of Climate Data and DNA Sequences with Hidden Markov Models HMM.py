import numpy as np
import pandas as pd
import plotly.graph_objects as go
from collections import Counter
import matplotlib.pyplot as plt
from hmmlearn import hmm
import requests

# === Geração dos dados e do DNA === #
def generate_dna_sequence(length=1000):
    """Gera uma sequência aleatória de DNA."""
    return ''.join(np.random.choice(['A', 'C', 'G', 'T'], size=length))

def calculate_frequencies(sequence):
    """Calcula a frequência relativa de cada base (A, C, G, T) em uma sequência."""
    counts = Counter(sequence)
    total = sum(counts.values())
    return {base: counts[base] / total for base in ['A', 'C', 'G', 'T']}

def generate_candlestick_data():
    """
    Gera dados simulados para candlesticks a partir de sequências genéticas,
    com uma mudança em frequências após certo ponto.
    """
    pre_change_sequences = [generate_dna_sequence(1000) for _ in range(10)]
    post_change_sequences = [generate_dna_sequence(1000) for _ in range(10)]
    
    # Alterar padrão após mudança ambiental
    for i in range(len(post_change_sequences)):
        post_change_sequences[i] = ''.join(np.random.choice(['A', 'C'], size=1000))  # Enfatiza mutação para A e C

    # Frequências antes e depois da mudança
    pre_change_freqs = [calculate_frequencies(seq) for seq in pre_change_sequences]
    post_change_freqs = [calculate_frequencies(seq) for seq in post_change_sequences]
    
    # Combinar em um DataFrame
    data = pd.DataFrame(pre_change_freqs + post_change_freqs)
    data['Phase'] = ['Pre-change'] * len(pre_change_freqs) + ['Post-change'] * len(post_change_freqs)
    return data

# === Dados climáticos para os postos === #
dados = {
    "Posto": ["Toritama"] * 12,  # Repetindo o nome do posto para cada mês
    "Média": [7, 8, 9, 10, 14, 15, 16, 17, 18, 19, 20, 21]  # Meses de janeiro a dezembro
}

# Criar DataFrame com os dados de 2023
df = pd.DataFrame(dados)

# Adicionar os meses do ano ao DataFrame
df['Mês'] = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# Identificar meses de seca (por exemplo, os meses com valores de 'Média' abaixo de 10)
df['Seca'] = df['Média'] < 10

# Verificar se todos os arrays têm o mesmo comprimento
if len(df['Média']) != len(df['Posto']):
    raise ValueError("Todos os arrays devem ter o mesmo comprimento.")

# Gerar valores para o gráfico de candlestick
df['Open'] = df['Média'] + np.random.uniform(-2, 2, len(df))
df['High'] = df['Média'] + np.random.uniform(0, 5, len(df))
df['Low'] = df['Média'] - np.random.uniform(0, 5, len(df))
df['Close'] = df['Média'] + np.random.uniform(-2, 2, len(df))

# === Plotar o Gráfico de Candlesticks em 2D com Matplotlib === #
fig, ax = plt.subplots(figsize=(10, 6))

# Loop para plotar cada candlestick
for i in range(len(df)):
    open_price = df['Open'][i]
    close_price = df['Close'][i]
    low_price = df['Low'][i]
    high_price = df['High'][i]

    color = 'green' if close_price > open_price else 'red'
    
    # Alterar a cor do candlestick para vermelho durante a seca
    if df['Seca'][i]:
        color = 'orange'
    
    # Plot do retângulo representando o corpo do candlestick
    ax.plot([i, i], [low_price, high_price], color=color)  # Linhas verticais para alta e baixa
    ax.plot([i - 0.25, i + 0.25], [open_price, open_price], color=color, linewidth=8)  # Corpo do candlestick

# Personalizar o gráfico
ax.set_title('Gráfico de Candlestick - Dados de 2023')
ax.set_xticks(range(len(df)))
ax.set_xticklabels(df['Mês'], rotation=45)
ax.set_ylabel('Média de Precipitação (mm)')

plt.tight_layout()
plt.show()

# === Gerar Matriz de Transição === #
def calcular_transicao_matriz(dados):
    """Calcula a transição de matriz simples entre dados de novembro (ex: Postos)"""
    matriz = np.zeros((len(dados), len(dados)))

    for i in range(len(dados) - 1):
        # Calculando a mudança entre o valor atual e o próximo (diferença)
        diff = dados.iloc[i + 1] - dados.iloc[i]
        matriz[i, i + 1] = diff

    return matriz

# Calcular e exibir a matriz de transição
transicao_matriz = calcular_transicao_matriz(df['Média'])
print("\nMatriz de transição para os dados de 2023:")
print(transicao_matriz)

# Plotar a matriz de transição usando matplotlib
plt.figure(figsize=(8, 6))
plt.imshow(transicao_matriz, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title('Matriz de Transição - Mudanças nos Dados de 2023')
plt.xticks(ticks=np.arange(len(df['Mês'])), labels=df['Mês'], rotation=45)
plt.yticks(ticks=np.arange(len(df['Mês'])), labels=df['Mês'])
plt.show()

# === Implementar Modelo de Markov Oculto (HMM) === #
# Prepare the data for HMM
data = np.array(df['Média']).reshape(-1, 1)  # Transformando os dados em uma matriz coluna para a HMM
n_components = 3  # Número de estados ocultos que você espera

# Inicializando o modelo HMM
model = hmm.GaussianHMM(n_components=n_components, covariance_type="diag", n_iter=1000)

# Ajustando o modelo aos dados
model.fit(data)

# Predizendo os estados ocultos
hidden_states = model.predict(data)

# Exibindo os estados ocultos
df['Estado Oculto'] = hidden_states
print("\nEstados ocultos preditos para os dados de 2023: ")
print(df)

# Plotar os estados ocultos
plt.figure(figsize=(10, 6))
plt.plot(df['Média'], label='Média de Precipitação')
plt.plot(hidden_states, label='Estado Oculto', linestyle='dashed')
plt.title('Identificação de Estado Oculto usando HMM')
plt.xlabel('Mês')
plt.ylabel('Média de Precipitação')
plt.legend()
plt.show()
