#setup.py
from cx_Freeze import setup, Executable
setup(
    name = "coinium",
    version = "1.0.0",
    options = {"build_exe": {
        'packages': ["wx", "os","sys","ctypes","win32con"],
        'include_msvcr': True,
    }},
    executables = [Executable("obfuscated_graph.py",base="Win32GUI")]
    )