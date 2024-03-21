from Capit4_Dicionarios .funcao_arquivo import *
inventario={}
opcao=chamarMenu()
while opcao>0 and opcao<4:
    if opcao==1:
        registrar(inventario)
    elif opcao==2:
        persistir(inventario)
    elif opcao==3:
        resultado = exibir()
        for linha in resultado:
            print(linha[linha.find(";")+1:-1])
    opcao = chamarMenu()


    #  de toda a linha, iremos exibir somente do terceiro caracter [2] ate o ultimo [-1]
    #  por meio do [2: -1] que se cahma 'slice' e representa um corte em um strig
    