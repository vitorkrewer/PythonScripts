"""
Conversor de Questões de Arquivos DOCX para TXT
Autor: Vitor Krewer
Data: 01/01/2023
Descrição: O Script converte questões de múltipla escolha de um arquivo .docx para txt para a sintaxe GIFT aceita pelo Moodle no módulo de importação de questões.
"""

# Importações
from docx import Document

# Função para converter .docx em .txt
def convert_docx_to_txt(input_file, output_file):
    # Ler o documento .docx
    doc = Document(input_file)
    
    # Extrair o texto dos parágrafos
    paragraphs = [p.text for p in doc.paragraphs]
    
    # Juntar os parágrafos em um único texto preservando as quebras de linha originais
    text = '\n\n'.join(paragraphs)
    
    # Procurar por itens a), b), c), d) e e) no início dos parágrafos e substituir
    lines = text.split('\n\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith('a)'):
            lines.insert(i, '{\n')
            lines[i+1] = line.replace('a)', '=')
        elif line.startswith(('b)', 'c)', 'd)')):
            lines[i] = line.replace(line[:2], '~')
        elif line.startswith('e)'):
            lines[i] = line.replace('e)', '~') + '\n}\n'

    # Salvar o texto no arquivo .txt de saída
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines('\n'.join(lines))

# Exemplo de uso
input_file = 'arquivo.docx'  # Arquivo .docx de entrada
output_file = 'saida.txt'  # Arquivo .txt de saída

# Chamar a função para converter o arquivo
convert_docx_to_txt(input_file, output_file)

# Exibir mensagem de sucesso
print("Arquivo de saída gerado com sucesso!")
