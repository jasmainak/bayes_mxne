#! /usr/bin/env python
import os
import setuptools  # noqa; we are using a setuptools namespace
from numpy.distutils.core import setup

# get the version (don't import bayes_mxne here to avoid dependency)
version = None
with open(os.path.join('bayes_mxne', '__init__.py'), 'r') as fid:
    for line in (line.strip() for line in fid):
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip('\'')
            break
if version is None:
    raise RuntimeError('Could not determine version')

descr = """Mixed-norms and Hierarchical Bayesian models for the M/EEG inverse problem"""

DISTNAME = 'bayes_mxne'
DESCRIPTION = descr
MAINTAINER = 'Yousra Bekhti'
MAINTAINER_EMAIL = 'yousra.bekhti@gmail.com'
LICENSE = 'BSD (3-clause)'
DOWNLOAD_URL = 'https://github.com/agramfort/bayes_mxne'
VERSION = version

if __name__ == "__main__":
    setup(name=DISTNAME,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          license=LICENSE,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          long_description=open('README.rst').read(),
          classifiers=[
              'Intended Audience :: Science/Research',
              'Intended Audience :: Developers',
              'License :: OSI Approved',
              'Programming Language :: Python',
              'Topic :: Software Development',
              'Topic :: Scientific/Engineering',
              'Operating System :: Microsoft :: Windows',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS',
          ],
          platforms='any',
          packages=[
              'bayes_mxne'
          ],
          )
