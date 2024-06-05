from setuptools import setup, find_packages

setup(
    name='foo_param',
    version='0.1',

    # find_packages() is provided by setuptools and automatically discovers all packages and subpackages in the project directory
    # This line ensures that all subdirectories in your project that are python packages (i.e. contain an __init__.py file) are included when the package is built and distributed
    packages=find_packages(),
    install_requires=[],

    #'entry_points' is a mechanism in 'setuptools' to specify what scripts should be made available as comman-line executables when your package is installed
    #'console scripts' creates command line tools
    #foo_param=foo_param:main' means that when the command foo_param is run in the terminal, it should execute the main function defined in the foo_param/__init__.py module.
    entry_points={
        'console_scripts': [
            'foo_param=foo_param:main',
        ],
    },
    author='Wasay Qureshi',
    author_email='waaspad@gmail.com',
    description='A package for Foo et al. parameterization',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/wasayq5/foo_param',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
