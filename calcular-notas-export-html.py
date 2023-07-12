import csv
from html import escape

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
        aluno = row[0]
        APD = float(row[1])
        AFD = float(row[2])
        EF = float(row[3])
        nota_final, status = calcular_nota(APD, AFD, EF)
        # adiciona resultado à lista de resultados
        resultados.append([aluno, nota_final, status])

# ordena a lista de resultados pela situação (aprovado/reprovado)
resultados.sort(key=lambda x: x[2])

with open('resultados.html', 'w', encoding='UTF-16') as file_out:
    # escreve o cabeçalho HTML e inicia a tabela
    file_out.write('<html>\n<head>\n<title>Resultados</title>\n</head>\n<body>\n')
    file_out.write('<table border="1">\n<tr><th>Nome do Aluno</th><th>Nota Final</th><th>Situação</th></tr>\n')

    for resultado in resultados:
        # usa a função escape() para garantir que os dados estejam em formato HTML seguro
        file_out.write(f'<tr><td>{escape(resultado[0])}</td><td>{resultado[1]}</td><td>{escape(resultado[2])}</td></tr>\n')

    # finaliza a tabela e o HTML
    file_out.write('</table>\n</body>\n</html>')