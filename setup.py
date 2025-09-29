from setuptools import find_packages, setup
from typing import List

HYPEN_DOT_E = '-e .'

def get_requirement(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n", "") for req in requirement]
        
        if HYPEN_DOT_E in requirement:
            requirement.remove(HYPEN_DOT_E)

    return requirement

setup(
    name='mlproject',
    version='0.0.1',
    author='gaurav',
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')
)
