"""
Return a dict of mapping of 
string name to actual app's main function
date: 06/21/2017
"""
from . import diffusion


def catalog():
    return {
        "diffusion": diffusion.main,
    }
