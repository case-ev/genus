# Runner

The runner is the class that *genus* creates to run training, set training parameters, etc. It contains the current population in the `x` attribute, the used pipeline, a stop criterion (of which we will talk about in [Stop criterions](#stop-criterions)), the current generation, start and update hooks (which you tipically will not use, but are useful for debugging or display reasons), and any other relevant information.

It contains three important methods:
- `start`, which is meant to be run once when starting the training, as it inializes all necessary variables and sets-up the runner for training. This method runs the `_start_hook` hook, used when creating the runner.
- `update`, which applies an iteration/generation of training, evaluating the pipeline on the current population. This method runs the `_update_hook` hook, used when creating the runner.
- `run`, which runs the `start` method once and runs `update` until the stop criterion determines that the simulation should stop.

# Stop criterions
The stop criterions, defined through the `StopCriterion` interface, are objects that implement the `should_stop` method, which takes the runner as an argument and determine whether the simulation should stop or not. You can define custom criterions if necessary, but the currently implemented ones are:
- `GenerationCriterion(gen_num)`, which stops the simulation once `gen_num` generations are trained.
- `ConvergenceCriterion(epsilon, num, max_generations: Optional)`, which stops the simulation once the current and previous fitness differ by less than `epsilon` some number of times, specified through the `num` parameter (by default 5). You can optionally pass a parameter `max_generations`, that stops the simulation if `max_generations` generations are trained, logging a warning.
