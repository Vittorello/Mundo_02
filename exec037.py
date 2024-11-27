while True:
    try:
        numero = int(input("Digite o número que deseja converter: "))
        print('- - - - '* 3)
        print('[1] Binário')
        print('[2] Octal')
        print('[3] Hexadecimal')
        print('[x] Sair')
        print('- - - - '* 3)

        pergunta = str(input("Escolha uma das opções acima, para que seu número seja convertido: ")).lower()
        if pergunta == 'x':
            print("Você fechou o sistema!")
            break
        elif pergunta == '1':
            binario = bin(numero)
            print(f"Esse é o valor do número digitado em binário: {binario[2:]}")
            break
        elif pergunta == '2':
            octal = oct(numero)
            print(f"Esse é o valor do número digitado em octal: {octal[2:]}")
            break
        elif pergunta == '3':
            hexa = hex(numero)
            print(f"Esse é o valor do número digitado em octal: {hexa[2:]}")
            break
        else:
            print("Opção invalida!")
            exit()
    except ValueError:
        print("Digite um número válido.")
        exit()