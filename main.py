import requests # type: ignore
from config import API_URL, API_TOKEN

def consultar_pix(cpf):
    url = f"{API_URL}/{cpf}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  # Adaptar conforme o retorno da API
    else:
        return None

from utils import ler_arquivo_cpf

def processar_cpfs(cpfs):
    resultados = []
    for cpf in cpfs:
        resultado = consultar_pix(cpf)
        if resultado:
            resultados.append({"CPF": cpf, "Possui_Chave_PIX": True})
        else:
            resultados.append({"CPF": cpf, "Possui_Chave_PIX": False})
    return resultados

import pandas as pd # type: ignore

def salvar_resultados(resultados, caminho_saida):
    df = pd.DataFrame(resultados)
    df.to_csv(caminho_saida, index=False)

def main():
    caminho_arquivo = "lista_cpfs.txt"
    cpfs = ler_arquivo_cpf(caminho_arquivo)
    resultados = processar_cpfs(cpfs)
    salvar_resultados(resultados, "resultado_pix.csv")

if __name__ == "__main__":
    main()
