from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

sourcefiles = ["rir_generator.c", "rirgenerator.pyx"]
ext_modules = [Extension(
	"rirgenerator", sourcefiles,
	libraries=['m'],
	include_dirs=[np.get_include()]
)]

setup(
	name = 'RIRGenerator',
	cmdclass = {'build_ext': build_ext},
	ext_modules = ext_modules
)
