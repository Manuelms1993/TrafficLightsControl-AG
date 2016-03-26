import matplotlib.pyplot as plt

def printGraphic(pltBestFitness, pltFitnessAverage, generations):
    plt.figure(num=None, figsize=(20, 10), dpi=60, facecolor='w', edgecolor='k')
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    plt.title("Fitness Evolution")
    plt.plot(pltBestFitness,'r-',label='Best Fitness',linewidth=2.0)
    plt.plot(pltFitnessAverage,'b-',label='Fitness Average',linewidth=2.0)
    plt.legend(loc="lower left")
    plt.show()
