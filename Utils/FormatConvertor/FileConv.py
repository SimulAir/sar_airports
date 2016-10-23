#!/usr/bin/env python

## @mainpage File Format Convertor Documentation
#
#  @section intro_sec Introduction
#   This module implement a mechanism to convert a set of input files
#   in a set of formats  to a set of  output files in a set of formats
#
#
#  @section reference_sec Reference
#  The following format are currently supported
#  JSON: Information about this format can be found at http://json.org/
#  XML:  Information about this format can be found at https://www.w3.org/XML/
#  CSV:  Information about this format can be found at https://en.wikipedia.org/wiki/Comma-separated_values
#
#  @section synopsis_sec Synopsis
#
#
#  @section design_sec Design
#
#  @section install_sec Installation
#  in order to install this module run the following command:
#   @em "python setup.py install" @em .
#
#
#  @section license_sec License
#  Copyright 2016 @em SimulAir @em .

class FileConv(object):



    dictFormat = \
    {
           'csv'  :	'comma separeted format'
        ,  'json' :	'J'
    };
    #
    def __init__(self, infile, informat ):
        self.file = infile
        self.format = informat
        pass


    def validateInput(self):

        pass
