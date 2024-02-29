with open("arquivo_de_testeAQ1", "r") as arquivo:
    conteudo=arquivo.readlines()
print("Tipo de dado da variavel", type(conteudo))
print("Conteudo do arquivo: ", conteudo)

#read mostra o conteudo do arquivo, porem se eu mudar para readlines 
   #ele mostra a saida do conteudo nao como strig, mas como uma lista
#quebrar um texto grande em partes seria mto util