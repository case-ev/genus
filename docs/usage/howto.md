# Usage guidelines

In this section, a brief overview of how *genus* can be used to solve optimization problems is given. For a more complex understanding read the full documentation.

## General idea
The general process of implementing a solution in *genus* is:

1. Define a fitness function.
2. Create the initial population which contains the fitness function.
3. Create the pipeline to use for the problem. A good example of a pipeline that should work for most problems can be found in the `maximize_ones` example, which consists of a `Sequential` operation that contains:
    - `ElitismSelection` and `TwoParentCrossover` done in parallel, with sizes that preserve the original size of the population.
    - `Join` to resolve the divergence created by `Parallel` by joining both populations.
    - `BinaryMutation` to introduce randomness and allow finding the global maximum.
4. Iterate as many times as necessary, passing the current population into the pipeline and setting the result of the operation as the current population.

It is important to consider that most operations have hyperparameters that must be passed, which have a great influence on whether the implemented solution works or not. It is up to the user to pass the correct hyperparameters.

Another important aspect to consider is that the given pipeline is only a recommendation: more operations can be included in the pipeline, the order of operations can be changed, and custom operations can be defined, depending on the problem and your proposed solution. *genus* only gives you the tools: it is up to you to use them properly :)
