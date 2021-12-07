#! python3
#! PATH.py - Adds the directory needed for these tools to work to the PATH environment variable.

from os import environ, pathsep

environ["PATH"] += pathsep + "C:\\Search-Tools\\Batch Files"