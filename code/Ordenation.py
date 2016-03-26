from copy import deepcopy
def selectionsort(fitnessValues,population):

    tam = len(fitnessValues)
    for i in range(0,tam-1):
        max=i
        for j in range(i+1,tam):
            if fitnessValues[max] < fitnessValues[j]:
                max=j

        aux = fitnessValues[max]
        fitnessValues[max] = fitnessValues[i]
        fitnessValues[i] = aux

        aux2 = deepcopy(population[max])
        population[max] = deepcopy(population[i])
        population[i] = deepcopy(aux2)

    return fitnessValues,population
