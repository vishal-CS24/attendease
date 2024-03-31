import cx_Freeze
import sys
import os
from mysql.connector.locales.eng import client_error
base = None


if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Python\Python311\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Python\Python311\tcl\tk8.6"

executables = [cx_Freeze.Executable(
    "attendease.py", base=base, icon="pictures/icon.ico")]

cx_Freeze.setup(
    name="ATTENDEASE",
    options={"build_exe": {"packages": ["tkinter", "os"], "include_files": [
        "pictures/icon.ico", 'tcl86t.dll', 'tk86t.dll', 'pictures', 'Data', 'database', 'Attendance_files']}},
    version="1.0",
    description="Face Recognization based Attendance system using LBPH Algorithm",
    executables=executables
)
