#!/bin/bash/

python -m venv venv

mkdir notebook api utils getdata datasets

touch notebook/experiment.ipynb
touch api/{__init__.py,app.py}
touch utils/{__init__.py,utils.py}
touch getdata/{__init__.py,getdata.py}

# Requierements file
pip freeze > requirements.txt