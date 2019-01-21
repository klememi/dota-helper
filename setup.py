from setuptools import setup, find_packages


with open('README.rst') as f:
    long_description = ''.join(f.readlines())


setup(
    name='Dota 2 Companion',
    version='1.0',
    description='',
    long_description=long_description,
    author='Michal Klement',
    author_email='klememi1@fit.cvut.cz',
    license='MIT License',
    url='https://github.com/klememi/dota-helper',
    packages=find_packages(),
    python_requires='~=3.6',
    install_requires=[
        'click>=7.0', 
        'requests>=2.21.0',
        'ascii-graph>=1.5.1',
        'configparser>=3.5.0'],
    entry_points={
        'console_scripts': [
            'dotacli = companion.cli:main',
        ],
    },
    keywords='dota,moba,esport,gaming,cvut,fit',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Topic :: Games/Entertainment',
        'Topic :: Games/Entertainment :: Real Time Strategy',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        ],
    zip_safe=False,
)