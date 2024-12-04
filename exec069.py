qtd_produtos = 0
menor_produto = ""
menor_preco = float("inf")
total = 0

while True:
    print("=-=" * 10)
    produto = input("Digite o nome do produto: ").strip()
    preco = float(input("Digite o valor do preço: R$ "))

    total += preco

    if preco > 1000:
        qtd_produtos += 1

    if preco < menor_preco:
        menor_preco = preco
        menor_produto = produto

    escolha = input("Você deseja continuar? [S/N] ").strip().upper()
    while escolha not in ['S', 'N']:
        escolha = input("Entrada inválida. Você deseja continuar? [S/N] ").strip().upper()
    
    if escolha == 'N':
        break

print("\nResumo da compra:")
print(f"O total gasto foi de R$ {total:.2f}")
print(f"{qtd_produtos} produto(s) custam mais de R$ 1000,00")
print(f"O produto mais barato foi '{menor_produto}' que custa R$ {menor_preco:.2f}")
