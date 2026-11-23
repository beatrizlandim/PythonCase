import investigacoes


menu = "==============================\n          PYTHONCASE\n     SISTEMA INVESTIGATIVO\n==============================\n[1] NOVA INVESTIGAÇÃO\n[2] CONTINUAR INVESTIGAÇÃO\n[3] ARQUIVO DE CASOS\n[4] ESTATÍSTICAS\n[5] CONFIGURAÇÕES\n[0] SAIR DO SISTEMA"


while True:
    print(menu)

    try:
        opcao_menu=int(input("Escolha uma opção: "))

    except ValueError:
        print("Entrada inválida! Digite apenas números.")
        continue
        


    if opcao_menu==0:
        break

    elif opcao_menu==1:
        investigacoes.nova_investigacao()

    elif opcao_menu== 2:
        investigacoes.continuar_investigacao()

    elif opcao_menu==3:
        investigacoes.arquivo_casos()

    else:
        print("Opção inválida, tente novamente.")

    print("Continuando...")

