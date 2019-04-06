
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


## Set up to prevent errors (first time only)

On your terminal, go in the directory created above if you are not already in it. Then, run the following command:

``` shell
jupyter notebook --generate-config
```

This command will generate a configuration file that you can customize to prevent some errors related to the loading of the data that Python can encounter. After executing this command, the terminal will print a message starting with 

``` shell
Writing default config to:
```

Go to that directory (which may be invisible in certain OS) and open the file `jupyter_notebook_config.py`. Search for `c.NotebookApp.iopub_data_rate_limit`. After finding this line, change the value to `c.NotebookApp.iopub_data_rate_limit = 10000000` and comment out the line, i.e. remove the `#` symbol. Save the file. After that, run in the terminal the following command:

``` shell
jupyter notebook
```

Everything should work fine! Now, when you want to execute the code again, you just have to follow the instructions of the next section.

## Run the code

On your terminal, go in the directory created in the first section if you are not already in it. Then, run the following command:

``` shell
jupyter notebook
```
In your browser, go in the `src` folder and run  `project.ipynb` .
