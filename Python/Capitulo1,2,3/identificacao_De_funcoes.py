def preencherInventario(lista):
    resposta ="SIM"
    while resposta == "SIM":
        equipamento=[input("Equipamento: "),
                     float(input("Valor: ")),
                     int(input("Numero do serial: ")),
                     input("Departamento: ")]
        lista.append(equipamento)
        reposta = input("Digite 'SIM' para continuar: ").upper()


def exibir_inventario(lista):
   for elemento in lista:
       print("nome: ", elemento[0])
       print("valor: ", elemento[1])
       print("serial: ", elemento[2])
       print("depaertamento: ", elemento[3])


def localizar_por_nome(lista):
    localizar=input("Digite o nome do equipamento que deseja busca: ")
    for elemento in lista:
       if localizar==elemento[0]:
          print("Valor: ", elemento[1])
          print("Serial: ", elemento[2])


def depreciacao(lista):
    depreciacao=input("Digite o nome do equipamento que sera depreciado: ")
    for elemento in lista:
       if depreciacao==elemento[0]:
          print("VALOR Antigo: ", elemento[1])
          elemento[1] = elemento[1] * (1-porc/100)# duvida pq mudou o calculo?
          print("NOVO valor: ", elemento[1])          

def excluirPor_serial(lista):
    serial=int(input("Digite o numero do serial para excluir um equipamento: "))
    for elemento in lista:
       if elemento[2]==serial:
         lista.remove(elemento)
    return "Itens excluidos: "               


def total_valores(lista):
  valores=[]
  for elemento in lista:
      valores.append(elemento[1])
  if len(valores)>0:
       print("O equipamento mais caro custa: ", max(valores))
       print("O equipamento com o menos preço: ", min(valores))
       print("O valor TOTAL de todos os equipamentos: ", sum(valores))
