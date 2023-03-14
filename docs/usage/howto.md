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
4. Create a `Runner`, which you can initialize with the defined pipeline and initial population, and in which you can specify a stop criterion that the runner uses to decide when to stop the training.
5. Run the training and use your results! The last obtained population is contained in the `x` attribute in the runner.

Alternatively, you can manually run each iteration if you need a lower level interface to the training. Also consider that the runner can take an **start hook** and an **update hook**, which are functions that take the runner instance as an input and return nothing: these can be used for any special functionality that you need to add (e.g adding a progress bar to show the progress of the training. For an example of this see the *maximimize_ones* example).

It is important to consider that most operations have hyperparameters that must be passed, which have a great influence on whether the implemented solution works or not. It is up to the user to pass the correct hyperparameters.

Another important aspect to consider is that the given pipeline is only a recommendation: more operations can be included in the pipeline, the order of operations can be changed, and custom operations can be defined, depending on the problem and your proposed solution. *genus* only gives you the tools: it is up to you to use them properly :)
