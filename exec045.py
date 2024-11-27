from random import randint
from time import sleep

RESET = '\033[0m'
YELLOW = '\033[33m'
CYAN = '\033[36m'
GREEN = '\033[32m'
BLUE = '\033[34m'
RED = '\033[31m'

print(f"{YELLOW}-=" * 15)
print(f"{CYAN}Bora jogar pedra, papel e tesoura?")
print(f"{YELLOW}-=" * 15)
print('')

print(f'''{CYAN}Escolha uma jogada:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')

itens = ('Pedra', 'Papel', 'Tesoura')

try:
    jogador = int(input(f"{CYAN}Sua escolha: "))
    if jogador not in [0, 1, 2]:
        print(f"{RED}Jogada inválida! Tente novamente. {RESET}")
    else:
        computador = randint(0, 2)

        print('')
        print(f"{GREEN}JO")
        sleep(1)
        print(f"{YELLOW}KEN")
        sleep(1)
        print(f"{BLUE}PO!")
        print('')

        print(f"{YELLOW}-=" * 15)
        print(f"{GREEN}Você jogou: {itens[jogador]}")
        print(f"{GREEN}Eu joguei: {itens[computador]}")
        print(f"{YELLOW}-=" * 15)

        if jogador == computador:
            resultado = f"{YELLOW}Empate! :|"
        elif (jogador == 0 and computador == 2) or \
             (jogador == 1 and computador == 0) or \
             (jogador == 2 and computador == 1):
            resultado = f"{GREEN}Você venceu! :)"
        else:
            resultado = f"{RED}Eu venci! :("

        print(resultado)
except ValueError:
    print(f"{RED}Por favor, insira um número válido! {RESET}")

print(RESET)