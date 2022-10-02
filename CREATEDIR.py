import os, sys
import nbformat as nbf

def create_notebook_cell(title):
    open(title, "x")

    nb = nbf.v4.new_notebook()

    code = '''\
def read_file(filename="test"):
    with open(filename) as fp:
        for line in fp.readlines():
            
            x = line.strip().split(" ")

            return x
read_file()'''
    nb['cells'].append(nbf.v4.new_code_cell(code))
    nbf.write(nb, title)

if __name__ == "__main__":
    _, year, day, *_ = sys.argv

    path = os.path.join(os.getcwd(), f"__{year}__/{day:0>2}_")
    os.mkdir(path)
    open(f"{path}/test", "x")
    open(f"{path}/input", "x")
    create_notebook_cell(f"{path}/{day}_solve.ipynb")