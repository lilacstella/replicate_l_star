from setuptools import setup, find_packages

setup(
    name='l_star',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'automathon==0.0.15',
        'graphviz==0.16',
    ],
    include_package_data=True,
    description='An implementation of the L* algorithm',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lilacstella/replicate_l_star',
    author='Stella Yang',
    author_email='stella@stellayang.dev',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)