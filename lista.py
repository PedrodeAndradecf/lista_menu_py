lista = []

def produto():
    nome = input("Digite o nome do produto: ")
    codigo = int(input("Digite o código do produto: "))
    quantidade = int(input("Digite a quantidade do produto a ser cadastrado: "))
    produto = [nome, codigo, quantidade]
    lista.append(produto)
    print("Produto cadastrado com sucesso!")

def consultar():
    codigo = int(input("Digite o código do produto a ser consultado: "))
    for produto in lista:
        if produto[1] == codigo:
            print("Nome: ", produto[0])
            print("Código: ", produto[1])
            print("Quantidade: ", produto[2])
            return
    print("Produto não encontrado.")
  
def atualizar():
  codigo = int(input("Digte o código do produto a ser atulizado: "))
  print("Produto encontrado. Insira os novos dados: ")
  for produto in lista:
    if produto [1] == codigo:
      nome = input("Digite o nome do produto: ")
      quantidade = int(input("Digite a nova quantidade do produto: "))
      produto[0] = nome
      produto[2] = quantidade
      print('ATUALIZADO ')
      print(" NOME", produto[0])
      print(" CODIGO", produto[1])
      print(" QUANTIDADE", produto[2])
      return  

def excluir():
    codigo = int(input("Digite o código do produto a ser excluído: "))
    for produto in lista:
        if produto[1] == codigo:
            lista.remove(produto)
            print("Produto excluído com sucesso!")
            return
    print("Produto não encontrado.")

def exibir():
    print("Relatório de Produtos:")
    for produto in lista:
        print("Nome: ", produto[0])
        print("Código: ", produto[1])
        print("Quantidade: ", produto[2])
        print("--------------------")
      
while True:
    print("+++++++ MENU +++++++")
    print("1. Cadastrar Produto")
    print("2. Consultar Produto")
    print("3. Atualizar Produto")
    print("4. Excluir Produto")
    print("5. Exibir relatórios de Produto")
    print("6. Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        produto()
    elif opcao == 2:
        consultar()
    elif opcao == 3:
        atualizar()
    elif opcao == 4:
        excluir()
    elif opcao == 5:
        exibir()
    elif opcao == 6:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
