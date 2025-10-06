import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    current_directory = os.path.join(working_directory, directory)
    abs_cur = os.path.abspath(current_directory)
    abs_wor = os.path.abspath(working_directory)

    if not abs_cur.startswith(abs_wor):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_cur):
        return f'Error: "{directory}" is not a directory'
    try:
        results = []
        for content in os.listdir(abs_cur):
            check = os.path.join(abs_cur, content)
            file_size = 0
            is_dir = os.path.isdir(check)
            file_size = os.path.getsize(check)
            results.append(f"- {content}: file_size={file_size}, is_dir={is_dir}")
        return "\n".join(results)
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
