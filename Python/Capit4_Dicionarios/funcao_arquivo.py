def chamarMenu():
    escolha = int(input("""Digite: 
                  <1> registrar ativo
                   <2> persistir arquivo
                    <3> exibir ativos armazenados:  """))
    return escolha

def registrar(dicionario):
    resposta = "S"
    while resposta == "S":
        dicionario[input("Digite o numero patrimoniAL: ")]=[
            input("Digite a data da ultima atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]
        resposta("Digite <5> para continuar. ").upper()

def persistir (dicionario):
     with open("inventario.csv", "a") as inv:
         for chave, valor in dicionario.items():
             inv.write(chave +";" + valor[0] + ":" +
                       valor[1] + ";" + valor [2] +"")

             return "Persistido com sucesso!" 

def exibir():
    with open("Inventario.csv", "r") as inv:
        linhas = inv.readlines()
        return linhas
                    
