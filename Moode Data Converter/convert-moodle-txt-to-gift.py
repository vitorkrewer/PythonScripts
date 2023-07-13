import traceback

try:
    # Função para processar o arquivo
    def process_file(file_path):
        # Ler o arquivo txt com a codificação correta
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Procurar por itens a), b), c), d) e e) no início dos parágrafos e substituir
        for i in range(len(lines)):
            line = lines[i].strip()
            if line.startswith('a)'):
                lines.insert(i, '{\n')
                lines[i+1] = line.replace('a)', '=') + '\n'
            elif line.startswith(('b)', 'c)', 'd)')):
                lines[i] = line.replace(line[:2], '~') + '\n'
            elif line.startswith('e)'):
                lines[i] = line.replace('e)', '~') + '\n}'
                lines[i] += '\n'

        # Criar o nome do arquivo de saída
        output_file_path = file_path.rsplit('.', 1)[0] + '-quest-moodle.' + file_path.rsplit('.', 1)[1]

        # Exportar o resultado para o arquivo
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)

    # Exemplo de uso
    file_path = 'afd-e1-2023-historia-da-educacao.txt'  # Caminho do arquivo de entrada
    process_file(file_path)
    print("Arquivo de saída gerado com sucesso!")

except Exception as e:
    traceback.print_exc()
