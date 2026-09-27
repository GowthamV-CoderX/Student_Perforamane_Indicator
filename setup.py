"""  
In Python and Machine Learning (ML) projects, setup.py is a build script 
used to manage dependencies, define metadata, and package code 
so that it can be easily shared or installed across different environments
"""

""" 
The relation between setup.py and the command pip install -e . is that setup.py provides the configuration and 
metadata that pip uses to install your local package in "editable" development mode. When you execute pip install -e .,
the -e flag stands for editable (or development mode), 
and the dot (.) tells pip to look for a package configuration file—traditionally setup.py—in the current working directory.
How They Work Together
Instead of copying your code to a global site-packages directory, running pip install -e . 
creates a link (a .egg-link file or a developer path pointer) back to your local project directory.
• The Role of setup.py: It defines your package's name, version, external dependencies (install_requires), and structural layouts.
• The Role of pip install -e .: It reads setup.py to figure out what dependencies to download, but links your own source code dynamically
"""
from setuptools import find_packages,setup

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
setup(
    name = "Student_Performance_Indicator an End to End ML Project.",
    version = '0.0.1',
    author='Gowtham',
    author_email='gowthamvudumu007@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)