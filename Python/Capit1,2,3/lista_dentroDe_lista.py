#usando lista dentro de lista, nao corremos o risco de exibir um dado de um equipamento
#com o do outro.
#com lista dentro de lista, o codigo ficou mais calroe e limpo, sem o uso do break tbm

inventario = []
resposta = "S"
while resposta == "S":
    equipamento=[input("Equipamento: "),
                  float(input("Valor: ")),
                  int(input("Numero Serial: ")),
                  input("Departamento: ")]
    inventario.append(equipamento)
    resposta=input("Digite 'S' para continuar: ").upper()

for elemento in inventario:
    print("NOME: ", elemento[0])
    print("VALOR: ",elemento[1])
    print("SERIAL: ",elemento[2])
    print("DEPARTAMENTO: ", elemento[3])

busca=input("Digite o nome do equipamento que deseja busca: ")
for elemento in inventario:
    if busca==elemento[0]:
        print("Valor: ", elemento[1])
        print("Serial: ", elemento[2])

depreciacao=input("Digite o nome do equipamento que sera depreciado: ")
for elemento in inventario:
    if depreciacao==elemento[0]:
        print("VALOR Antigo: ", elemento[1])
        elemento[1] = elemento[1]*0.9
        print("NOVO valor: ", elemento[1])

serial=int(input("Digite o numero do serial para excluir um equipamento: "))
for elemento in inventario:
    if elemento[2]==serial:
        inventario.remove(elemento)

for elemento in inventario:
    print("NOME: ", elemento[0])
    print("VALOR: ", elemento[1])
    print("SERIAL: ", elemento[2])
    print("DEPARTAMENTO: ", elemento[3])

 # Funcoes para lista numerica
    # ++ lista para armazenar somente os valores dos equipamentos. 

valores=[]
for elemento in inventario:
    valores.append(elemento[1])
if len(valores)>0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento com o menos preço: ", min(valores))
    print("O valor TOTAL de todos os equipamentos: ", sum(valores))
