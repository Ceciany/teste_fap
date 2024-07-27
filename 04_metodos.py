def resultado (nome, nota1, nota2):
    media = (nota1+nota2)/2
    
    if media >=7:
        status = ("APROVADO")
    elif media <=4:
        status = ("REPROVADO")
    else:
        status = ("EM RECUPERAÇÃO")

    return (print (f"O aluno {nome}, com média {media}, está {status}."))

resultado("Ceciany", 5,4)
