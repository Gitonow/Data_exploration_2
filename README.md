
# Data Exploration Project - PSYC 5270

This repository contains all the files you need to analyze a dataset from CRCNS containing spike data from auditory areas in male zebra finches. The data comes from a study by Theunissen et al. titled _Single-unit recordings from two auditory areas in male zebra finches_.

## Cloning the repository

Clone the repository: `git clone https://github.com/Gitonow/Data_exploration_2.git`.

In the directory created on your computer, you will have different items:

- `README.md`: this file
- `setup.py`:  package description file.
- `requirements.txt`: a list of packages the code depends on
- `.gitignore`: a list of files git will ignore
- `src`:       a directory with the Python code
- `test`:      a directory with some test code
- `data`:      a directory where the data is located
- `build`:     a directory where processed output from the analysis will live


## Running the code

On your terminal, go in the directory created above if you are not already in it. Then, run the following command:

``` shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

Alternatively, if you're using anaconda, create a new environment and run the following to install dependencies:

``` shell
conda install git numpy scipy pandas matplotlib notebook
```
Then, in the terminal, run:
``` shell
jupyter notebook
```

Install the project in development mode by running `python setup.py develop`. If you use notebooks, this will ensure that you can access your modules.

You can run the .ipynb file in the `src` folder.
