RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5:
    print(f"Você está {RED}REPROVADO!{RESET}")
elif 5 <= media <= 6.9:
    print(f"Você está de {YELLOW}RECUPERAÇÃO!{RESET}")
elif media >= 7:
    print(f"Parabéns, você está {GREEN}APROVADO!{RESET}")
