resposta = "SIM"
while resposta == "SIM": #adicionamos uma estrutura de repeticao
    nome = input("Digite o seu nivel de acesso: ").upper()
    if nome == "ADMINISTRADOR"or nome == "USUARIO":
        genero = input("Digite o seu genero: ").upper()
        if nome == "ADMINISTRADOR":
          if genero == "FEMININO":
           print("Ola Administradora! ")
          else:
            print("Ola administrador! ")
        else: 
           if genero == "FEMININO":
              print("ola usuaria!")
           else:   
           
             print("Ola usuario")   
    elif nome == "VISITANTE":
       print("Ola visitante!")
    else:
      print("Erro")               
    