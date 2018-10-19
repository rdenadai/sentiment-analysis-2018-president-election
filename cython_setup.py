from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

setup(
    ext_modules=cythonize("src/ai/unsupervised/emotional_lsa_utils.pyx"),
    include_dirs=[numpy.get_include()]
)