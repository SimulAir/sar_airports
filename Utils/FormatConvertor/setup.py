# see http://software-carpentry.codesourcery.com/entries/build/Distutils/Distutils.html for more information about this file
from distutils.core import setup
import distutils.sysconfig as s

setup (
    name = "FormatConvertor",
    version = "0.0.1",
    description = "FormatConvertor - a module allowing the conversion of data file format",
    author = "Karl Butz",
    author_email = "Karlvbutz@gmail.com",
    url = "",
	data_files = [],
	py_modules = ['FileConv']
    )
