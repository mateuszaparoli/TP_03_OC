import sys

def main():
    
    tamanhoCache = int(sys.argv[1]) # quantas bytes na cache
    tamanhoLinha = int(sys.argv[2]) # quantos bytes por linha
    tamanhoGrupo = int(sys.argv[3]) # quantas linhas por grupo
    arquivoEntrada = sys.argv[4]

    # calculando quantas linhas temos
    linhas = tamanhoCache // tamanhoLinha


if __name__ == "__main__":
    main()