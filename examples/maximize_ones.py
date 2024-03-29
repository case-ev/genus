"""
exmples.maximize_ones
---------------------
Example to show a program that maximizes the number of ones in a string
using genetic algorithms.
"""

from timeit import default_timer as timer

from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np

from genus_utils.logger import LOGGER
import genus


plt.style.use("tableau-colorblind10")


# Counts the number of ones
def _fitness(c: genus.Chromosome) -> float:
    return (c.code == 1).sum()


class _Diagnostic:
    def __init__(self) -> None:
        self.dict = {}

    def _get_times(self, _type):
        if (t := self.dict.get(_type)) is not None:
            return t
        return []

    def _append(self, val, _type):
        if (d := self.dict.get(_type)) is not None:
            d.append(val)
        else:
            self.dict[_type] = [val]

    def add_time(self, x, op):
        """Add the time of the operation"""
        start = timer()
        val = op(x)
        end = timer()
        delta = end - start
        self._append(delta, type(op).__name__)
        return val


def main(
    members=100,
    elitism_size=10,
    chrom_size=20,
    one_prob=0.5,
    cross_num=1,
    cross_prob=1,
    mut_prob=0.001,
    generations=200,
    criterion="random_binary",
    diagnostic=False,
    display=False,
):
    """Maximize the number of ones in a string"""
    LOGGER.info("Parsing input arguments")
    members = int(members)
    elitism_size = int(elitism_size)
    chrom_size = int(chrom_size)
    one_prob = float(one_prob)
    cross_num = int(cross_num)
    cross_prob = float(cross_prob)
    mut_prob = float(mut_prob)
    generations = int(generations)

    LOGGER.info("Creating pipeline")
    _diagnostic = _Diagnostic()
    pipeline = genus.ops.Sequential(
        genus.ops.Parallel(
            genus.ops.ElitismSelection(elitism_size),
            genus.ops.TwoParentCrossover(members - elitism_size, cross_num, cross_prob),
            _update_function=_diagnostic.add_time,
        ),
        genus.ops.Join(),
        genus.ops.BinaryMutation(mut_prob),
        _update_function=_diagnostic.add_time,
    )

    LOGGER.info("Creating progress bar")
    prog_bar = tqdm(desc="Optimizing", total=generations, unit="gen")

    def _prog_bar_hook(runner):
        best = runner.x.max_member()
        ratio = _fitness(best) / len(best)
        prog_bar.update()
        prog_bar.set_description(
            f"Optimizing, current best is {100 * ratio:6.2f}% \
{str(best) * display}"
        )

    LOGGER.info("Creating runner")
    runner = genus.Runner(
        genus.Population.from_num(
            members,
            chrom_size,
            _fitness,
            criterion=criterion,
            criterion_kwargs={"p": one_prob},
        ),
        pipeline,
        genus.GenerationCriterion(generations),
        update_hook=_prog_bar_hook,
    )
    LOGGER.info("Running the training")
    runner.run()
    LOGGER.info("Finished training")

    best = runner.x.max_member()
    ratio = _fitness(best) / len(best)
    print(f"Best chromosome {100 * ratio:6.2f}% {str(best) * display}")

    if diagnostic:
        print("\nDiagnostic")
        print("==========")
        for op, times in _diagnostic.dict.items():
            if op not in ["Parallel", "Join"]:
                fig, ax = plt.subplots()
                fig.suptitle(op)
                ax.set_xlabel("Generations")
                ax.set_ylabel("Time")

                x = np.arange(len(times))
                result_avg = []
                result_var = []
                std_p = []
                std_m = []
                moving_avg = 0
                moving_var = 0
                for i, t in enumerate(times):
                    moving_avg = t / (i + 1) + i / (i + 1) * moving_avg
                    moving_var = (t - moving_avg) ** 2 / (i + 1) + i / (
                        i + 1
                    ) * moving_var
                    result_avg.append(moving_avg)
                    result_var.append(moving_var)
                    std_p.append(moving_avg + np.sqrt(moving_var))
                    std_m.append(moving_avg - np.sqrt(moving_var))

                print(
                    f"+ {op:20} -> Total {1000 * sum(times):12.4f}ms | Per generation \
{1000 * moving_avg:8.4f} \u00b1 {1000 * np.sqrt(moving_var):.4f}ms"
                )
                ax.scatter(x, times, label="raw", alpha=0.5)
                ax.plot(x, result_avg, label="\u03bc")
                ax.fill_between(
                    x, std_m, std_p, alpha=0.25, color="#555", label="\u03c3"
                )
            ax.legend()

        plt.show()
