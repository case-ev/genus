# Example guidelines

## How to run examples
To run an example, standing at the root directory of the project simply run
```bash
python -m examples <EXAMPLE> [<POSITIONAL_ARGUMENTS>...] [<KEYWORD_ARGUMENTS>...]
```

Keyword arguments are specified by passing an argument of the form `<key>=<value>`. The type of the value must be handled and cast by the example, to avoid any errors or unexpected behaviour.

Additionally, the following flags can be passed to the example:

- `-v`, `--verbose` : Runs in verbose mode, which means any logs of level *INFO* and above are printed to stdout.
- `-d`, `--debug` : Runs in debug mode, which means any logs of level *DEBUG* and above are printed to stdout, and it might enable special debugging behaviour, depending on the example.
- `--log <LOG>` : Makes the program output all logs to the file given by `<LOG>`, overwriting if necessary.
- `-q`, `--quiet` : Disable all logging (**WARNING**: This even disables *ERROR* and *CRITICAL* level logs, which is probably not what you desire).
- `-h`, `--help` : Show the help menu.

## Adding examples
To add another example, simply create a module in the *examples* directory! There are two ways to do this:

- If it is a small example, create a *.py* file for your example, making sure to add a `main()` function that receives all necessary arguments (this function is necessary, as it acts as the starting point for the example).
- If the example is larger and requires multiple files, create a directory within *examples* and add an *\_\_init\_\_.py* file which must contain the `main()` function.

An important point to notice is that, as of currently, all arguments are passed to the `main()` function as a string. This means that it is the developer's responsability to transform them into the appropiate data type to avoid crashes or undefined behaviour (this will probably be fixed in the future for a nicer developer experience).

Setting the correct path for the examples to import the currently cloned version is automatically done by the *examples* module, so all you need to do is import *genus* as if it was installed in your system.
