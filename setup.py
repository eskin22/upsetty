from setuptools import setup, find_packages

setup(
    name='upsetty',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'plotly',
        'pandas',
        'numpy'
    ],
    author='eskin22',
    description='An upset plot creation package using Plotly'
)