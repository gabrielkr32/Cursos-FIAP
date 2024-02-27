nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))                                    #upper == para reconhcer o seu 'sim' como um 'SIM' 
doenca_infectocontagiosa = input ("Suspeita de doença infectocontagiosa?").upper()
#o primeiros bloco de if se refere a com maiores de 65. Assim sao os que tem preioridade
#separei por blocos, para facilitar a leitura do codigo.
#como temos duas condicoes apenas, que seria a de doença e a idade, montar por 'blocos' parece n fazer mta diferença; porem se tivessemos mais variaveis para montar,
#provavelmente nos perderiamos nos varios if's e elif's. Entao, como uma boa pratica, tenha isso em mente, para boa leitura e para isolar as partes que demandam mais atenção.
if idade >= 65:
    print("Paciente COM prioridade")
    if doenca_infectocontagiosa == "SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa == "NAO":
        print("Encaminhe o paciente para a sala BRANCA")
    else:
        print("Responda a suspeita de doenca infectocontagiosa com SIM ou NAO")


#ja o segundo, com os sem prioridade
else:
    print("Paciente SEM prioridade")    
    if doenca_infectocontagiosa =="SIM":
        print("Encaminhe o paciente para a sala AMARELA") 
    elif doenca_infectocontagiosa == "NAO":
        print("Encaminhe o paciente para a sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")
