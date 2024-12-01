from time import sleep

print("\n--- Vamos trabalhar com números! ---")
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

while True:
    try:
        soma = n1 + n2
        multi = n1 * n2

        print('--------------------------------------')
        print('¦                                    ¦')
        print('¦   [1] SOMAR                        ¦')
        print('¦   [2] MULTIPLICAR                  ¦')
        print('¦   [3] MAIOR                        ¦')
        print('¦   [4] NOVOS NÚMEROS                ¦')
        print('¦   [X] SAIR DO PROGRAMA             ¦')
        print('¦                                    ¦')
        print('--------------------------------------')

        escolha = input("Escolha uma operação: ").upper().strip()

        if escolha == 'X':
            print("Programa finalizado! Volte sempre que precisar.")
            exit()

        elif escolha == '1':
            print(f"O resultado da soma é: {soma}")

        elif escolha == '2':
            print(f"O resultado da multiplicação é: {multi}")

        elif escolha == '3':
            if n1 > n2:
                print(f"{n1} é o maior número.")
            elif n2 > n1:
                print(f"{n2} é o maior número.")
            else:
                print("Os dois números são iguais.")

        elif escolha == '4':
            print("Escolha novos números.\n")
            break 

        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")
        sleep(2)
    except ValueError:
        print("⚠️ Erro: Por favor, insira um número válido.")
