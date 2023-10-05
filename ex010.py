n = int(input("Digite um numero para o tamanho dos vetores: "))
vetorA = n*[0]
vetorB = n*[0]
vetorS = n*[0]
for a in range (n):
    vetorA[a] = int(input("Digite um valor para o Vetor A: "))
    vetorB[a] = int(input("Digite um valor para o Vetor B: "))
    vetorS[a] = vetorA[a] + vetorB[a]

print(vetorA)
print("+")
print(vetorB)
print("=")
print(vetorS)