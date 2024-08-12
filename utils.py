def ler_arquivo_cpf(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        cpfs = file.read().splitlines()
    return cpfs
