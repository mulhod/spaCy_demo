from os.path import join
from subprocess import getoutput
from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

cmdclass = {}

# Hackish way of doing this. Find better way...
root_env = getoutput('conda info | grep "package cache :"'
                     ' | awk \'{print $4}\'')
python_header_dir = join(root_env, 'python-3.4.3-2/include/python3.4m')

ext_modules = [Extension('awesome_hello_world.hello',
                         ['awesome_hello_world/hello.pyx'],
                         include_dirs=[python_header_dir])]
cmdclass.update({'build_ext': build_ext})

setup(name = 'spaCy and Cython demo',
      description='Repository storing spaCy demo + mini-Cython demo.',
      url='https://github.com/mulhod/spaCy_demo',
      long_description=readme(),
      author='Matt Mulholland',
      author_email='mulhodm@gmail.com',
      packages=['awesome_hello_world'],
      cmdclass=cmdclass,
      ext_modules=ext_modules,
      keywords='spacy cython',
      classifiers=['Intended Audience :: Science/Research',
                   'Intended Audience :: Developers',
                   'License :: MIT',
                   'Programming Language :: Python :: 3.4',
                   'Topic :: Scientific/Engineering',
                   'Operating System :: POSIX',
                   'Operating System :: Unix',
                   'Operating System :: MacOS'],
      zip_safe=True)
