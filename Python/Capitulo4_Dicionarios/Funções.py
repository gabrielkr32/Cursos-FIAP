def perguntar(): #estou definindo uma função 'pergubntar'
    resposta = input("""" O que deseja realizar?
<I> - Para Inserir um usuario
<P> - Para pesquisar um usuario
<E> - Para Excluir um usuario 
<L> - Para Listar um usuario: """).upper()   
    return resposta


#defini uma função quue vai adiconar la no dicionario
def inserir(dicionario):
    dicionario[[input]("Digite o login: ").upper()]= [input("Digite o nome: ").upper(),
                                                      input("Digite a ultima data de acesso: "),
                                                      input("Qual a ultima estação acesssada: ").upper()]

def pesquisar(dicionairo, chave):
    lista = dicionairo.get(chave)
    if lista != None:
        print("Nome.............: " + lista[0])
        print("Ultimo acesso....:" + lista[1])  
        print("Ultima estação....: " + lista[2])

#moatar a funçao que ira deletar um login
# ela vai nprocurar entre os usuarios, com a CHAVE e deletar
def excluir(dicionairo, chave):
    if dicionairo.get(chave)!=None:
        del dicionairo[chave]
    print("Objeto deletado")

#vou definir uma função para percorrer e listar os usuarios com seus detalhes
def listar(dicionairo):
    for chave, valor in dicionairo.item():
        print("Objeto..........")
        print("Login...........", chave) 
        print("Dados.........", valor)               
    