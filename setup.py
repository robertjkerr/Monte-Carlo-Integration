from distutils.core import setup, Extension

module = Extension("mctoolsScatter", sources = ["mctools/c/_mctools.c", "mctools/c/src/scatter.c", "mctools/c/src/tools.c"])

setup(name = "mctoolsScatter",
        version = "0.0.1",
        description = "Scatter tools for robertjkerr/mctools",
        ext_modules=[module])