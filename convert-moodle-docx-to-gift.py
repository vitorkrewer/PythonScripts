from docx import Document
import docx2txt

def process_file(file_path):
    # Converter o arquivo Word para texto
    text = docx2txt.process(file_path)

    # Lista para armazenar o conteúdo processado
    processed_lines = []
    print(docx2txt)

    # Variável para controlar se estamos no parágrafo final de uma questão
    last_paragraph = False

    # Separar o texto em parágrafos
    paragraphs = text.split('\n')

    # Procurar por itens a), b), c), d) e e) no início dos parágrafos e substituir
    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if paragraph.startswith('a)'):
            if last_paragraph:
                processed_lines.append('}\n')
                last_paragraph = False
            processed_lines.append('{\n')
            processed_lines.append(paragraph.replace('a)', '=') + '\n')
        elif paragraph.startswith(('b)', 'c)', 'd)')):
            processed_lines.append(paragraph.replace(paragraph[:2], '~') + '\n')
        elif paragraph.startswith('e)'):
            processed_lines.append(paragraph.replace('e)', '~') + '}\n')
            last_paragraph = True
    if last_paragraph:
        processed_lines.append('}\n')

    # Criar o nome do arquivo de saída
    output_file_path = file_path.rsplit('.', 1)[0] + '-quest-moodle.txt'

    # Exportar o resultado para o arquivo de texto
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.writelines(processed_lines)

    print("Arquivo de saída gerado com sucesso!")

# Exemplo de uso
file_path = 'arquivo.docx'  # Caminho do arquivo Word de entrada
process_file(file_path)
