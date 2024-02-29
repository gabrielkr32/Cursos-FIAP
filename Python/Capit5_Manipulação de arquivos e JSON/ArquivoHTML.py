with open("pagina.html", "w") as pagina: 
    pagina.write("<body> <h1> Este é um teste para pagina da Web </h1> ")
    pagina.write("<br><h2> Abaixo seqguem alsuns nomes importantes para projetos: </h2>")
    pagina.write("<h3>")
    nome=""
    while nome != "SAIR":
        nome = input("Digite um nome ou 'SAIR': ").upper()
        if nome!="SAIR":
            pagina.write("<br>"+nome)
    pagina.write("</hr></body>")        