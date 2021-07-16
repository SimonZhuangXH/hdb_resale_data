# HDB resale: EDA to prediction

[![package](https://github.com/lingjie00/hdb_resale_data/actions/workflows/project-actions.yml/badge.svg)](https://github.com/lingjie00/hdb_resale_data/actions/workflows/project-actions.yml)
[![Docker](https://github.com/lingjie00/hdb_resale_data/actions/workflows/docker-actions.yml/badge.svg)](https://github.com/lingjie00/hdb_resale_data/actions/workflows/docker-actions.yml)

HDB resale data: from EDA to model prediction, for NUS Data and Social Science Club

# Project overview

We will be demonstrating basic exploratory data analysis and model prediction using Singapore HDB resale data.

# Notebook examples

Please refer to /notebooks for interactive notebook examples.

# Datasets

We will be downloading the HDB resale data using data.gov.sg APIs.
Please refer to code example for more details.

# Code

Please refer to /src for code examples.

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


# Reprodue code

Please include requirements.txt
```python
conda list --export > requirements.txt
```

