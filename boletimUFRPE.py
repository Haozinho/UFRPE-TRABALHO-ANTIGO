import matplotlib.pyplot
boletim = []  # Criando uma lista.

# Definindo as Funções:

def p_nome():  # Função para pedir o nome.
    return (input("Digite seu nome: "))

def p_va1():  # Função para pedir a nota da va1.
    global boletim
    n=0
    n=float(input("Digite a nota da primeira verificação de aprendizagem: "))
    if (0.0 > n or n > 10.0000):
        print("Sua nota não pode ser menor que 0 e nem maior que 10, por favor digite novamente: ")
        return p_va1()
    else:
        return n

def p_va2():  # Função para pedir a nota da va2.
    global boletim
    n=0
    n=float(input("Digite a nota da segunda verificação de aprendizagem: "))
    if (0 > n or n > 10.1):
        print("Sua nota não pode ser menor que 0 e nem maior que 10, por favor digite novamente: ")
        return p_va2()
    else:
        return n

def listar_dados(nome, va1, va2, media): # Função que mostra todos os dados dos alunos.
    print("     Nome: %s\n       VA1: %s\n       VA2: %s\n     Media: %s\n--------------------" % (nome, va1, va2, media))

def pesquisa(nome):  # Função para pesquisar aluno.
    name = nome.lower()  # Convertendo todas as letras em minúsculas.
    for d, e in enumerate(boletim):  # Executando o loop.
        if e[0].lower() == name:  # Determinando uma condição.
            return d  # Executa caso a condição for verdadeira.
    return None  # Executa caso a condição for falsa.

def novo():  # Função para adicionar novo aluno.
    global boletim  # Definindo variável como Global.
    nome = p_nome()  # Entrada de dados.
    va1 = p_va1()  # Entrada de dados.
    va2 = p_va2()  # Entrada de dados.
    media = (va1+va2)/2 # Calcula a media.
    boletim.append([nome, va1, va2, media])  # Adicionando os dados

def notageral(): # Imprime as notas dos alunos sem plotar o gráfico.
    print("\nBoletim\n\n--------------------")
    for e in boletim:
        listar_dados(e[0], e[1], e[2], e[3])
    print("--------------------\n")

def listar():  # Função para mostrar lista de alunos.
    print("\nBoletim\n\n--------------------")

    for e in boletim:
        listar_dados(e[0], e[1], e[2], e [3])

    x = range(len(boletim) + 1)

    notas = []
    for aluno in boletim:
        notas.append(aluno[3])

    media = sum(notas)/len(notas)
    notas.append(media)

    nomes = []
    for aluno in boletim:
        nomes.append(aluno[0])

    nomes.append("Media Geral")

    matplotlib.pyplot.bar(x, notas)
    matplotlib.pyplot.xticks(x, nomes)
    matplotlib.pyplot.show()

    print("--------------------\n")

def pesquisar():  # Função para Pesquisar os aluno.
    p = pesquisa(p_nome())  # Entrada de dados.
    if p != None:  # Determinando uma condição, caso seja verdadeira:
        nome = boletim[p][0]  # Procurando os dados na boletim.
        va1 = boletim[p][1]  # Procurando os dados na boletim.
        va2 = boletim[p][2]  # Procurando os dados na boletim.
        media = (va1+va2)/2
        print("Aluno encontrado:\n--------------------")  # Exibi informação na tela.
        listar_dados(nome, va1, va2, media)  # Mostra os dados.
    else:
        print("Aluno não encontrado, você digitou o nome errado ou não foi cadastrado, caso não foi cadastrado faça o cadastro.")  # Executa caso a condição seja falsa.

def validar(pergunta, inicio, fim):  # Função para validar numeros inteiros.
    while True:  # Criando um loop infinito.
        try:  # Criando um acordo/condição.
            valor = int(input(pergunta))  # Entrada de dados.
            if inicio <= valor <= fim:  # Deterimando uma condição.
                return (valor)  # Executa caso for verdadeira.
            return
        except ValueError:  # Executa caso for falsa.
            print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def menu():  # Função que exibe o menu de opções.
    print("""
   1 - Cadastrar um novo aluno e suas notas.
   2 - Consultar notas.
   3 - Gerar boletim.
   4 - Plotar gráfico de médias.
   5 - Sair.
""")

    return validar("Escolha uma opção: ", 1, 7)  # Retorna o valor da opção desejada.

while True:  # Criando um loop infinito.
    opcao = menu()
    if opcao == 5:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        pesquisar()
    elif opcao == 3:
        notageral()
    elif opcao == 4:
        listar()