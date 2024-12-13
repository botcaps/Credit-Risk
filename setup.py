from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'  # Marker used in requirements.txt for editable installations

# This function reads a requirements file and returns a list of dependencies.
def get_requirement(file_path: str) -> List[str]:
    requirements = []  # Initialize an empty list to store requirements
    with open(file_path) as file_obj:  # Open the requirements file
        requirements = file_obj.readlines()  # Read all lines from the file
        # Remove newline characters from each requirement
        requirements = [req.replace("\n", "") for req in requirements]
        # Remove '-e .' if present, as it is specific to editable installations
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

# Configure the package setup
setup(
    name='credit risk',  # Name of the package
    version='0.0.1',  # Version of the package
    author='Abhishek',  # Author's name
    authoremail='abhishek.7979033@gmail.com',  # Author's email address
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=get_requirement('requirements.txt')  # Install dependencies listed in the requirements file
)
