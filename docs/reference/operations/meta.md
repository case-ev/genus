# Meta operations

Meta operations are those whose purpose is to call other operations. The currently implemented ones are:

- `Sequential`: Sequentally calls the given operations, using the output of one operation as the input to the next. This allows for the formation of pipelines of operations, which give rise to complex training sequences.
- `Parallel`: Runs many operations in parallel, returning the result in a list of populations. This creates a divergence and thus must be resolved using some operation that acts on a list of populations instead of a single one. This operation **does not guarantee** that the order of the results matches the ordering of the inputs, as it uses multithreading to speed up execution.
- `ParallelOrdered`: Runs many operations in parallel, returning the result in a list of populations. This creates a divergence and thus must be resolved using some operation that acts on a list of populations instead of a single one. Unlike `Parallel`, this does guarantee that the results are in the same order as the given operations, risking a **potentially** slightly slower execution.
- `ForEach`: Takes any operation and iteratively applies it to each element of the input. For this reason, the input to this function has to be an object you can iterate over
