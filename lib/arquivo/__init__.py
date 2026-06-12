from rich import print
from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome,'rt')

    except FileNotFoundError:
        return False
    
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')

    except:
        print('[red]Houve um ERRO ao criar o arquivo![[/]]')
    
    else:
        print(f'[green]Arquivo {nome} criado com sucesso![/] ')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    
    except:
        print('Erro ao ler o arquivo')

    else:
        cabeçalho('Pessoas cadastradas')
        print(a.read())