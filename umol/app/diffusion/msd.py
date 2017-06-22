"""
Compute mean square displacement
date: 06/21/2017
"""
import numpy
from numpy import ndarray


def msd(x: ndarray) -> ndarray:
    """Assume each row is for one atom"""
    N = x.shape[0]

    def aux(gap: int) -> float:
        return numpy.average(
            numpy.sum(
                numpy.square(x[gap:N, :] - x[0:N-gap, :]),
                axis=1
            )
        )
    return numpy.array([aux(i) for i in range(1, N)])
