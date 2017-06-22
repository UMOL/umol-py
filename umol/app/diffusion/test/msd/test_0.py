from umol.app.diffusion.msd import msd
import numpy


def test():
    coords = numpy.array(
        [
         [1.0, 0, 0],
         [0, 1.0, 0],
         [0, 0, 1.0],
        ]
    )
    answer = msd(coords)
    print("answer.shape =", answer.shape)
    solution = numpy.array([2.0, 2.0])
    assert (answer == solution).all()
