# Definindo a classe como um molde simples
class livro:
    titulo = ''
    autor = ''
    ano = ''
    codigo = ''
    exemplares = 0 # Total de livros que a biblioteca comprou
    disponiveis = 0 # Quantos estão na estante agora

# Lista para guardar os livros
biblioteca = []

def cadastrar_livro():
    print("\n--- Cadastrar Livro ---")
    cod = input("Digite o código do livro: ")
    
    # Verificar se o código já existe
    for l in biblioteca:
        if l.codigo == cod:
            print("Erro: Já existe um livro com este código!")
            return

    novo = livro()
    novo.codigo = cod
    novo.titulo = input("Digite o título: ")
    novo.autor = input("Digite o autor (apenas o primeiro): ")
    novo.ano = input("Digite o ano de publicação: ")
    
    qtd = int(input("Quantidade de exemplares: "))
    novo.exemplares = qtd
    novo.disponiveis = qtd # No cadastro, todos estão disponíveis
    
    biblioteca.append(novo)
    print("Livro cadastrado com sucesso!")

def consultar_livro():
    print("\n--- Consultar Livro ---")
    print("1. Por código")
    print("2. Por autor")
    opcao = input("Escolha uma opção: ")

    encontrou = 0
    if opcao == "1":
        cod = input("Digite o código: ")
        for l in biblioteca:
            if l.codigo == cod:
                print("Título:", l.titulo, "| Autor:", l.autor, "| Disponíveis:", l.disponiveis, "/", l.exemplares)
                encontrou = 1
    
    if opcao == "2":
        aut = input("Digite o nome do autor: ")
        for l in biblioteca:
            if l.autor == aut:
                print("Código:", l.codigo, "| Título:", l.titulo, "| Disponíveis:", l.disponiveis)
                encontrou = 1
    
    if encontrou == 0:
        print("Livro não encontrado")

def alterar_dados():
    print("\n--- Alterar Dados ---")
    cod = input("Digite o código do livro: ")
    
    encontrou = 0
    for l in biblioteca:
        if l.codigo == cod:
            print("Alterando:", l.titulo)
            l.titulo = input("Novo título: ")
            l.autor = input("Novo autor: ")
            l.ano = input("Novo ano: ")
            print("Dados alterados!")
            encontrou = 1
            
    if encontrou == 0:
        print("Livro não encontrado")

def busca_rapida():
    print("\n--- Busca Rápida (Opção 4) ---")
    cod = input("Digite o código: ")
    encontrou = 0
    for l in biblioteca:
        if l.codigo == cod:
            print("Título:", l.titulo)
            print("Número de exemplares (Total):", l.exemplares)
            print("Número de exemplares (Disponíveis):", l.disponiveis)
            encontrou = 1
    
    if encontrou == 0:
        print("Livro não encontrado")

def remover_livro():
    print("\n--- Remover Livro ---")
    cod = input("Digite o código: ")
    
    posicao = -1
    for i in range(len(biblioteca)):
        if biblioteca[i].codigo == cod:
            posicao = i
            
    if posicao != -1:
        biblioteca.pop(posicao)
        print("Livro removido!")
    else:
        print("Livro não encontrado")

def listar_todos():
    print("\n--- Lista de Livros Disponíveis (Ordenada) ---")
    
    # Criar lista apenas com livros que tem pelo menos 1 disponível
    disponiveis_agora = []
    for l in biblioteca:
        if l.disponiveis > 0:
            disponiveis_agora.append(l)
            
    if len(disponiveis_agora) == 0:
        print("Nenhum livro disponível para listagem no momento.")
    else:
        # Ordenação
        n = len(disponiveis_agora)
        for i in range(n):
            for j in range(0, n - i - 1):
                if disponiveis_agora[j].titulo > disponiveis_agora[j+1].titulo:
                    aux = disponiveis_agora[j]
                    disponiveis_agora[j] = disponiveis_agora[j+1]
                    disponiveis_agora[j+1] = aux

        for l in disponiveis_agora:
            print("Título:", l.titulo, "| Ano:", l.ano, "| Na estante:", l.disponiveis)

def realizar_emprestimo():
    print("\n--- Empréstimo ---")
    cod = input("Digite o código: ")
    
    encontrou = 0
    for l in biblioteca:
        if l.codigo == cod:
            encontrou = 1
            if l.disponiveis > 0:
                l.disponiveis = l.disponiveis - 1
                print("Empréstimo realizado! Restam", l.disponiveis, "na estante.")
            else:
                print("Livro já emprestado (todos os exemplares estão fora)")
                
    if encontrou == 0:
        print("Livro não encontrado")

def realizar_devolucao():
    print("\n--- Devolução ---")
    cod = input("Digite o código: ")
    
    encontrou = 0
    for l in biblioteca:
        if l.codigo == cod:
            encontrou = 1
            if l.disponiveis < l.exemplares:
                l.disponiveis = l.disponiveis + 1
                print("Devolução realizada! Agora temos", l.disponiveis, "na estante.")
            else:
                print("Erro: Todos os exemplares já estão na biblioteca!")
            
    if encontrou == 0:
        print("Livro não encontrado")

# Loop principal
rodando = 1
while rodando == 1:
    print("\n--- MENU BIBLIOTECA ---")
    print("1- Cadastrar livro")
    print("2- Consultar livro")
    print("3- Alterar dados")
    print("4- Busca rápida")
    print("5- Remover livro")
    print("6- Listar todos")
    print("7- Realizar empréstimo")
    print("8- Realizar devolução")
    print("9- Sair")
    
    op = input("Escolha: ")
    
    if op == "1":
        cadastrar_livro()
    if op == "2":
        consultar_livro()
    if op == "3":
        alterar_dados()
    if op == "4":
        busca_rapida()
    if op == "5":
        remover_livro()
    if op == "6":
        listar_todos()
    if op == "7":
        realizar_emprestimo()
    if op == "8":
        realizar_devolucao()
    if op == "9":
        print("Saindo...")
        rodando = 0