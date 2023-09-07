#!/usr/bin/python3
import pyclbr

def print_names_from_pyc(pyc_file_path):
    try:
        module_data = pyclbr.readmodule_ex('hidden_4', [pyc_file_path])
        names = [name for name, item in module_data.items() if not name.startswith('__')]

        sorted_names = sorted(names)
        for name in sorted_names:
            print(name)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    pyc_file_path = "hidden_4.pyc"
    print("Printing names from compiled module:")
    print_names_from_pyc(pyc_file_path)
