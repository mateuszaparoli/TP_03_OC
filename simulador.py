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
    #print(palavrasBin)
    
    #retirando o offset de palavra e de grupo
    palavrasBin = [palavra[:-int(offsetPalavra)].zfill(32) for palavra in palavrasBin]
    grupoPorPalavra = [0] * len(palavrasBin)
    if offsetGrupo > 0:
        for i, palavra in enumerate(palavrasBin):
                grupoPorPalavra[i] = int(palavra[-int(offsetGrupo):], 2)
        palavrasBin = [palavra[:-int(offsetGrupo)].zfill(32) for palavra in palavrasBin]
    #palavrasBin = [palavra[:-int(offsetPalavra + offsetGrupo)].zfill(32) for palavra in palavrasBin]
    #print(palavrasBin)
    if offsetGrupo > 0:
        print(grupoPorPalavra)

    #obtendo os identificadores
    addrs = [f"0x{hex(int(palavra, 2))[2:].zfill(8).upper()}" for palavra in palavrasBin]
    #print(addrs)

    #matriz do bit de validade para cada linha
    validades = [[0] * linhasPorGrupo] * associatividade
    enderecosAlocados = [[-1] * linhasPorGrupo] * associatividade #matriz pra guardar os endereços já presentes na cahce
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

        for i in range(linhasPorGrupo):
            #print(f"{i:03d} {validades[i]}")
            if enderecosAlocados[grupoPorPalavra[j]] == addrs[j]:
                achou = True
                hit += 1
                break

        if achou == False:    
            enderecosAlocados[grupoPorPalavra[j]][num_enderecosAlocados[grupoPorPalavra[j]] % associatividade] = addrs[j]
            validades[grupoPorPalavra[j]][num_enderecosAlocados[grupoPorPalavra[j]] % associatividade] = 1
            num_enderecosAlocados[grupoPorPalavra[j]] += 1
            miss += 1
            # for l in range(numLinhas):
            #     if enderecosAlocados[l] == -1:
            #         enderecosAlocados[l] = addrs[j]
            #         validades[l] = 1
            #         miss += 1
            #         break
        
        for i in range(associatividade):
            for j in range(linhasPorGrupo):
                enderecoLinha = f"{enderecosAlocados[i][j]}" if enderecosAlocados[i][j] != -1 else ""
                print(f"{i:03d} {validades[i][j]} {enderecoLinha}")
            
    print("")                
    print(f"#hits: {hit}")
    print(f"#miss: {miss}")

if __name__ == "__main__":
    main()