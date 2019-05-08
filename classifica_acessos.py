from dados import carregar_acesso
from sklearn.naive_bayes import MultinomialNB


x, y = carregar_acesso()

modelo = MultinomialNB()

modelo.fit(x, y)

print(modelo.predict([[1, 0, 1], [0, 1, 0]]))

resultado = modelo.predict(x)
diferenca = resultado - y

acertos = [d for d in diferenca if d == 0]
total_elementos = len(x)
total_acertos   = len(acertos)

porcentagem_acertos = (100 * total_acertos) / \
                      total_elementos

print(porcentagem_acertos)