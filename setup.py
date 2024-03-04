from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()


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
    description='An upset plot creation package using Plotly',
    long_description=long_description,
    long_description_content_type="text/markdown"
)