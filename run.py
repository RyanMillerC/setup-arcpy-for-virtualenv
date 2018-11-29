"""
Set up arcpy for use inside Python virtual environments. This will
allow arcpy to be imported from any virtualenv created from the Python
included with ArcGIS Pro.

Usage: python run.py "C:\path\to\your\ArcGIS\Pro"

Paramaters: "C:\path\to\your\ArcGIS\Pro"
  - Give the full path down to the \Pro directory. The script will
    figure out the rest
"""

import sys

from shutil import copyfile, copytree


REQUIRED_PACKAGES = [
    'dateutil',
    'numpy'
]

REQUIRED_MODULES = [
    'ArcGISPro.pth',
    'arcgisscripting.pyd',
    'arcpy_wmx.pyd',
    'gapy.pyd',
    'six.py'
]


def main(pro_dir):
    print(r'Copying required packages to "C:\arcpy"...')
    for package in REQUIRED_PACKAGES:
        print('{}...'.format(package))
        copytree(
            r'{}\bin\Python\envs\arcgispro-py3\Lib\site-packages\{}'.format(
                pro_dir,
                package
            ),
            r'C:\arcpy\{}'.format(package)
        )
    print(r'Copying required modules to "C:\arcpy"...')
    for module in REQUIRED_MODULES:
        print('{}...'.format(module))
        copyfile(
            r'{}\bin\Python\envs\arcgispro-py3\Lib\site-packages\{}'.format(
                pro_dir,
                module
            ),
            r'C:\arcpy\{}'.format(module)
        )
    print(r'Injecting sitecustomize.py into ArcGIS Pro...')
    copyfile(
        r'lib\sitecustomize.py',
        r'{}\bin\Python\envs\arcgispro-py3\Lib\sitecustomize.py'.format(
            pro_dir
        )
    )
    print('Done!')


if (len(sys.argv) > 1):
    main(sys.argv[1])
else:
    print(r'Usage: python run.py "C:\path\to\your\ArcGIS\Pro"')
