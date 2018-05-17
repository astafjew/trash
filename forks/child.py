import os
import sys

print(f'Hello from child {os.getpid()} {sys.argv[1]}')
