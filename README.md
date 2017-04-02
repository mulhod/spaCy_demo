# ```spaCy``` + ```Cython``` demo

### Setup

- It's easy to get set up. Make sure to have a working ```conda``` and run the following from inside the repository:
    
    ```
    ./setup.sh
    ```
    
- This will create a ```conda``` environment named ```spacy``` and it will also install the packages in this repository into the environment, cythonizing/compiling the ```Cython``` extensions as needed automatically.

### ```Jupyter``` Notebooks

- The notebooks can be run by first starting the notebook server (on port 9999 or any port you want to use) from within the repository
    
    ```
    jupyter notebook --no_browser --port 9999
    ```
    
  and then navigating to ```http://localhost:9999``` in your browser and clicking on the notebook file that you want to start.

- When finished, check the notebooks that are to be shut down and click the red button to shut down the notebook sessions. Afterwards, navigate to the command-line where the server was started and press Ctrl+C twice in a row to shut down the entire server.


### ```spaCy``` demo
- [Introduction to spaCy library (link to slides)](https://docs.google.com/presentation/d/1KOvkwjZM1Wjj7hfbBP11fLrSUYJTPl_zaAM-fZje328/edit?usp=sharing)
- [Link to spaCy demo notebook](https://github.com/mulhod/spaCy_demo/blob/master/spaCy_demo_notebook.ipynb)

### Mini ```Cython``` demo
- [Link to Cython demo notebook](https://github.com/mulhod/spaCy_demo/blob/master/Cython_demo_notebook.ipynb)
