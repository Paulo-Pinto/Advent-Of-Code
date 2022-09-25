import os, sys

if __name__ == "__main__":
    _, year, day, *_ = sys.argv

    path = os.path.join(os.getcwd(), f"__{year}__/{day:0>2}_")
    os.mkdir(path)
    open(f"{path}/test", "x")
    open(f"{path}/input", "x")
    open(f"{path}/{day}_solve.ipynb", "x")
