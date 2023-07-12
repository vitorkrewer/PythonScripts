def check_line_length(filename, limit=70):
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            for i, line in enumerate(file, start=1): 
                if len(line.rstrip('\n')) > limit:  # rstrip('\n') é usado para não contar o caractere de nova linha
                    print(f"Linha {i} tem mais de {limit} caracteres: {line.strip()}")
    except FileNotFoundError:
        print(f"O arquivo {filename} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

# Use a função passando o nome do arquivo de texto que você quer analisar
check_line_length('disciplinas-cenes-facupar.txt')