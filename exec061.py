# pt = int(input("Digite o primeiro termo de uma PA: "))
# r = int(input("Digite a razão da PA: "))
# for c in range(pt, (r * 10 + pt), r):
#     print(c)


pt = int(input("Digite o primeiro termo de uma PA: "))
r = int(input("Digite a razão da PA: "))
c= 1
while c <= 10:
    print(f"{pt} > ", end='')
    pt += r
    c += 1
print("FIM")