# setup-arcpy-for-virtualenv

> Set up ArcGIS Pro's arcpy module for use inside Python virtual environments.

## Description

Running this script will allow arcpy to be imported from any virtualenv created
from the Python 3 executable included with ArcGIS Pro. This is accomplished by
making copies of arcpy dependances and placing them in `"C:\arcpy"`. Then a
`sitecustomize.py` file is placed into the ArcGIS Python's `site-packages`.

This script only needs to be run once. After running the script, all new
virtualenvs will be able to import arcpy, without any additional steps.

## Usage

`python run.py "C:\path\to\your\ArcGIS\Pro"`

## Paramaters

+ "C:\path\to\your\ArcGIS\Pro"
  - Give the full path down to the \Pro directory. The script will
    figure out the rest
