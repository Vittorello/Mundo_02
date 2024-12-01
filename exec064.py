x = 0
soma = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break

    else: 
        soma += n
        x += 1
print("Programa finalizado e esse foram os resultados: ")
print(f"O total de tentativas foi de {x} e a soma total dos valores é de {soma}")