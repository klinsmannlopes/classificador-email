import pandas as pd
df = pd.read_csv('busca.csv')

x_df = df[['home', 'busca', 'logado']]
y_df = df['comprou']

Xdummies_df = pd.get_dummies(x_df)

x = Xdummies_df.values
y = y_df.values

porcetagem_treino = 0.9

tamanho_treino = int(0.9 * len(y))
tamanho_teste = int(len(y) - tamanho_treino)

treino_dados = x[:tamanho_treino]
treino_marcacoes = y[:tamanho_treino]

teste_dados = x[-tamanho_teste:]
teste_marcacoes = y[-tamanho_teste:]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)
diferenca = resultado - teste_marcacoes

acertos = [d for d in diferenca if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print('{:.2f}'.format(taxa_de_acerto))