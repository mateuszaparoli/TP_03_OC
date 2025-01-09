from math import log2
import sys

def printCabeçalho():
    print("="*16)
    print("IDX V ** ADDR **")

def main():
    

    #leitura dos argumentos
    tamCache = int(sys.argv[1]) # quantas bytes na cache
    tamLinha = int(sys.argv[2]) # quantos bytes por linha
    tamGrupo = int(sys.argv[3]) # quantas linhas por grupo
    #leitura do arquivo de entrada
    arquivoEntrada = sys.argv[4]
    with open(arquivoEntrada, 'r') as file:
        palavras = file.readlines()

    # calculando quantas linhas temos e offsets
    numLinhas = tamCache // tamLinha
    offsetPalavra = log2(tamLinha)
    numGrupos = numLinhas // tamGrupo

    #prints de debug
    print(offsetPalavra)
    print(numLinhas)
    for i in range(len(palavras)):
        print(palavras[i])

    # prints resultados
    for j in range(len(palavras)):
        printCabeçalho()
        for i in range(numLinhas):
            print(f"{i:03d}")

if __name__ == "__main__":
    main()