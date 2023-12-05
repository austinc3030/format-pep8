#!/bin/python

import autopep8
import os

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
            # If no output file is specified, overwrite the input file with the formatted code
            with open(input_file, 'w') as f:
                f.write(formatted_code)
    
    except Exception as e:
        print(f"An error occurred: {e}")

def format_python_files_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                format_python_file(file_path)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python format_pep8.py <directory>")
        sys.exit(1)

    input_directory = sys.argv[1]
    format_python_files_in_directory(input_directory)
