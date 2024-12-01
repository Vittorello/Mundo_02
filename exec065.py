qtd_total = maior = menor = soma = media = 0
decisao = 'S'
while decisao in 'Ss':
    n = int(input("Digite um número: "))
    soma += n
    qtd_total += 1

    if qtd_total == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    decisao = str(input("Você ainda quer continuar a digitar valores [SIM/NAO]?  ")).upper().strip()[0]
media = soma / qtd_total
print("Programa finalizado e esse foram os resultados: ")
print(f"A média de todos os valores inseridos foi de '{media:.2f}', o maior número foi '{maior}' e o menor foi '{menor}' e a soma de {soma}")
