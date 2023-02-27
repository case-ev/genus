# Chromomes and populations

All the genetic information of an organism is contained within chromosomes, which are instances of the `Chromosome` class. These chromosomes store genetic code in a numpy array of `uint8` types which contain zeros and ones[^1], representing the genome as a binary code.


[^1]: This is memory inneficient, as you are using 8 bits for what could be stored in just 1, but as a first implementation it works and hasn't given me any trouble. In the future, to allow solving bigger problems where memory might be an issue, this is going to be optimized (which should allow for more memory efficiency as well as lower runtimes).
