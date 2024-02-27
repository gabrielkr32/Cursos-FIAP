nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
prioridade ="NÃO"
if idade >= 65:
    prioridade = "SIM"
print("O paciente",nome,"possui atendimento prioritario?",prioridade)

#estamos verificando se o paciente tem prioridade ou nao 
#se ele tiver a idade maior doq o estipulado == True
#depois é mostrado em tela o resultado