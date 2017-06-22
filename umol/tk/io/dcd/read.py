"""
Read a DCD trajectory file
"""
import prody
import numpy
from numpy import ndarray


def read(pdb: str, dcds: list, selection="all") -> ndarray:
    if len(dcds) == 0:
        return numpy.array([])
    else:
        topo = prody.parsePDB(pdb)
        traj = prody.Trajectory(dcds[0])
        for f in dcds[1:]:
            traj.addFile(f)
        traj.link(topo)
        traj.setAtoms(topo.select(selection))
        return traj.getCoordsets()
