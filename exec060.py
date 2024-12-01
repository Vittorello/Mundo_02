import math

print(math.factorial(5))

# Fatorial usando "FOR"

fact = 1
n = int(input("Digite um número: "))

for c in range(1,n+1):
    fact = fact * c
print(f"O fatorial do número {n} é {fact}")

# Fatorial usando "WHILE"

n = int(input('Digite um número: '))
c = n
f = 1 
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'o fatorial de {n} é {f}')

