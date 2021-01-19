import sys
from . import export

if __name__ == "__main__":
    command = sys.argv[1]
    if command == "export":
        export.export()
    else:
        print(f"Command %s not found" % sys.argv[1])
