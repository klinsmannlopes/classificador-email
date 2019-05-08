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
