from setuptools import setup, find_packages

setup(
    name='evaluation',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy==1.24.2',
    ],
    test_suite='test_evaluation',
)