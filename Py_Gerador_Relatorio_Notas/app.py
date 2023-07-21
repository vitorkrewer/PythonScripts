"""
Gerador de Relatório de Notas
Autor: Vitor Krewer
Data: 17/07/2023
Descrição: Ao executar a aplicação, um servidor Flask é iniciado e possibilita ao usuário calcular e gerar notas de alunos conforme regras descritas da função calcular_nota. O objetivo é trabalhar com arquivos exportados do sistema de Relatório de Notas do Moodle.
Poder ser executado via Terminal via py.exe ou python.exe app.py ou, para usuários do Windows, via arquivo .bat.
O arquivo do Excel enviado tem 4 colunas, Nome, Sobrenome, e os 3 tipos de notas. Irá juntar o nome e o sobrenome em uma única coluna e calcular a nota final do aluno.
"""

from flask import Flask, render_template, request, redirect, url_for, send_file
import pandas as pd
import openpyxl
import os
import io
from html import escape
import xlsxwriter

app = Flask(__name__)
print(app.root_path)

df_results = None

# Função que calcula a nota com as seguintes condições: soma (EF+AFD). Nota final (resultado de soma) divide por 2 soma ao valor da APD.
def calcular_nota(APD, AFD, EF):
    soma = EF + AFD
    nota_final = soma/2 + APD

    if nota_final >= 6.0:
        status = 'aprovado'
    else:
        status = 'reprovado'
    
    # Arredonda a nota_final para 10.0, se for maior ou igual a 10.0
    nota_final = min(nota_final, 10.0)
    return nota_final, status

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        upload_folder = os.path.join(app.root_path, 'upload')
        file = request.files['file']
        file_path = os.path.join(upload_folder, file.filename)
        file.save(file_path)
        process_file(file_path, os.path.join('templates', 'result.html'))
        
        # Retorne uma resposta válida após o processamento
        return render_template('result.html')

# Função que processa as informações do arquivo. 
def process_file(in_file, out_file):
    global df_results  # Informar que está se referindo à variável global
    df = pd.read_excel(in_file)
    df['Nome do Aluno'] = df[['Nome', 'Sobrenome']].apply(lambda x: ' '.join(x), axis=1) # Juntar as colunas Nome e Sobrenome e uma única Nome do Aluno
    global df_results  # Informar que está se referindo à variável global
    def convert_to_float(val):
        try:
            return float(val)
        except ValueError:
            return None
    
    # Substituir "-" por 0 nas colunas APD, AFD e EF. Em arquivos gerados de Notas gerados pelo Moodle, é utilizado "," ao invés do "."
    df['APD'] = df['APD'].replace('-', 0)
    df['AFD'] = df['AFD'].replace('-', 0)
    df['EF'] = df['EF'].replace('-', 0)

    # Converter Dados em formato Float
    df['APD'] = df['APD'].apply(convert_to_float)
    df['AFD'] = df['AFD'].apply(convert_to_float)
    df['EF'] = df['EF'].apply(convert_to_float)

    resultados = []

    for index, row in df.iterrows():
        APD = float(row['APD'])
        AFD = float(row['AFD'])
        EF = float(row['EF'])
        nota_final, status = calcular_nota(APD, AFD, EF)
        resultados.append([row['Nome do Aluno'], nota_final, status])
   
    resultados.sort(key=lambda x: x[2])


    with open(out_file, 'w', encoding='UTF-8') as file_out:
        # Limpar o conteúdo anterior do arquivo
        file_out.write('<html>\n<head>\n<title>Resultados</title>\n</head>\n<body>\n')
        file_out.write('<p style="text-align: center;"><a href="/voltar">Voltar</a></p>')  # Adiciona o botão "Voltar"
        file_out.write('<p style="text-align: justify;"><a href="/download">Baixar resultados em Excel</a><br></p>')
        file_out.write('<table border="1">\n')
        file_out.write('<tr><th>Nome do Aluno</th><th>Nota Final</th><th>Situação</th></tr>\n')
        for resultado in resultados:
            file_out.write(f'<tr><td>{escape(resultado[0])}</td><td>{resultado[1]}</td><td>{escape(resultado[2])}</td></tr>\n')
        file_out.write('</table>\n')
        file_out.write('</body>\n</html>')
        df_results = pd.DataFrame(resultados, columns=['Nome do Aluno', 'Nota Final', 'Situação'])

@app.route('/voltar')
def voltar():
    # Rota para voltar à página inicial
    return redirect(url_for('home'))


@app.route('/download')
def download_file():
    # Garante que df_results não é None e possui dados
    if df_results is not None and not df_results.empty:
        # Escreve o DataFrame para um arquivo Excel na memória
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df_results.to_excel(writer, index=False)
        output.seek(0)
        # Salva o arquivo Excel no disco
        filename = 'result.xlsx'  # Nome do arquivo a ser baixado
        filepath = os.path.join(app.config['DOWNLOAD_FOLDER'], filename)
        with open(filepath, 'wb') as file:
            file.write(output.read())
        # Retorna o arquivo para download
        return send_file(filepath, as_attachment=True)
    else:
        # Se df_results é None ou vazio, retorna uma mensagem de erro ou redireciona para uma página de erro
        return "Erro: nenhum resultado disponível para download."

DOWNLOAD_FOLDER = os.path.join(app.root_path, 'download')
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER


@app.route('/encerrar')
def encerrar():
    # Encerra o servidor Flask enviando o sinal SIGINT (equivalente a Ctrl+C)
    os.kill(os.getpid(), 2)

if __name__ == '__main__':
    app.run(debug=True)
