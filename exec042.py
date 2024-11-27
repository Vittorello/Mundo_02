lado1 = float(input("Primeiro lado: "))
lado2 = float(input("Segundo lado: "))
lado3 = float(input("Terceiro lado: "))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    print("Os segmentos acima formam um triângulo.")
    if lado1 == lado2 == lado3:
        print("Esse triângulo é Equilátero.")
    elif lado1 == lado2 or lado2 == lado1 or lado3 == lado2 or lado2 == lado3 or lado1 == lado3 or lado3 == lado1:
        print("Esse triângulo é Isósceles")
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("Esse triângulo é Escaleno")

else:
    print("Os segmentos acima não formam um triângulo.")