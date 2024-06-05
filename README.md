# foo_param

This package calculates the volume of a sphere using the Foo et al. parameterization.

## Installation

Clone the repository and install the package using pip:

```bash
git clone https://github.com/wasayq5/foo_param.git
cd foo_param
pip install .

```

## Usage
### With Command-Line Interface
Once the package is installed, navigate to the root of the software package and then run 

```bash
python -m foo_param <radius_of_sphere>
```
This lets you interact with the program using a command line interface to calculate the volume of a sphere with the given radius.

### As a Library
At the top of the python file where you want to import FooParameterization, add the import statement:

```python
from foo_param.foo import FooParameterization
```

You are then able to use Foo Parameterization in your file. You can then initialize an instance of a FooParameterization object and call its methods on the instance.

Sample Usage:
```python
foo_param = FooParameterization()
volume = foo_param.volume(radius)
print(f"The volume of a sphere with radius {radius} is {volume} (cubed units)")
```

## Testing
You can run unit tests with:

```bash
python -m unittest tests.test_foo
```
