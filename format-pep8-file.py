#!/bin/python

import autopep8
import sys

def format_python_file(input_file, output_file=None):
    try:
        # Read the content of the input file
        with open(input_file, 'r') as f:
            input_code = f.read()

        # Format the code to PEP 8 standards
        formatted_code = autopep8.fix_code(input_code)

        # If an output file is specified, write the formatted code to it
        if output_file:
            with open(output_file, 'w') as f:
                f.write(formatted_code)
        else:
            # If no output file is specified, print the formatted code to the console
            print(formatted_code)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python format_pep8.py <input_file> [output_file]")
        sys.exit(1)

    input_file = sys.argv[1]
    
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
        format_python_file(input_file, output_file)
    else:
        format_python_file(input_file)
