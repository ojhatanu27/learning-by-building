#package is a third party library that e can install and gain access to it
#PyPI - python package index is a website where we can download and install all sort of packages
#cowsay - package in python
#pip - programme is a paclage manager that allows to doenload package by running command
import cowsay
import sys
if len(sys.argv)==2:
    cowsay.cow("Hello,"+sys.argv[1])
    cowsay.trex("Hello,"+sys.argv[1])

