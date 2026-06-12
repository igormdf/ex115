from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = 'arquivo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu('Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema')
    if resposta == 1:
        #listar o conteúdo de um aqrquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        print('Opção 3')
        cabeçalho('Saindo so sistema... até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)