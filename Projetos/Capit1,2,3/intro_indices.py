equipamentos = []
valor = []
serial = []
setor = []
#agora eu abre com True  para gerar um loop
resposta = "SIM"
while resposta == "SIM":
#adiciono os elementos     
    equipamentos.append(input("Nome do equipamento: "))
    valor.append(float(input("Valo do equipamento: ")))
    serial.append(int(input("numero do serial: ")))
    setor.append(input("Setor do equipamento"))
    resposta=input("Digite 'SIM' para continuar: ").upper()
#mostro em tela oque foi adicionado nas listas
# ++ nessa outra parte é usado os indices    
for indice in range(0,len(equipamentos)): #ele ira mostrar em tela com mais detalhes 
    print("equipamento..:",(indice+1))
    print("Nome......:" , equipamentos[indice])
    print("Valor.........:" , valor[indice])
    print("Serial.......:" , serial[indice])
    print("Setor.......:," , setor[indice])

# ++ agora adionamos esse trecho para fazer a busca do equipamento na nossa lista
busca=input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
  if busca==equipamentos[indice]:
    print("Valor..: ", valor[indice])
    print("Serial.:", serial[indice])    

# ++ Todos os equipamentos 'aq3' receberam uma depreciação de 10%.
# ++ O codigo é responsavel por fazer essa mudança de valor do equipamento 

depreciacao = input("digite o nome do equipamento que sera depreciado: ")
for indice in range(0,len(equipamentos)):
   if depreciacao==equipamentos[indice]:
      print("Valor antigo: ", valor[indice])
      valor[indice] = valor[indice] * 0.9
      print("NOVO valor: " , valor[indice])

#Um equipamento esta danificado e eu repciso deletalo, pq sera removido do estoque
      #adicione ate 3 equipamentos para ver o resultado melhor
sereais=(int(input("Digite o serial do equipamento a ser removido: ")))
for indice in range(0, len(setor)):
   if serial[indice]==sereais:
      del setor[indice]
      del equipamentos[indice]
      del serial[indice]
      del valor[indice]
      break #depois de excluir o equipamento ele ira sair do laço for, pois o indice podera se perder, pq excluimos um item
#aqui nos repetimos o codigo para ver se real,mente foi excluido o equipamento 
for indice in range(0,len(equipamentos)):
   print("Equiopamento...: ", (indice+1))
   print("nome: ", equipamentos[indice])
   print("valor: ", valor[indice])
   print("setor: ", setor[indice])
   print("serial: ", serial[indice])

