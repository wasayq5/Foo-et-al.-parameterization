from .foo import FooParameterization
import argparse

#This file creates the command line interface users ca use in the terminal to use/test Foo Parameterization

def main():

    #Create the argument parser
    parser = argparse.ArgumentParser(description="Caclulate the volume of a sphere with Foo Parameterization")

    #Add argument for the radius of the sphere
    parser.add_argument('radius', type = float, help = 'Add an argument for the radius of the sphere')

    #Parse the arguments
    args = parser.parse_args()

    #Create instance of Foo Parameterization and calculate the volume
    foo_param = FooParameterization()
    volume = foo_param.volume(args.radius)

    #print volume
    print(f"The volume of this sphere is {volume} (cubed units)")
    
# Allow script to be run directly from command line
if __name__ == "__main__":
    main()