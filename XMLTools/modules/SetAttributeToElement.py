#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
AUTHOR: 
    Emanuel Valero - Provita

LATEST UPDATE:
    2019-12-10
"""

import os, sys
import xml.etree.ElementTree as ET

def setAttribute(filename, parent, nodename, attribute, value ):

    # Define structure of input and output directories
    inputDir  = '../inputs/'
    outputDir = 'outputs/'

    # Import .xml file and get root of the tree

    typefile = type( filename )

    try:
        if typefile is str and filename.count('\n') is 0:
            tree = ET.parse(inputDir + filename)
                
        elif 'xml.etree.ElementTree' in str( typefile ):
            tree = filename

        parent = tree.findall( './/' + parent + '/' + nodename)
        itemscount = len(parent)

        for child in parent:
            child.set('completed', 'yes')

    
    except:
        print('ERROR: Invalid filename')
  

"""
Implementation
"""


xmlfile = 'DT00/dummy.xml'
setAttribute(xmlfile, 'catalog', 'book', 'completed', 'yes')
