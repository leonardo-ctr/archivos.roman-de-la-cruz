import os
try:
    os.rmdir("c:\pr1.arch.roman de la cruz.9999")
except OSError as e:
    print(f"Error: {e.strerror}")

