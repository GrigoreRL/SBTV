import sys
from setuptools import find_packages
from cx_Freeze import setup, Executable

includefiles=['./Resources/rugr_fse_logoen_rood_rgb.png']
build_exe_options={"packages":["os","sys","matplotlib","numpy","numba"],'include_files':includefiles}

#base = "Win32GUI"
base = "Console"
setup(
name = "SBTV",
version = "0.1",
description="Test Description",
options = {"build_exe":build_exe_options},
executables=[Executable("mainFile.py",targetName = "SBTV.exe",base=base,icon='./icon.png')])