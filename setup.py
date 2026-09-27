"""  
In Python and Machine Learning (ML) projects, setup.py is a build script 
used to manage dependencies, define metadata, and package code 
so that it can be easily shared or installed across different environments
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