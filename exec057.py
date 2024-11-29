while True:
    sexo = str(input("Qual é o seu sexo [M/F]? ")).upper()
    if sexo == 'M' or sexo == 'F':
        print("Sexo inserido corretamente!")
        break
    else:
        print("Digite novamente o sexo correto.")
