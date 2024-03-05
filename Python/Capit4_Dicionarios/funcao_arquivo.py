def chamarMenu():
    #a funcao apenas exibi para usuario as opcaoes que ele possui, para manipulaçao do inventario
      #e retorna o valor sewlecionado por meio da variavel ' escolha '
    escolha = int(input("""Digite: 
                  <1> registrar ativo
                   <2> persistir arquivo
                    <3> exibir ativos armazenados:  """))
    return escolha

def registrar(dicionario):
    #a funcao ia receber o dicionario responsavel por armazenar os ativos e entao
      #ira preencher quanto o usuario digitar 'S'
    resposta = "S"
    while resposta == "S":
        dicionario[input("Digite o numero patrimoniAL: ")]=[
            input("Digite a data da ultima atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]
        resposta("Digite <5> para continuar. ").upper()

def persistir (dicionario):
     #descarregar o diconario que for passado com parametro para dentro do arquivo 'inventario.csv' 
     with open("inventario.csv", "a") as inv:
         for chave, valor in dicionario.items():
             inv.write(chave +";" + valor[0] + ":" +
                       valor[1] + ";" + valor [2] +"")

             return "Persistido com sucesso!" 

def exibir():#retornar o conteudos das linhas do 'inventario.csv' por meio da variavel 'linha'
    with open("Inventario.csv", "r") as inv:
        linhas = inv.readlines()
        return linhas
                    
