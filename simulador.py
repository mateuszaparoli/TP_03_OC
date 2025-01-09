from math import log2
import sys

def printCabeçalho():
    print("="*16)
    print("IDX V ** ADDR **")

def main():
    
    tamCache = int(sys.argv[1]) # quantas bytes na cache
    tamLinha = int(sys.argv[2]) # quantos bytes por linha
    tamGrupo = int(sys.argv[3]) # quantas linhas por grupo
    arquivoEntrada = sys.argv[4]

    # calculando quantas linhas temos
    numLinhas = tamCache // tamLinha

    offsetPalavra = log2(tamLinha)

    printCabeçalho()

    

if __name__ == "__main__":
    main()