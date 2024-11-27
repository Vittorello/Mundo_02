while True:
    try:
        valor = float(input("🌟 Digite o valor do produto: "))

        desconto_pix_dinheiro = valor * 0.10
        desconto_cartao_vista = valor * 0.05
        acrescimo_cartao_parcelado = valor * 0.20
        valor_com_desconto_pix = valor - desconto_pix_dinheiro
        valor_com_desconto_cartao = valor - desconto_cartao_vista
        valor_com_juros = valor + acrescimo_cartao_parcelado

        print('--------------------------------------')
        print('¦                                    ¦')
        print('¦  🔥 [1] À VISTA PIX / DINHEIRO      ¦')
        print('¦  💳 [2] À VISTA NO CARTÃO           ¦')
        print('¦  🛍️ [3] EM ATÉ 2X NO CARTÃO         ¦')
        print('¦  💸 [4] 3X OU MAIS NO CARTÃO        ¦')
        print('¦  ❌ [X] CANCELAR PAGAMENTO          ¦')
        print('¦                                    ¦')
        print('--------------------------------------')

        escolha = input(f"💵 Com base no valor do produto R${valor:.2f}, qual será a forma de pagamento? ").upper()

        if escolha == 'X':
            print("❌ Pagamento cancelado! Volte sempre que precisar. 😊")
            break
        elif escolha == '1':
            print(f"💰 Que oportunidade! Com 10% de desconto, você pagará apenas R${valor_com_desconto_pix:.2f}.")
            break
        elif escolha == '2':
            print(f"💳 Pagamento à vista no cartão? Excelente escolha! Você terá um desconto de 5%, totalizando R${valor_com_desconto_cartao:.2f}.")
            break
        elif escolha == '3':
            print(f"📦 Pagando em até 2x, o valor permanece o mesmo: R${valor:.2f}.")
            break
        elif escolha == '4':
            total_parcela = int(input("Quantas parcelas? "))
            parcela = valor_com_juros / total_parcela
            print(f"📈 Parcelamento em {total_parcela}x de {parcela} com juross de 20%. O novo valor será R${valor_com_juros:.2f}.")
            break
        else:
            print("⚠️ Opção inválida. Por favor, escolha uma das opções disponíveis.")
    except ValueError:
        print("🚨 Por favor, insira um valor válido para o produto.")
