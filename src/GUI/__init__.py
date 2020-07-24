from os import listdir
from os.path import dirname, realpath

path = dirname(realpath(__file__))
__all__ = [f[:-3] for f in listdir(path) if f.endswith(".py") and not "__" in f]
