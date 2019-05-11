import csv

def carregar_acesso():

    x = []
    y = []

    arquivo = open('acesso.csv', 'r')
    leitor = csv.reader(arquivo)

    next(leitor)
    for home,como_funciona,contato,comprou in leitor:
        dados = [int(home), int(como_funciona), int(contato)]
        x.append(dados)
        y.append(int(comprou))

    return x, y

def carregar_buscas():
    x = []
    y = []

    arquivo = open('busca.csv', 'r')
    leitor = csv.reader(arquivo)

    next(leitor)
    for home, busca, logado, comprou in leitor:
        dados = [int(home), busca, int(logado)]
        x.append(dados)
        y.append(int(comprou))

    return x, y
