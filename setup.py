"""setup.py controls the build, testing, and distribution of the egg"""
from setuptools import setup, find_packages


def get_requirements():
    """Reads the installation requirements from requirements.pip"""
    with open("requirements.pip") as reqfile:
        return [line for line in reqfile.read().split("\n") if not line.startswith(('#', '-'))]


setup(
    name='cookiecuttercatfacts',
    description="awesommmeeeeeeeeeeeeeeeeeeeeeeeeeee",
    packages=find_packages(),
    install_requires=get_requirements(),
    test_suite='nose.collector',
)
