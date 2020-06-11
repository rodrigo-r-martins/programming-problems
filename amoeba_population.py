'''
A population of amoebas starts with 1. After a single period, assume the amoeba can divide into 1, 2, 3, or 0 (it can die) with equal probability. What is the probability that the entire population dies out eventually?
'''
# After researching because I couldn't make it, I found the following source, so I used it as a reference: 
# https://goldenratiphi.wordpress.com/2013/02/02/amoeba-generation-and-branching-processes/
# It gives a code simulation but I just had to change a few lines of code to make it match with the question.

import random
 
class CreateAmoeba:
    growth_rate = [0,1,2,3]   # set the outcomes here, each of them will be identically distributed
    
    def regeneration(self, random_rate):
        return self.growth_rate[random_rate]
 

SAMPLESIZE = 1000             # number of colonies to test
sample = 0

for k in range(SAMPLESIZE):
    amoeba_population = [[CreateAmoeba()]]
    population = 1
    states = len(amoeba_population[0][0].growth_rate)-1
    
    while (population != 0 and population < 1000):
        amoeba_population.append([])
        for j in amoeba_population[-2]:
            random_rate = random.randint(0, states)
            offspring = j.regeneration(random_rate)
            for k in range(offspring):
                amoeba_population[-1].append(CreateAmoeba())
 
        population = len(amoeba_population[-1])
        # print(f"population = {population}")
        if population == 0:
            sample += 1
 
print(f"The probability of extinction is {(sample/SAMPLESIZE)*100:.2f}%")