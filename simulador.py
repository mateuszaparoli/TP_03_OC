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
    associatividade = numLinhas // linhasPorGrupo # aqui é o numero de grupos
    offsetPalavra = log2(tamLinha)
    offsetGrupo = log2(associatividade) # aqui é o numero de bits para identificar o grupo
    #offsetPalavra = int(log2(tamLinha))  # Número de bits do offset da palavra
    #offsetGrupo = int(log2(associatividade))  # Número de bits do grupo


    # obter as palavras de entrada em binário
    palavrasBin = [bin(palavra)[2:].zfill(32) for palavra in palavras]
    #print(palavrasBin)
    
    #retirando o offset de palavra e de grupo
    palavrasBin = [palavra[:-int(offsetPalavra)].zfill(32) for palavra in palavrasBin]
    grupoPorPalavra = [0] * len(palavrasBin)
    #if associatividade > 1:
    #    grupoPorPalavra = [int(palavra[-offsetGrupo:], 2) for palavra in palavrasBin]  # Calcular o grupo
    #    palavrasBin = [palavra[:-offsetGrupo] for palavra in palavrasBin]  # Remover offset de grupo
    #else:
    #    grupoPorPalavra = [0] * len(palavrasBin)  # Apenas 1 grupo
    if offsetGrupo > 0:
        for i, palavra in enumerate(palavrasBin):
            grupoPorPalavra[i] = (int(palavra[-int(offsetGrupo):], 2) % associatividade) #Mudei essa linha Ricardo
        palavrasBin = [palavra[:-int(offsetGrupo)].zfill(32) for palavra in palavrasBin]
    #palavrasBin = [palavra[:-int(offsetPalavra + offsetGrupo)].zfill(32) for palavra in palavrasBin]

    #obtendo os identificadores
    addrs = [f"0x{hex(int(palavra, 2))[2:].zfill(8).upper()}" for palavra in palavrasBin]
    #print(addrs)

    #matriz do bit de validade para cada linha
    validades = [[0] * linhasPorGrupo for _ in range(associatividade)]
    enderecosAlocados = [[-1] * linhasPorGrupo for _ in range(associatividade)]  # Matriz para guardar os endereços já presentes na cache
    num_enderecosAlocados = [0] * associatividade #vetor para guardar quant de blocos em cada conjunto

    #prints de debug
    #print(offsetPalavra)
    #print(numLinhas)
    #for i in range(len(palavras)):
    #    print(palavras[i])

    #AGORA TEMOS QUE VER A LÓGICA DE PREENCHER AS LINHAS DA SAIDA UMA A UMA E PRINTAR O RESULTADO
    achou = False
    hit = 0
    miss = 0

    # prints resultados
    for j in range(len(palavras)):
        printCabeçalho()
        achou = False

        if addrs[j] in enderecosAlocados[grupoPorPalavra[j]]:
            achou = True
            hit += 1

        if not achou:
            grupo = grupoPorPalavra[j]
            enderecosAlocados[grupo][num_enderecosAlocados[grupo] % linhasPorGrupo] = addrs[j]
            validades[grupo][num_enderecosAlocados[grupo] % linhasPorGrupo] = 1
            num_enderecosAlocados[grupo] += 1
            miss += 1

        k = 0
        for i in range(associatividade):
            for l in range(linhasPorGrupo):
                enderecoLinha = f" {enderecosAlocados[i][l]}" if enderecosAlocados[i][l] != -1 else ""
                print(f"{k:03d} {validades[i][l]}{enderecoLinha}")
                k += 1

    print("")
    print(f"#hits: {hit}")
    print(f"#miss: {miss}")

if __name__ == "__main__":
    main()
