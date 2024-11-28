pt = int(input("Digite o primeiro termo de uma PA: "))
r = int(input("Digite a razão da PA: "))
for c in range(pt, (r * 10 + pt), r):
    print(c)
