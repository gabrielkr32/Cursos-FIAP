usuario = {} # na primeira linha estamos criando o dicionarios de dados
usuario = {
    "Chaves": ["Chaves Silva", "17/06/2017", "Recep_01"], #preenchemos o nosso dicionarios, de acordo com o exemplo do materia.
    "Quico":["Enrico Flores", "03/06/2017", "Raiox-02"]
}
    #chave : ["dados das chaves" nome, data do ultimo acesso, e o nome da ultima estação] apos a virgula ,
                                                                                                           #iniciamos outro objeto
# encerramos fechando as chaves =  }

#as chasves sao a representação de um dicionario de dados 

#adicionei um novo objeto no meu dicinario. Apenas chamei o nome do dicionario, com o valor da chave(Gabriel), e add os dados. 
usuario["Gabriel"] = ["Gabriel Kruger", "22/02/2024", "Setor_Show's"]


#Agora podemos retornar os dados de um objeto da lista, no dicionario
print(usuario) #exibimos tdo oq existe dentro do dicionario
print("#################========##########")
print("Dados: ", usuario.get("Chaves")) #exibimos somente os dados da chave 'Chaves'
#O metodo .get() ele vai pesquisar os valores entre as chaves existentes, caso encontre
# ele retornara os dados. Caso nao encontre ele respondera como  NONE; por padrão em Python.