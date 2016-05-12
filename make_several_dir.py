#!/usr/bin/python

import os, sys

# Current path 
dirname = "tutorials"
path = os.getcwd() + "/"

for x in range(1,15):
	os.mkdir( path + dirname + str(x), 0o777 )


print("Path is created..")
