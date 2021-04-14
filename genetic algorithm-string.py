#n자리의 문자열이 자연선택을 반복하면서 최종 문자열에 가까워지는 현상을 관찰합니다.
from matplotlib import pyplot as plt
import numpy as np
import random

def set_random_string(n): #n자리의 랜덤 문자열을 생성
    str1 = ""
    for i in range(n):
        str1 += chr(random.randrange(ord('A'), ord('Z')+1))
    return str1

def measure_fitness(gene): #최종값과의 유사도 측정
    score = 0
    for i in range(length_of_genes):
        if final[i]==gene[i]:
            score += 1
    return score

def crossover(genes): #자연선택된 유전자를 가지고 후대 유전자를 만듬
    for i in range(number_of_genes):
        str1 = ""
        switch_dna = random.randrange(0, length_of_genes)
        for j in range(length_of_genes):
            if j==switch_dna:
                str1 += chr(random.randrange(ord('A'), ord('Z')+1))
            else:
                str1 += genes[i%2][j]
        gene[i] = str1

final = "DIGITALMEDIA" #최종값
number_of_genes = 100 #유전자 갯수
loop = 1000 #반복 횟수

length_of_genes = len(final) #유전자 길이
gene = []
fitness = []

for i in range(number_of_genes):
    gene.append(set_random_string(length_of_genes))

for i in range(loop):
    print(f"{i+1}대 유전자 : {gene}")

    score = []
    for j in range(number_of_genes):
        score.append((j, measure_fitness(gene[j])))
    score = sorted(score, key = lambda x: -x[1])

    best_genes = [gene[score[0][0]], gene[score[1][0]]] #자연선택된 유전자들
    fitness.append((score[0][1]/15 + score[1][1]/15)/2)
    print(f"{i+1}대 자연선택된 유전자)")
    print(f"{best_genes[0]}최종값과의 유사도 : {score[0][1]/length_of_genes}")
    print(f"{best_genes[1]}최종값과의 유사도 : {score[1][1]/length_of_genes}")
    print()

    crossover(best_genes)

for i in range(loop):
    print(f"{i+1}대 유전자의 유사도 : {fitness[i]}")

x = np.arange(1, loop+1)
y = fitness

plt.plot(x, y)
plt.show()
