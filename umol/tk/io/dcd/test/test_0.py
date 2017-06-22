import umol.sample_data as sample
import os
from umol.tk.io import dcd

def test():
    pdb = sample.path("mdm2.pdb")
    dcds = [
        sample.path("mdm2.dcd"),
    ]
    assert os.path.exists(pdb)
    for f in dcds:
        assert os.path.exists(f)

    coords = dcd.read(pdb, dcds, selection="name CA")
    print(coords.shape)
    assert coords.shape == (500, 85, 3)

    coords = dcd.read(pdb, dcds, selection="name CB")
    print(coords.shape)
    assert coords.shape == (500, 81, 3)
