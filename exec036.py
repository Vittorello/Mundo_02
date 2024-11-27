try:
    valor_casa = float(input("Qual o valor da casa? "))
    salario = float(input("Qual é o seu salário? "))
    anos = int(input("Em quantos anos você pretende pagar a casa? "))

    meses = anos * 12
    parcela_mensal = valor_casa / meses

    if parcela_mensal > (salario * 30) / 100:
        print("Infelizmente seu emprestimo foi negado, pois seu salário não é compativel!")
    else:
        print("Parabéns, o seu emprestimo foi concedido!")
except ValueError:
    print("Digite os valores corretos.")

