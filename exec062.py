# pt = int(input("Digite o primeiro termo de uma PA: "))
# r = int(input("Digite a razão da PA: "))
# c = 1
# while c <= 4:
#     print(f"{pt} > ", end= '')
#     pt += r
#     c += 1
# print("\nCaso queira ver mais alguns termos digite quantos termos, caso contrario digite '0' para sair do programa. ")
# new_pt = int(input("Digite o valor dos novos termos: "))
# c2 = 1
# while c2 <= new_pt:
#     if new_pt == 0:
#         print("Encerrando o programa, obrigado e volte sempre!")
#         exit()
#     elif c2 <= new_pt:
#         print(f"> {pt}", end = ' ')
#         pt += r
#         c2 += 1
# print("FIM")


pt = int(input("🌟 Bem-vindo ao Gerador de Progressão Aritmética! 🌟\nDigite o primeiro termo da sua PA: "))
r = int(input("Agora me diga, qual será a razão? "))

print("\n🔢 Aqui estão os primeiros termos da sua PA:")
c = 1
while c <= 4:
    print(f"{pt} ➡️  ", end='')
    pt += r
    c += 1

while True:
    print("\n✨ Deseja ver mais termos dessa PA incrível?")
    print("Digite quantos termos você quer ver ou '0' para finalizar e sair.")
    new_pt = int(input("Quantos termos a mais você quer? "))

    if new_pt == 0:
        print("\n🛑 Programa finalizado! Obrigado por usar o Gerador de PA. Até a próxima! 👋")
        break

    print("\n🎉 Aqui estão os novos termos da sua PA:")
    c2 = 1
    while c2 <= new_pt:
        print(f"{pt} ➡️  ", end='')
        pt += r
        c2 += 1

print("\n🚀 Fim da PA! Continue praticando e aprendendo. Até logo!")

