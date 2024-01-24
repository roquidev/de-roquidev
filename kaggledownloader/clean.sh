#!/bin/bash
find . -type d -name '__pycache__' -exec rm -r {} +
echo ":::::: Python cache files removed succesfully!"