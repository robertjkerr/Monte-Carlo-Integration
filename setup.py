from distutils.core import setup, Extension

module = Extension("mctoolsMethods", sources = ["mctools/c/_mctools.c", "mctools/c/_functions.c", "mctools/c/src/scatter.c", 
                                                "mctools/c/src/tools.c", "mctools/c/src/allocate.c"])

setup(name = "mctoolsScatter",
        version = "0.0.1",
        description = "C methods for robertjkerr/Monte-Carlo-Math-Tools",
        ext_modules=[module])