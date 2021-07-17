# HDB resale: EDA to prediction

[![package](https://github.com/lingjie00/hdb_resale_data/actions/workflows/project-actions.yml/badge.svg)](https://github.com/lingjie00/hdb_resale_data/actions/workflows/project-actions.yml)
[![Docker](https://github.com/lingjie00/hdb_resale_data/actions/workflows/docker-actions.yml/badge.svg)](https://github.com/lingjie00/hdb_resale_data/actions/workflows/docker-actions.yml)

HDB resale data: from EDA to model prediction, for NUS Data and Social Science Club (DSS)

# Project overview

We will be training data science skills using Singapore HDB resale data.
The demonstrations here provides an example of the skills required in different data analysis steps.
There might be smarter ways to improve the things we are doing here.
Please feel free to explore new ideas and to build this project by adding suggestions to 
[issues](https://github.com/lingjie00/hdb_resale_data/issues).

Depending on the membership duration, we expect DSS members to complete the following checkpoints:

First semester
- data profiling and data cleaning techniques
- data visualisation and exploratory data analysis
- Git and GitHub

Second semester
- machine learning model: from model fitting to error analysis
- feature engineering and web scraping: extracting new features using web scraping

Third semester (TBC)
- deployment: from deploying machine learning model and dashboard to monitoring model performance
- deployment: containerized python development

Future possible plans include covering deep learning models to include unstructued data (text, image, sound) as new features.

# Notebook examples

Please refer to [notebooks](notebooks) for interactive notebook examples.

Please follow the following order:

[1. EDA - Data profiling and cleaning](notebooks/1. EDA - Data profiling and cleaning.ipynb)
[2. EDA - Data visualisation](notebooks/2. EDA - Data visualisation.ipynb)
3. Model - Data preprocessing and model fitting pipeline (WIP)
4. Model - Error analysis (WIP)
5. EDA + Model - feature engineering with web scrapped data (WIP)
6. Deployment - API (WIP)
7. Deployment - Containerlised API (WIP)

# Datasets

We will be downloading the HDB resale data using data.gov.sg APIs.
Please refer to code example for more details.

[Resale Flat Prices](https://data.gov.sg/dataset/resale-flat-prices)

# Code

[src](src) contains two kinds of codes:
1. Utilities function used in the notebook
2. End to end deployment of the model and API

Utilities function will also be used by the model deployment,
since deployment is still WIP,
we expect the code base to be slightly messy now.

# Local development

install [miniconda](https://docs.conda.io/en/latest/miniconda.html)
and create new virtual environment

create new environment, replace ```hdb_resale_data``` with the env name
```bash
conda create -n hdb_resale_data python==3.9
```

activate the new environment
```bash
conda activate hdb_resale_data
```

install essential packages and this repo package
```bash
pip install -r requirements.txt
```
