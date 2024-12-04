while True:
    n = int(input("Digite um número para visualizar a tabuada (negativo para sair): "))
    if n < 0:
        print("Digite um número válido.")
        break
    for d in range(1,11):
        resultado = d * n
        print(f"{d} X {n} = {resultado}")
