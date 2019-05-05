#gordinho / perna_curta / faz_auau

porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [1, 1, 1]
cachorro3 = [0, 0, 0]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

marcacoes = [1, 1, 1, -1, -1, -1]

from sklearn.naive_bayes import MultinomialNB

#criando modelo
modelo = MultinomialNB()

#treinando modelo
modelo.fit(dados, marcacoes)

#prevendo resultado
misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]

teste = [misterioso1, misterioso2]

print(modelo.predict(misterioso1))