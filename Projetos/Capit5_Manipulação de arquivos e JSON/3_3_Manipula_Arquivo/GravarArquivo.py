with open("Teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tao facil criar um arquivo!, Agora estou aprendendo mais sobre python.  ")

with open("Teste.txt", "w") as arquivo:
    arquivo.write("Continuacaoo do texto")


#Na ultilizaçao do with + open é que em resumo, diminuimos as linhas, e simplificamos o codigo 
    #esse comando with, permitira representar dentro de blocos identado, o arquivo.
    #tbm temos o controle de encerramento do aqruivo, uma vez que nao é necessario o uso do close()
        
#se eu adicionar outro codigo igual o primeiro mas com um conteudo diferente, ele ira ser escrito por cima e atualizara.
   
   
# 'as' é uma palavra-chave utilizada em conjunto com a instrução with em Python para criar um contexto de gerenciamento de recursos. 
    #Nesse contexto, um recurso é aberto e automaticamente fechado quando não é mais necessário, garantindo que recursos como arquivos 
    #sejam fechados de forma adequada, mesmo se ocorrerem exceções durante a execução do código.