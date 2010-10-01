#!/usr/bin/python
import pexpect
import os
import subprocess

# testing hello world

child = pexpect.spawn ("pseudoterm %s" % os.environ["PORT"])

null = open('/dev/null', 'wb')
subprocess.call(['jam', 'reset'], stdout=null)

child.expect ('Hello world!\r\n')
print("Test successful!")
