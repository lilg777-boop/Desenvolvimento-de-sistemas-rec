# Importa a biblioteca Pandas para análise e manipulação de dados tabulares
import pandas as pd

# Cria um dicionário com os dados dos produtos
dados = {
'nome': ['Fone de ouvido', 'Teclado', 'Mouse'],
'preco': [200, 150, 100],
'desconto': [15, 10, 0]
}

# Converte o dicionário em um DataFrame (tabela de dados)
df = pd.DataFrame(dados)

# Define uma função para calcular o preço final com base no desconto
def calcular_preco_final(row):
return row['preco']
(row['preco'] * row['desconto'] / 100)
# Aplica a função a cada linha do DataFrame e cria uma nova coluna com o preço final
df['preco_final'] = df.apply(calcular_preco_final, axis=1)

# Exibe o DataFrame com os preços finais calculados
print('## TABELA DE PREÇOS FINAIS DOS PRODUTOS ##\n')
print(df)
