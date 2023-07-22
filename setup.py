from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements() -> List[str]:
    """
    this function will return the list of requirements
    """
    requirements = []
    with open("requirements.txt") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="SPI",
    version="0.0.1",
    author="Owais",
    author_email="owaisnawaz17@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
