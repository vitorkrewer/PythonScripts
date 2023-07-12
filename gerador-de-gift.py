import tkinter as tk
from tkinter import filedialog, messagebox
from subprocess import call
from tkinter import filedialog

def convert_docx_to_txt():
    input_file = filedialog.askopenfilename(filetypes=[('Documentos Word', '*.docx')])
    if input_file:
        output_file = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Arquivos de Texto', '*.txt')])
        if output_file:
            call(['python', 'convert-moodle-txt-to-gift.py', input_file, output_file])
            messagebox.showinfo('Conversão Concluída', 'Arquivo de saída gerado com sucesso!')

def convert_notas_to_excel():
    input_file = filedialog.askopenfilename(filetypes=[('Planilhas', '*.csv')])
    if input_file:
        call(['python', 'calcular-notas-export-excel.py', input_file])
        messagebox.showinfo('Conversão Concluída', 'Arquivo de saída gerado com sucesso!')

def convert_notas_to_html():
    input_file = filedialog.askopenfilename(filetypes=[('Planilhas', '*.csv')])
    if input_file:
        call(['python', 'calcular-notas-export-html.py', input_file])
        messagebox.showinfo('Conversão Concluída', 'Arquivo de saída gerado com sucesso!')

def convert_txt_to_txt():
    input_file = filedialog.askopenfilename(filetypes=[('Arquivos de Texto', '*.txt')])
    if input_file:
        call(['python', 'convert-moodle-txt-to-gift.py', input_file])
        messagebox.showinfo('Conversão Concluída', 'Arquivo de saída gerado com sucesso!')

root = tk.Tk()
root.title('Conversor de Arquivos')

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
