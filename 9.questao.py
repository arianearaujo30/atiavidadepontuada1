import os
os.system("cls")

renda = float(input("Digite sua renda mensal: R$ "))
emprestimo = float(input("Digite o valor do empréstimo desejado: R$ "))
prestacoes = int(input("Digite o número de prestações: "))

limite_emprestimo = renda * 10

prestacao_maxima = renda * 0.30

prestacao_real = emprestimo / prestacoes

if emprestimo <= limite_emprestimo and prestacao_real <= prestacao_maxima:
    print("Empréstimo concedido!")
    else:
        print("Empréstimo NEGADO.")