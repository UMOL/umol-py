from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='umol',
    version="0.1.0",
    description="umol: molecular data analytics suite",
    long_description=long_description,
    url="https://github.com/UMOL/umol-py.git",
    author="Steven(Yuhang) Wang",
    license="MIT/X11",
    packages=find_packages(),
    entry_points={
            'console_scripts': [
                    'plot = umol.main:main'
                ],
        },
    install_requires=[
            "typing",
            "numpy",
            "prody",
            "yaml"
        ],
    )
