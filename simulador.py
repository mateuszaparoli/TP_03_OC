from math import log2, ceil
import sys

def printCabeçalho():
    print("="*16)
    print("IDX V ** ADDR **")

def main():
    
    #leitura dos argumentos
    tamCache = int(sys.argv[1]) # quantas bytes na cache
    tamLinha = int(sys.argv[2]) # quantos bytes por linha(bloco)
    linhasPorGrupo = int(sys.argv[3]) # quantos blocos(linhas) por grupo
    #leitura do arquivo de entrada
    arquivoEntrada = sys.argv[4]
    with open(arquivoEntrada, 'r') as file:
        palavras = [int(linha.strip(), 16) for linha in file]

    # calculando quantas linhas temos e offsets
    numLinhas = tamCache // tamLinha
    associatividade = numLinhas // linhasPorGrupo
    offsetPalavra = log2(tamLinha)
    offsetGrupo = log2(associatividade) # numero de grupos

    # obter as palavras de entrada em binário
    palavrasBin = [bin(palavra)[2:].zfill(32) for palavra in palavras]
    print(palavrasBin)
    
    #retirando o offset de palavra e de grupo
    palavrasBin = [palavra[:-int(offsetPalavra)].zfill(32) for palavra in palavrasBin]
    if offsetGrupo > 0:
        grupoPorPalavra = [int(palavra[-int(offsetGrupo):], 2) for palavra in palavrasBin]
        palavrasBin = [palavra[:-int(offsetGrupo)].zfill(32) for palavra in palavrasBin]
    #palavrasBin = [palavra[:-int(offsetPalavra + offsetGrupo)].zfill(32) for palavra in palavrasBin]
    print(palavrasBin)
    if offsetGrupo > 0:
        print(grupoPorPalavra)

    #obtendo os identificadores
    addrs = [f"0x{hex(int(palavra, 2))[2:].zfill(8).upper()}" for palavra in palavrasBin]
    print(addrs)

    #vetor do bit de validade para cada linha
    validades = [0] * numLinhas

    #AGORA TEMOS QUE VER A LÓGICA DE PREENCHER AS LINHAS DA SAIDA UMA A UMA E PRINTAR O RESULTADO

    #prints de debug
    #print(offsetPalavra)
    #print(numLinhas)
    #for i in range(len(palavras)):
    #    print(palavras[i])

    # prints resultados
    for j in range(len(palavras)):
        printCabeçalho()
        for i in range(numLinhas):
            print(f"{i:03d} {validades[i]}")

if __name__ == "__main__":
    main()