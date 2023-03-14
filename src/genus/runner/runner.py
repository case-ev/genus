"""
genus.runner.runner
-------------------
Code for the class that runs the training and contains the training parameters.
"""

import abc
from typing import Callable, Self

from genus_utils.logger import LOGGER

from genus.population import Population
from genus.ops.operation import Operation


class Runner:
    """Class that contains the training parameters and runs the training"""

    def __init__(
        self,
        initial_population: Population,
        pipeline: Operation,
        stop_criterion: "StopCriterion" = None,
        *,
        start_hook: Callable[[Self], None] = None,
        update_hook: Callable[[Self], None] = None,
    ) -> None:
        self.x = initial_population
        self.pipeline = pipeline
        self.stop_criterion = stop_criterion
        self.generation = 0
        self._start_hook = start_hook
        self._update_hook = update_hook

    def start(self):
        """Start the training"""
        LOGGER.info("Starting training")
        self.generation = 0
        if self._start_hook is not None:
            self._start_hook(self)

    def update(self):
        """Go to the next generation"""
        LOGGER.debug("Call to update")
        self.generation += 1
        if self._update_hook is not None:
            self._update_hook(self)
        self.x = self.pipeline(self.x)

    def run(self, *args, **kwargs):
        """Run the training"""
        try:
            self.start(*args, **kwargs)
            while not self.should_stop:
                self.update()
        except BaseException as e:
            LOGGER.error("Found error %s, safely ending training", repr(e))

    @property
    def should_stop(self) -> bool:
        """Whether the training should stop or not"""
        return self.stop_criterion.should_stop(self)


class StopCriterion(abc.ABC):
    """Trait for a class that acts as a stop criterion"""

    @abc.abstractmethod
    def should_stop(self, runner: Runner) -> bool:
        """Determine whether the training should stop or not"""


class GenerationCriterion(StopCriterion):
    """Stop when a given generation is reached"""

    def __init__(self, gen_num: int) -> None:
        self.gen_num = gen_num

    def should_stop(self, runner: Runner) -> bool:
        return runner.generation >= self.gen_num


class ConvergenceCriterion(StopCriterion):
    """Stop when the maximum fitness stops changing"""

    def __init__(self, epsilon: float, num: int = 5, max_generations: int = None) -> None:
        self.epsilon = epsilon
        self.num = num
        self.max_generations = max_generations
        self.current = 0
        self.prev_fitness = 0

    def should_stop(self, runner: Runner) -> bool:
        if runner.generation >= self.max_generations:
            LOGGER.warning("Reached maximum generations in ConvergenceCriterion")
            return True

        fitness = runner.x.max_fitness()
        if abs(fitness - self.prev_fitness) <= self.epsilon:
            self.current += 1

        if self.current >= self.num:
            return True

        self.prev_fitness = fitness
        return False
