arquivos = ["Roubo","Assalto"]

arquivos.append("Sequestro")


def nova_investigacao():
    print("Iniciando nova investigação...")

def continuar_investigacao():
    print("Continuando investigação...")

def excluir_caso():
    nome_caso=input("Digite o nome do caso que deseja excluir: ")
    if nome_caso in arquivos:
        arquivos.remove(nome_caso)
        print(f"Caso {nome_caso} excluído com sucesso.")
    else:
        print("Caso não encontrado na lista.")
        excluir_caso()

def arquivo_casos():
    print("Abrindo arquivos de casos...")
    for numerador, arquivo in enumerate(arquivos, start=1):
        print(numerador, arquivo)

    
    while True:
        exclusao=input("Deseja excluir um caso (S/N)? ")

        if exclusao=="S" or exclusao=="s":
            excluir_caso()
            break
        elif exclusao=="N" or exclusao=="n":
            print("Voltando ao menu...")
            break
        else:
            print("Opção inválida, digite novamente.")
