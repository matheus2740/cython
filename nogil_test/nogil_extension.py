from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        'nogil_extension',
        ['nogil_extension.pyx'],
    )
]

setup(
    ext_modules = cythonize(ext_modules)
)
