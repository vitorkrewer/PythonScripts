import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
from docx2pdf import convert
from pptx import Presentation
import svgtopdf


def convert_to_pdf():
    # Obter o tipo de arquivo selecionado
    file_type = file_type_var.get()
    
    # Abrir uma caixa de diálogo para selecionar o arquivo de origem
    file_path = filedialog.askopenfilename(filetypes=[(file_type.upper(), f'*.{file_type}')])
    
    if file_path:
        try:
            # Obter o diretório de salvamento do arquivo de origem
            save_dir = os.path.dirname(file_path)

            # Abrir uma caixa de diálogo para especificar o nome do arquivo de saída
            file_name = filedialog.asksaveasfilename(defaultextension='.pdf', initialdir=save_dir, filetypes=[('PDF', '*.pdf')])

            # Converter o arquivo para pdf
            if file_type == 'docx':
                convert(file_path, file_name)
            if file_type == 'svg':
                svg2pdf.convert_svg_to_pdf
                convert(file_path,file_name)
            elif file_type == 'ppt':
                presentation = Presentation(file_path)
                pdf_path = os.path.join(save_dir, file_name)
                presentation.export(pdf_path)
            
            messagebox.showinfo('Conversão Concluída', 'Arquivo convertido para PDF com sucesso!')
        except Exception as e:
            messagebox.showerror('Erro na Conversão', str(e))
    else:
        messagebox.showwarning('Nenhum arquivo selecionado', 'Selecione um arquivo para converter.')


# Criação da janela principal
root = tk.Tk()
root.title('Conversor de Arquivos para PDF')
root.geometry("350x200")

# Frame para seleção do tipo de arquivo
type_frame = tk.Frame(root)
type_frame.pack(pady=20)

# Variável para armazenar o tipo de arquivo selecionado
file_type_var = tk.StringVar()
file_type_var.set('docx')

# Rótulo e opções de seleção do tipo de arquivo
file_type_label = tk.Label(type_frame, text='Selecione o tipo de arquivo:')
file_type_label.pack(side=tk.LEFT)

file_type_menu = tk.OptionMenu(type_frame, file_type_var, 'docx', 'ppt', 'svg')
file_type_menu.pack(side=tk.LEFT)

# Botão para iniciar a conversão
convert_button = tk.Button(root, text='Selecione o Arquivo para Conversão', command=convert_to_pdf)
convert_button.pack(pady=10)

root.mainloop()