from identificacao_De_funcoes import *

minhaLista=[]
print("Preenchendo")
preencherInventario(minhaLista)
print("Exibido")
exibir_inventario(minhaLista)

print("Pesquisando")
localizar_por_nome(minhaLista)
print("Alterando")
depreciacao(minhaLista, 20)

print("Excluido")
print(excluirPor_serial(minhaLista)) #Foi chamado dentro do print o excluirPor_serial.. pq somente ela possui retorno
exibir_inventario(minhaLista)#tbm a economia de linhas ao exibir o inventario()

print("Resumindo")
total_valores(minhaLista)

#toda vez que estiver deparando com um codigo mto extenso, se pergunte se pode separa por funcoes, assim criando modulos que iram facilitar a manutenção