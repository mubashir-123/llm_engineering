import subprocess
import os

# /O2: Maximize speed
# /EHsc: Standard exception handling
# /Fe: Specify output executable name
compile_command = ["cl", "/O2", "/EHsc", "main.cpp", "/Fe:main.exe"]

# The executable produced
run_command = ["main.exe"]

# Compile
# Note: This requires running the script from a 'Developer Command Prompt for VS'
# or having run vcvarsall.bat beforehand.
compile_result = subprocess.run(compile_command, check=True, text=True, capture_output=True)

# Run
run_result = subprocess.run(run_command, check=True, text=True, capture_output=True)

print(run_result.stdout)