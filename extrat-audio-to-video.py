from moviepy.editor import VideoFileClip

def extract_audio(input_file,output_file):
    video = VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile(output_file)

# Configuração dos Dados de Entrada e Saída - Especificar caminhos absolutos incluíndo nome do arquivo com extensão
input_file = 'C:/Users/hp-14-vmk/OneDrive - Grupo Focus/faculdade-focus/equipe-multidisciplinar/reunioes-videos/reuniao-multi-03-07-23.mp4'
output_file = 'C:/Users/hp-14-vmk/OneDrive - Grupo Focus/faculdade-focus/equipe-multidisciplinar/reunioes-videos/reuniao-multi-03-07-23.mp3'  # Arquivo de áudio de saídas

extract_audio(input_file,output_file)
print("Áudio extraído com sucesso!")