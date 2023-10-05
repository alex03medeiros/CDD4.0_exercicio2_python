vetorN = 30*[0]
num = 0
for n in range(30):
    vetorN[n] = int(input("Digite um numero para armazenar no Vetor N: "))

num = int(input("Digite um numero: "))
cont = 0
for x in range(30):
    if num == vetorN[x]:
        cont +=1

print("O numero {} se repete {} vezes no vetor N".format(num,cont))