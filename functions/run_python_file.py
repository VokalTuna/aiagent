import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_work = os.path.abspath(working_directory)
    abs_file = os.path.abspath(os.path.abspath.join(working_directory, file_path))

    if not abs_file.startswith(abs_work):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_file):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    #todo
    # subprocess.run()
