# for c in range(6, 0, -1):
#     print(c)
# print("FIM")

# for c in range(1, 10, 2):
#     print(c)
# print("FIM")

# n = int(input("Digite um número: "))
# for c in range(1, n+1):
#     print(c)

# i = int(input("Inicio: "))
# f = int(input("Fim: "))
# p = int(input("Passo: "))
# for c in range (i, f+1, p):
#     print(c)

n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"Você digitou {par} números pares e {impar} números ímpares")