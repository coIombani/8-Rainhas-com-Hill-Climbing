import random
import time

#gera um estado aleatório inicial
def gerar_tabuleiro(n=8):
    return [random.randint(0, n - 1) for _ in range(n)]

#conta quantos conflitos existem no tabuleiro (função heurística h)
def contar_conflitos(tabuleiro):
    n = len(tabuleiro)
    conflitos = 0

    for i in range(n):
        for j in range(i + 1, n):
            #verifica ataque na mesma linha
            if tabuleiro[i] == tabuleiro[j]:
                conflitos += 1
            #verifica ataque na diagonal
            if abs(tabuleiro[i] - tabuleiro[j]) == abs(i - j):
                conflitos += 1

    return conflitos

#busca o melhor vizinho (steepest ascent)
def buscar_melhor_vizinho(tabuleiro):
    n = len(tabuleiro)
    melhor = list(tabuleiro)
    melhor_h = contar_conflitos(tabuleiro)

    #tenta mover cada rainha para todas as linhas possíveis
    for col in range(n):
        linha_original = tabuleiro[col]

        for linha in range(n):
            if linha == linha_original:
                continue

            temp = list(tabuleiro)
            temp[col] = linha
            h = contar_conflitos(temp)

            #se encontrou um estado melhor que o atual, guarda
            if h < melhor_h:
                melhor_h = h
                melhor = temp

    return melhor, melhor_h

#imprime tabuleiro
def imprimir_tabuleiro(tabuleiro):
    n = len(tabuleiro)
    print("\nTabuleiro:")
    print("  " + " ".join([str(i) for i in range(n)])) #parece meio estranho mas funciona pro cabeçalho
    for linha in range(n):
        lin = f"{linha} "
        for col in range(n):
            if tabuleiro[col] == linha:
                lin += "* "
            else:
                lin += ". "
        print(lin)
    print()

#hill climbing com random restart
def resolver_rainhas(n=8):
    limite_restarts = 100 #não vai ter muita utilidade pra um n baixo de rainhas

    total_passos = 0
    minimos_locais = 0
    restarts_usados = 0

    inicio_total = time.perf_counter()

    for tentativa in range(limite_restarts):
        atual = gerar_tabuleiro(n)
        print(f"\n{atual}") #so pra demonstração
        h_atual = contar_conflitos(atual)
        h_inicial = h_atual

        passos_da_tentativa = 0

        while True:
            #tenta achar vizinho com menos conflitos (subir encosta)
            vizinho, h_viz = buscar_melhor_vizinho(atual)

            #se o vizinho não é melhor, chegamos num topo (local ou global)
            if h_viz >= h_atual:
                if h_atual > 0:
                    minimos_locais += 1 #travou num mínimo local
                break

            atual = vizinho
            h_atual = h_viz
            passos_da_tentativa += 1

        total_passos += passos_da_tentativa
        restarts_usados = tentativa

        #se h=0, achamos o mínimo global (solução)
        if h_atual == 0:
            fim_total = time.perf_counter()
            tempo_total = (fim_total - inicio_total) * 1000

            print(f"Solução foi encontrada")
            print(f"H inicial: {h_inicial}")
            print(f"H final: {h_atual}")
            print(f"Passos totais acumulados: {total_passos}")
            print(f"Mínimos locais: {minimos_locais}")
            print(f"Tempo total: {tempo_total:.3f} ms")
            print(f"Vetor Solução: {atual}")
            imprimir_tabuleiro(atual)
            return atual

    print("Nenhuma solução encontrada após limite de restarts.")
    return None

if __name__ == "__main__":
    resolver_rainhas()