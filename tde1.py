import os

def uniao(grupo1, grupo2):
    return grupo1.union(grupo2)

def intersecao(grupo1, grupo2):
    return grupo1.intersection(grupo2)

def diferenca(grupo1, grupo2):
    return grupo1.difference(grupo2)

def produto_cartesiano(grupo1, grupo2):
    return {(x, y) for x in grupo1 for y in grupo2}

# Caminho para o arquivo .txt#
nome_arquivo = os.path.expanduser("~/Downloads/dados2.txt")

def processar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {nome_arquivo}")
        return

    num_operacoes = int(linhas[0].strip())
    indice = 1

    resultados = []

    for _ in range(num_operacoes):
        operacao = linhas[indice].strip()
        grupo1 = set(linhas[indice + 1].strip().split(', '))
        grupo2 = set(linhas[indice + 2].strip().split(', '))
        indice += 3

        if operacao == 'U':
            resultado = uniao(grupo1, grupo2)
            resultados.append(f"União: conjunto 1 {grupo1}, conjunto 2 {grupo2}. Resultado: {resultado}")
        elif operacao == 'I':
            resultado = intersecao(grupo1, grupo2)
            resultados.append(f"Interseção: conjunto 1 {grupo1}, conjunto 2 {grupo2}. Resultado: {resultado}")
        elif operacao == 'D':
            resultado = diferenca(grupo1, grupo2)
            resultados.append(f"Diferença: conjunto 1 {grupo1}, conjunto 2 {grupo2}. Resultado: {resultado}")
        elif operacao == 'C':
            resultado = produto_cartesiano(grupo1, grupo2)
            resultados.append(f"Produto Cartesiano: conjunto 1 {grupo1}, conjunto 2 {grupo2}. Resultado: {resultado}")
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    processar_arquivo(nome_arquivo)
