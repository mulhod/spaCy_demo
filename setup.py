from os.path import join
from subprocess import getoutput
from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

# Hackish way of doing this. Find better way...
root_env = getoutput('conda info | grep "package cache :"'
                     ' | awk \'{print $4}\'')
python_header_dir = join(root_env, 'python-3.4.3-2/include/python3.4m')

setup(name = 'spaCy and Cython demo',
      description='Repository storing spaCy demo + mini-Cython demo.',
      url='https://github.com/mulhod/spaCy_demo',
      author='Matt Mulholland',
      author_email='mulhodm@gmail.com',
      packages=['awesome_cython_stuff', 'regular_old_yet_fine_python_stuff'],
      cmdclass={'build_ext': build_ext},
      ext_modules=[Extension('awesome_cython_stuff.hello',
                             ['awesome_cython_stuff/hello.pyx'],
                             include_dirs=[python_header_dir]),
                   Extension('awesome_cython_stuff.great_circle',
                             ['awesome_cython_stuff/great_circle.pyx'],
                             include_dirs=[python_header_dir])],
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
