import numpy as np
import random
from copy import deepcopy

def initialize_population(size,chromosomeSize):
    population = np.random.rand( *(size,4,chromosomeSize))
    for i in range(population.shape[0]):
        for j in range(population.shape[1]):
            for k in range(population.shape[2]):
                population[i,j,k]=round(population[i,j,k])
    return population

def tournamentSelection(population, fitnessValues, numberOfSelectedIndividuals=50):
    newPopulation = np.zeros((numberOfSelectedIndividuals,4,population.shape[2]))
    l = len(fitnessValues)-1
    for i in range(numberOfSelectedIndividuals):
        ind1 = random.randint(0, l)
        ind2 = random.randint(0, l)
        newPopulation[i] = deepcopy(population[ind1]
                                    if fitnessValues[ind1]>fitnessValues[ind2] else population[ind2])
    return population

def selection(population, numberOfSelectedIndividuals=50):
    population = population[0:numberOfSelectedIndividuals]
    return population

# uniform crossover + elitism
def uniformCrossover(population, populationSize,chromosomeSize):
    newPopulation = np.zeros((populationSize,4,chromosomeSize))
    newPopulation[0] = population[0]
    newPopulation[1] = population[1]

    for i in xrange(2,populationSize,1):
        father = population[random.randint(0, len(population)-1)]
        mother = population[random.randint(0, len(population)-1)]

        #Crossover
        for j in range(father.shape[0]):
            for k in range(father.shape[1]):
                newPopulation[i,j,k]= father[j,k] if random.randint(0, 1)==0 else mother[j,k]

    return newPopulation

def threeParentCrossover(population, populationSize,chromosomeSize):
    newPopulation = np.zeros((populationSize,4,chromosomeSize))
    newPopulation[0] = population[0]
    newPopulation[1] = population[1]

    for i in xrange(2,populationSize,1):
        father = population[random.randint(0, len(population)-1)]
        mother = population[random.randint(0, len(population)-1)]
        three = population[random.randint(0, len(population)-1)]

        #Crossover
        for j in range(father.shape[0]):
            for k in range(father.shape[1]):
                newPopulation[i,j,k]= mother[j,k] if father[j,k]==mother[j,k] else three[j,k]

    return newPopulation

def mutation(population, mutationPercentage=5):
    for i in range(2,len(population)):
        if (random.randint(0, 100) <= mutationPercentage):
            geneX = random.randint(0, population[0].shape[0]-1)
            geneY = random.randint(0, population[0].shape[1]-1)
            value = population[i,geneX,geneY]
            population[i,geneX,geneY] = 0 if value==1 else 1

    return population

