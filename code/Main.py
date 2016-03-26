import GeneticAlgorithm as GA
import Fitness
import Ordenation
import Graphic

time = 720
chromosomeSize = time/10
generations = 50
mutationPercentage = 40
populationSize = 20
numberOfSelectedIndividuals = 12
pltBestFitness = []
pltFitnessAverage = []

# Main
population = GA.initialize_population(populationSize,chromosomeSize)
for i in range(generations):
    print "Generation: "+ str(i)
    fitnessvalues = Fitness.fitness(population,time)
    fitnessvalues,population = Ordenation.selectionsort(fitnessvalues,population)
    print "     Best fitness: "+str(fitnessvalues[0])
    print "     Fitness average: "+str(sum(fitnessvalues)/len(fitnessvalues))
    pltBestFitness.append(fitnessvalues[0])
    pltFitnessAverage.append(sum(fitnessvalues)/len(fitnessvalues))
    population = GA.selection(population, numberOfSelectedIndividuals)
    population = GA.uniformCrossover(population, populationSize, chromosomeSize)
    population = GA.mutation(population, mutationPercentage)

Graphic.printGraphic(pltBestFitness,pltFitnessAverage,generations)