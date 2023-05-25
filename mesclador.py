import PyPDF2 as pyf
from pathlib import Path
from datetime import datetime
from tkinter.filedialog import askopenfilename

arquivo = pyf.PdfFileMerger()
print(arquivo, type(arquivo))
caminho = Path(askopenfilename(filetypes=[('PDF', '*.pdf')]))
print(caminho, type(caminho))
while caminho.name != '':
    arquivo.append(caminho)
    caminho = Path(askopenfilename(filetypes=[('PDF', '*.pdf')]))
caminho_download = Path.home() / 'Downloads'
data_horario = str(datetime.now()).replace('-','').replace(' ','_').replace(':','').replace('.','')
with Path(caminho_download/'arquivo_mesclado_{}.pdf'.format(data_horario)).open(mode='wb') as arquivo_mesclado:
    arquivo.write(arquivo_mesclado)
