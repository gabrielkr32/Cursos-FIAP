#primerio eu crio as lista quie vao armazenar o conteudo
equipamentos = []
valor = []
sereal = []
setor = []
#agora eu abre com True  para gerar um loop
resposta = "SIM"
while resposta == "SIM":
#adiciono os elementos     
    equipamentos.append(input("Nome do equipamento: "))
    valor.append(float(input("Valo do equipamento: ")))
    sereal.append(int(input("numero do serial: ")))
    setor.append(input("Setor do equipamento"))
    resposta=input("Digite 'SIM' para continuar: ").upper()
#mostro em tela oque foi adicionado nas listas
for equipamento in equipamentos:
    print("Equipamento:", equipamento)
