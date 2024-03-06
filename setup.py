from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()


setup(
    name='upsetty',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'plotly',
        'pandas',
        'numpy'
    ],
    author='eskin22',
    author_email='blakepmcbride@gmail.com',
    description='An UpSet plot creation package using Plotly',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/eskin22/upsetty',
    download_url='https://pypi.org/project/upsetty/',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers', 
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    keywords=[
        'upset',
        'upset-plot',
        'upsetplot',
        'set-interaction',
        'set-intersection',
        'set-interactions',
        'sets',
        'plotting',
        'visualization',
        'data-visualization',
        'visualization-tools',
        'data-visualization-tools',
        'python',
        'python3',
        'python310',
        'pandas',
        'plotly'
    ]
)