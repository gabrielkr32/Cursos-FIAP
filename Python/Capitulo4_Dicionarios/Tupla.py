ips = { }
resp ="S"
while resp =="S":
    ips[(input("Digite os dois primeiros octetos: "),
         input("Digite os dois ultimos octetos:"))] = input("Nome da maquina: ")
    resp = input("Digite <5> para continuar: ").upper()



print("Exibindo ip's: ")
# inicia um loop que passa por todas as chaves (tuplas de octetos) no dicionário
for ip in ips.keys():                #keys() é um método em Python que retorna uma visualização de todas as chaves em um dicionário. 
    print(ip[0]+ "-" + ip[1])        #No contexto do código fornecido, ips.keys() retorna uma visualização de todas as chaves no dicionário ips



#esta parte do código permite ao usuário pesquisar máquinas que compartilham o mesmo endereço IP com base nos dois últimos octetos fornecidos por eles
print("Exibindo maquinas com o mesmo endereço" )
pesquisa = input("Digite os dois ultimos octetos: ")
for ip, nome in ips.items():#Este é um loop que itera sobre cada item no dicionário ips. ips.items() retorna uma visão de todos os pares chave-valor no dicionário.
    print("Maquina no mesmo endereço (redes diferentes)")
    if(ip[1]==pesquisa):#Aqui, o código verifica se o segundo elemento da tupla ip (que representa os dois últimos octetos do endereço IP) é igual ao valor armazenado em pesquisa,
        print(nome)     #que é o que o usuário digitou.   




print("Exibindo as maquinas que compoe uma mesma rede: ")
rede = input("digite os dois primeiros octetos: ")
for ip, nome in ips.items():
    if(ip[0]==rede):
        print(nome)
