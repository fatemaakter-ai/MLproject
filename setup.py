from setuptools import find_packages,setup
from typing import List

def get_requirments(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    HYPHEN_DOT='-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_DOT in requirements:
            requirements.remove(HYPHEN_DOT)

    return requirements        


setup(
    name='mlprojects',
    version='0.0.1',
    author='Fatema',
    author_email='ifatema170.gmail.com',
    install_requires=get_requirments('requirements.txt')
)