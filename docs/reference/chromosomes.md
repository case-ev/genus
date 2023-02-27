# Chromomes and populations

All the genetic information of an organism is contained within chromosomes, which are instances of the `Chromosome` class. These chromosomes store genetic code in a numpy array of `uint8` types which contain zeros and ones[^1], representing the genome as a binary code.

## Operators on chromosomes

There are the `concatenate` and `split` functions that can be applied directly on chromosomes, which allow for mixing and splitting of chromosomes, respectively. These act as operators on chromosomes, and they are the base of some of the more complex operators that are described later.

## Populations

In *genus* there exists the concept of a population, modelled by the `Population` class, which is just a group of chromosomes that are related in some way. Most complex operators act on these populations, as they usually represent chromosomes which belong to the same generation during training.

Populations also contain a fitness function \\(F: \mathcal{C}\rightarrow\mathbb{R}\\), such that \\(F(c), c\in\mathcal{C}\\) indicates how fit a chromosome \\(c\\) is, where \\(\mathcal{C}\\) is the space of all possible chromosomes. This fitness function is then used by the algorithm, by making it so that those organisms which are stronger (meaning they map to a higher value through the fitness function) are more likely to produce offspring or go straight trough to the next generation than those who are weaker. After some number of generations, this ensures that the population is composed mostly of those individuals who are stronger, leading to better solutions to the proposed problem.

These populations can also be joined using the `join()` function, which simply takes the chromosomes from all the given populations and groups them together into a new one. This function can take a `fitness` argument, which would represent the fitness function that the new population should have: if no fitness function is given, it will simply take the fitness function from the first given population.

## Notes on operators
The operators `concatenate()`, `split()`, `join()`, and any others that could be created in the future, can be called as both functions or methods of some instance. For each one of these operators, the homonymous method simply acts as an alias, passing `self` as the first parameter to the operator and the other arguments as the rest of the parameters.

---

[^1]: This is memory inneficient, as you are using 8 bits for what could be stored in just 1, but as a first implementation it works and hasn't given me any trouble. In the future, to allow solving bigger problems where memory might be an issue, this is going to be optimized (which should allow for more memory efficiency as well as lower runtimes).
