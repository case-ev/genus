# Genetic operations

Genetic operations are those that modify the genetic content inside of a chromosome. The currently implemented genetic operations are:

- **Crossover**: The crossover operation tries to mix the genetic material of existing chromosomes to create better offspring. The way parents are chosen is based on fitness: a probability function is given, which uses the fitness of each chromosome to associate its probability to be chosen for reproduction, such that stronger individuals have a higher probability. This choosing is done with replacement, meaning that one chromosome can reproduce many times in a single crossover operation: this even allows for asexual reproduction, where a chromosome mates with itself to create offspring that will be exactly equal to the parent (save for mutations).
    - `TwoParentCrossover`: Takes the genetic material of two parents and does a crossover at a random point with some probability (tipically 1). This leads to two offspring per mating.

- **Mutation**: Mutation is a mechanism that allows populations to explore the entire search space of a problem, thus avoiding local maxima and allowing them to find the true global maximum. It works by modifying the genetic material of a chromosome with some small probability, leading to offspring that can have genetic material that is slightly different than their parents'. Together with the other operations, this can lead to better solutions.
    - `BinaryMutation`: Assumes the genetic material is composed of ones and zeros, so there is a small chance that one bit in the code is flipped.

- **Selection**: Selection is a mechanism through which strong parents can pass straight to the next generation. This can allow, for example, for a generation to be composed of chromosomes with a really high fitness together with their offspring.
    - `ElitismSelection`: The best \\(n\\) chromosomes pass to the next generation while the rest are discarded, where \\(n\\) is a hyperparameter of the problem.
