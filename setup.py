import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

os.environ['TCL_LIBRARY'] = r"C:\Users\sahil\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\sahil\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable(
    'file_extractor.py', base=base, icon='file_ico.ico')]

cx_Freeze.setup(

    name="File Extractor",
    options={'build_exe': {'packages': ['tkinter', 'os', 'shutil'], "include_files": [
        "file_ico.ico", 'tcl86t.dll', 'tk86t.dll', 'file_logo.png']}},
    version="0.0.01",
    description="Tkinter Application",
    executables=executables
)
