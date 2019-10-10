from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys


setup(name='mccabe_group',
      version='0.1',
      description='',
      author='McCabe Group',
      author_email='timothy.c.moore@vanderbilt.edu',
      license='MIT',
      packages=['mccabe_group'],
      zip_safe=False,
      #test_suite='tests',
      #cmdclass={'test': PyTest},
      #extras_require={'utils': ['pytest']},
)
