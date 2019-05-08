from dados import carregar_acesso
from sklearn.naive_bayes import MultinomialNB


x, y = carregar_acesso()

modelo = MultinomialNB()

modelo.fit(x, y)

print(modelo.predict([[1, 0, 1], [0, 1, 0]]))