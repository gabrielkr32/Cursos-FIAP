# iremos armazenar apenas os seguinte dados, o numero patrimonial do ativo
  #a descrição do ativo, a data da ultima atualizaçao 
   # e o nome do departamento em que esta localizado

inventario = {}

while True:
    opcao = int(input("""Digite:
                <1> para registrar
                <2> para persistir em arquivo
                <3> para exibir ativos armazenados
                <4> para sair: """))

    if opcao == 1:
        resposta = "S" #resposta = "S": Inicializa a variável resposta com o valor "S". Essa variável será usada para controlar um loop interno que permite ao usuário 
                         #adicionar vários itens ao inventário sem precisar reiniciar o programa.
        #Quando o usuário digitar qualquer coisa diferente de "S" como resposta, o loop interno será encerrado e o programa retornará ao menu principal.
        
        while resposta == "S": #enquanto o usuário responder "S" (indicando sim) à pergunta "Digite <S> para continuar.", o programa continuará permitindo que o 
                                 #usuário adicione novos itens ao inventário.
            numero_patrimonial = input("Digite o número patrimonial: ")
            data_atualizacao = input("Digite a data da última atualização: ")
            descricao = input("Digite a descrição: ")
            departamento = input("Digite o departamento: ")
            
            inventario[numero_patrimonial] = [data_atualizacao, descricao, departamento]
            resposta = input("Digite <S> para continuar.").upper()
            #inventario[numero_patrimonial] = [data_atualizacao, descricao, departamento]: Esta linha cria uma entrada no dicionário inventario. 
              #O número patrimonial (a chave) é associado a uma lista que contém a data de atualização, a descrição e o departamento do item. 
               #Isso permite que você armazene todas essas informações juntas, associadas a um número patrimonial específico.


    elif opcao == 2:
        with open("Inventario.csv", "a") as inv:#Esta linha abre o arquivo "Inventario.csv" em modo de escrita ("a" significa "append", ou seja, adicionar ao final do arquivo)
            #utilizando o comando open() dentro de um bloco with. Usar o bloco with garante que o arquivo seja fechado corretamente após o término do bloco,mesmo se ocorrerem exceções 
              #durante a execução do código.
            for chave, valor in inventario.items():#Esta linha inicia um loop for que percorre todos os itens do dicionário inventario. Em cada iteração do loop,
                #a variável chave receberá o número patrimonial e a variável valor receberá a lista de informações associadas a esse número patrimonial.
                inv.write(chave + ";" + valor[0] + ";" + #escreve uma linha no arquivo CSV para cada item do inventário.
                          valor[1] + ";" + valor[2] + "\n")
                #Número patrimonial (chave)
                 #Data de atualização (valor[0])
                 #Descrição (valor[1])
                 #Departamento (valor[2])
                 #Ao final de cada linha, é adicionado um caractere de nova linha (\n) para garantir que cada entrada seja escrita em uma nova linha no arquivo.
            print("Persistindo com sucesso")
    
    elif opcao == 3:
        with open("Inventario.csv", "r") as inv:#abre o arquivo "Inventario.csv" em modo de leitura ("r" significa "read") utilizando o comando open() dentro de um bloco with. 
            #Assim como antes, o bloco with garante que 
            #o arquivo seja fechado corretamente após a conclusão do bloco.            
            print(inv.readlines())
            #lê todas as linhas do arquivo usando o método readlines() e as imprime usando a função print(). O método readlines() lê todas as linhas do arquivo e retorna uma 
            #lista onde cada elemento corresponde a uma linha do arquivo. Então, print() é usado para imprimir essa lista de linhas na saída padrão (normalmente o console).
            
    
    elif opcao == 4:
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")