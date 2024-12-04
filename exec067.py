from random import randint

while True:
    print("=-=" * 10)
    print("VAMOS JOGAR PAR OU ÍMPAR")
    print("=-=" * 10)
    
    jogador = int(input("Digite um valor: "))
    escolha = input("Par ou Ímpar? [P/I] ").strip().upper()
    while escolha not in ['P', 'I']:
        escolha = input("Escolha inválida. Par ou Ímpar? [P/I] ").strip().upper()
    
    maquina_num = randint(1, 11)
    total = jogador + maquina_num
    
    print(f"Você jogou {jogador} e a máquina jogou {maquina_num}. Total: {total} {'PAR' if total % 2 == 0 else 'ÍMPAR'}")

    if (total % 2 == 0 and escolha == 'P') or (total % 2 == 1 and escolha == 'I'):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
        break 
