import PyPDF2 as pyf
from pathlib import Path
from datetime import datetime
from tkinter.filedialog import askopenfilename

arquivo = pyf.PdfMerger()
caminho = Path(askopenfilename(filetypes=[('PDF', '*.pdf')]))
while caminho.name != '':
    arquivo.append(caminho)
    caminho = Path(askopenfilename(filetypes=[('PDF', '*.pdf')]))
caminho_download = Path.home() / 'Downloads'
data_horario = str(datetime.now()).replace('-','').replace(' ','_').replace(':','').replace('.','')
with Path(caminho_download/'arquivo_mesclado_{}.pdf'.format(data_horario)).open(mode='wb') as arquivo_mesclado:
    arquivo.write(arquivo_mesclado)
