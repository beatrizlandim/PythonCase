arquivos = ["Roubo","Assalto"]

arquivos.append("Sequestro")


def nova_investigacao():
    print("Iniciando nova investigação...")

def continuar_investigacao():
    print("Continuando investigação...")

def arquivo_casos():
    print("Abrindo arquivos de casos...")
    for numerador, arquivo in enumerate(arquivos, start=1):
        print(numerador, arquivo)


