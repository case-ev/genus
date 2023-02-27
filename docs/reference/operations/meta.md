# Meta operations

Meta operations are those whose purpose is to call other operations. The currently implemented ones are:

- `Sequential`: Sequentally calls the given operations, using the output of one operation as the input to the next. This allows for the formation of pipelines of operations, which give rise to complex training sequences.
- `Parallel`: Runs many operations in parallel, returning the result in a list of populations. This creates a divergence and thus must be resolved using some operation that acts on a list of populations instead of a single one.
