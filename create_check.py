import os
import sys
from textwrap import dedent

def create_check(name):
    path = os.path.join(name)
    os.makedirs(path, exist_ok=True)

    with open(os.path.join(path, "__init__.py"), "w") as f:
        f.write(dedent(f"""
            from check50 import *

            class {name}(Checks):

                @check()
                def exists(self):
                    self.require("{name}.c")

                @check("exists")
                def compiles(self):
                    self.spawn("clang -o {name} {name}.c -lcs50 -lm").exit(0)
        """))

    with open(os.path.join(path, ".cs50.yml"), "w") as f:
        f.write(dedent(f"""
            submit50:
                files: &submit50_files
                    - !exclude "*"
                    - !include "{name}.c"
                    - !require {name}.c
                style: false

            check50:
                files: *submit50_files
        """))

def main():
    if len(sys.argv) < 2:
        print("Usage: script.py <name>")
        sys.exit(1)

    name = sys.argv[1]
    create_check(name)

if __name__ == "__main__":
    main()