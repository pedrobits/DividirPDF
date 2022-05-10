from asyncio import sleep
from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import msvcrt
from time import sleep

# PDF
arquivo = "arquivo.pdf"

# Criando uma função com a biblioteca msvcrt para "press any key for continue"

def wait():
    msvcrt.getch()

# Entrada do arquivo PDF que será divido
inputpdf = PdfFileReader(open(arquivo, "rb"))

# Criando uma função com a biblioteca PyPDF2 para dividir as folhas do PDF

def separar():
    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open("pagina%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)

# Var guardando a quantidade de paginas
numero_de_paginas = inputpdf.numPages

# Input com a decisão de NÃO ou SIM para dividir o PDF
pergunta1 = input(
    "O numero de paginas a serem divididas é de {}. Deseja continuar? (Sim ou Não): ".format(numero_de_paginas))
resposta = pergunta1.upper()

if resposta == "SIM" or "YES":
    print("Separando...")
    sleep(2)
    separar()
    print("Foi!")
elif resposta == "NÃO" or "NAO":
    print("Obrigado por usar o Agille PDFSPLITER")
    print("Pressione Qualquer Botão para sair")
    wait()
    sys.exit()
else:
    print("Comando Invalido")
    sys.exit()
