#!/bin/zsh

# Usage: ./setup.sh

set -eu

ORIG_DIR=$(pwd)
THIS_DIR=$(dirname $(readlink -f $0))
cd ${THIS_DIR}

echo "Make sure that conda (miniconda) is installed before trying to set up" \
     "or else this script will fail...\n"

echo "Creating conda environment...\n"
# Not sure if this is necessary
conda config --add channels pypi
conda config --add channels https://conda.anaconda.org/spacy
# Create environment first and force python=3.4 (for some reason, just
# adding python=3.4 to the list of packages in conda_requirements.txt
# does not work as it is not recognized as a valid package name)
conda create --yes -n spacy python=3.4
# And now install all of the packages we need
source activate spacy
# Install cymem separately and without specifying a version number since
# there's some issue with specifying the correct package version
conda install cymem
conda install --yes --file conda_reqs.txt
if [[ $? -gt 0 ]]; then
    
    echo "\"conda install --yes --file conda_reqs.txt\" failed. Exiting.\n"
    cd ${ORIG_DIR}
    exit 1
    
fi
echo "Created \"spacy\" environment successfully! To use environment, run" \
     "\"source activate spacy\". To get out of the environment, run" \
     "\"source deactivate\".\n"

echo "Installing some extra packages with pip (since conda does not seem to" \
     "want to install them)...\n"
pip install pudb
if [[ $? -gt 0 ]]; then
    
    echo "pip installation of pudb failed. Exiting.\n"
    cd ${ORIG_DIR}
    exit 1
    
fi

# Download model data for spaCy
echo "Downloading model data for spaCy package...\n"
python3.4 -m spacy.en.download all

# Compile Cython modules
echo "Compiling Cython extensions...\n"
python3.4 setup.py develop
echo "Package installed!"
echo "If changes are made to the Cython extensions, run the following to" \
     "re-compile the extensions for use in the various command-line" \
     "utilities:\n\tpython setup.py build_ext\n\nOr run the following to" \
     "reinstall the entire package:\n\tpython setup.py install\n\nOr run" \
     "the following to reinstall the entire package in the current" \
     "location, i.e., in development mode:\n\tpython setup.py develop\n"

echo "Setup complete. Use \"source activate spacy\" to activate conda" \
     "environment.\n"
