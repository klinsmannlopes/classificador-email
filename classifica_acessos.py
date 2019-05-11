from dados import carregar_acesso
from sklearn.naive_bayes import MultinomialNB


x, y = carregar_acesso()


treino_dados = x[:90]
treino_marcacoes = y[:90]

teste_dados = x[-9:]
teste_marcacoes = y[-9:]



modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)
diferenca = resultado - teste_marcacoes

acertos = [d for d in diferenca if d == 0]
total_elementos = len(teste_dados)
total_acertos   = len(acertos)

porcentagem_acertos = (100 * total_acertos) / \
                      total_elementos

print('{:.2f}'.format(porcentagem_acertos))