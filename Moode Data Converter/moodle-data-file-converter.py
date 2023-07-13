import tkinter as tk
from tkinter import filedialog, messagebox
from subprocess import call
from docx import Document
import docx2txt

def convert_docx_to_txt():
    # Selecionar o arquivo para processar
    file_path = filedialog.askopenfilename(filetypes=[('Documentos Word', '*.docx')])

    # Verificar se um arquivo foi selecionado
    if file_path:
        
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


    # Caixa de diálogo para selecionar o local de saída
    output_file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Arquivos de Texto', '*.txt')])

    if output_file_path:
        # Exportar o resultado para o arquivo de texto
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.writelines(processed_lines)
        messagebox.showinfo('Sucesso', 'Arquivo de saída gerado com sucesso!')

def convert_notas_to_excel():
    input_file = filedialog.askopenfilename(filetypes=[('Planilhas', '*.csv')])
    if input_file:
        call(['python', 'calcular-notas-export-excel.py', input_file, output_file])
        messagebox.showinfo('Conversão Concluída', 'Arquivo de saída gerado com sucesso!')

def convert_notas_to_html():
    input_file = filedialog.askopenfilename(filetypes=[('Planilhas', '*.csv')])
    if input_file:
        call(['python', 'calcular-notas-export-html.py', input_file, output_file])
        messagebox.showinfo('Conversão Concluída', 'Arquivo de saída gerado com sucesso!')

def convert_txt_to_txt():
    input_file = filedialog.askopenfilename(filetypes=[('Arquivos de Texto', '*.txt')])
    if input_file:
        call(['python', 'convert-moodle-txt-to-gift.py', input_file, output_file])
        messagebox.showinfo('Conversão Concluída', 'Arquivo de saída gerado com sucesso!')

root = tk.Tk()
root.title('Moodle Data Converter')

# Definir as propriedades da janela
root.geometry("500x300")

# Insere um texto na janela
text_label = tk.Label(root, text="Conversor de Arquivos para Moodle!")
text_label.pack()

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Arquivo', menu=file_menu)
file_menu.add_command(label='Converter de DOCX para TXT', command=convert_docx_to_txt)
file_menu.add_command(label='Converter de TXT para TXT', command=convert_txt_to_txt)

notas_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Notas', menu=notas_menu)
notas_menu.add_command(label='Converter Notas CSV to Excel', command=convert_notas_to_excel)
notas_menu.add_command(label='Converter Notas CSV to HTML', command=convert_notas_to_html)

menu_bar.add_command(label='Sair', command=root.quit)

root.config(menu=menu_bar)
root.mainloop()