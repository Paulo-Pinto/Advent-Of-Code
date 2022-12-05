import os, sys
import nbformat as nbf
import subprocess as sb

def create_notebook_cell(title):
    open(title, "x")

    nb = nbf.v4.new_notebook()

    code = '''import re

def read_file(filename="test"):
    
    # lista, listb = open(filename).read().split("\\n\\n") # split by new line
    
    with open(filename) as fp:
        for line in fp.read().splitlines():
            
            x = re.split("[, -]", line)

            return x

read_file()'''

    nb['cells'].append(nbf.v4.new_code_cell(code))
    nbf.write(nb, title)

if __name__ == "__main__":
    _, year, day, *_ = sys.argv

    path = os.path.join(os.getcwd(), f"__{year}__/{day:0>2}_")
    os.mkdir(path)
    open(f"{path}/test", "x")
    # result = sb.call("wget ")
    open(f"{path}/input", "x").write("")
    create_notebook_cell(f"{path}/{day}_solve.ipynb")