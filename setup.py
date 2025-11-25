#setup.py
from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
        This function return list of strings
    """
    requirements_list:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            # read lines from the files
            lines = file.readlines()
            # process each line
            for line in lines:
                requirement = line.strip()
                # ignoring empty lines and -e .
                if requirement and requirement != "-e .":
                    requirements_list.append(requirement)
    

    except FileNotFoundError:
        print("requirements.txt File is not found")

    return requirements_list

setup(
        name="NetworkSecurity",
        version="0.1",
        author="Narender Singh Yadav",
        author_email="narenyadav0929@gmail.com",
        packages=find_packages(),
        install_requires=get_requirements()

            )