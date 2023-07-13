import csv
import pandas as pd

def calcular_nota(APD, AFD, EF):
    soma = APD + AFD
    if soma >= 6.0:
        nota_final = soma
    else:
        nota_final = (soma + EF) / 2

    if nota_final >= 6.0:
        status = 'aprovado'
    else:
        status = 'reprovado'
    return nota_final, status

# lista para armazenar resultados
resultados = []

with open('notas.csv', 'r', encoding='UTF-8') as file_in:
    csv_reader = csv.reader(file_in)
    next(csv_reader)  # Pula o cabeçalho, se houver
    for row in csv_reader:
        if len(row) < 4:  # Se a linha não tem pelo menos 4 elementos
            continue  # Pule para a próxima linha
        Nome = row[0]
        APD = float(row[1])
        AFD = float(row[2])
        EF = float(row[3])
        nota_final, status = calcular_nota(APD, AFD, EF)
        # adiciona resultado à lista de resultados
        resultados.append([Nome, nota_final, status])

# ordena a lista de resultados pela situação (aprovado/reprovado)
resultados.sort(key=lambda x: x[2])

# cria um DataFrame pandas a partir da lista de resultados
df = pd.DataFrame(resultados, columns=['Nome do Aluno', 'Nota Final', 'Situação'])

# grava o DataFrame como um arquivo Excel
df.to_excel('resultados.xlsx', index=False)