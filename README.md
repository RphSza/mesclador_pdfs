# Descrição
 Mescla arquivos PDF na ordem selecionada, salvando o resultado na pasta downloads do usuário.

## Racional
- cria um objeto do tipo PdfFileMerger vazio, que receberá os arquivos PDF;
- os arquivos PDF são selecionados pelo usuário por meio do método askopenfilename(), com parâmetro filetypes= definido para receber apenas arquivos com extensão .pdf;
- os arquivos PDF selecionados geram um objeto do tipo Path, cujos nomes são verificados por meio da propridade name;
- dentro do laço while, o objeto PdfFileMerger recebe os arquivos PDF selecionados, um a um, por meio do método append();
- o laço se encerra quando o usuário não seleciona mais arquivos PDF, quando o nome do arquivo selecionado passa a ser vazio;
- uma vez pronto objeto PdfFileMerger, define-se o caminho da pasta downloads do usuário, por meio do método Path.home();
- define-se também a data e horário da mesclagem, por meio do método datetime.now(), convertendo o resultado para string;
- por fim, o arquivo PDF mesclado é salvo na pasta downloads do usuário, com nome arquivo_mesclado_data_horario.pdf, por meio do método write().

## Observações
- o caminho da pasta Downloads com Path.home() serve para qualquer sistema operacional, pois o caminho é definido pelo sistema operacional, não pelo usuário;
- a data e horário da mesclagem servem para evitar que arquivos com o mesmo nome sejam sobrescritos.
