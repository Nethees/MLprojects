from setuptools import find_packages,setup
from typing import List

e_hyphen = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if e_hyphen in requirements:
            requirements.remove(e_hyphen)
    return requirements

setup(
name = 'mlproject',
version = '0.0.1',
author = 'Netheeswaran',
author_email = 'netheeswaran.arunachalam@ucdconnect.ie',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')

)