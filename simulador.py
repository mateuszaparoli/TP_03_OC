import sys

def main():
    
    tamCache = int(sys.argv[1]) # quantas bytes na cache
    tamLinha = int(sys.argv[2]) # quantos bytes por linha
    tamGrupo = int(sys.argv[3]) # quantas linhas por grupo
    arquivoEntrada = sys.argv[4]

    # calculando quantas linhas temos
    numLinhas = tamCache // tamLinha


if __name__ == "__main__":
    main()