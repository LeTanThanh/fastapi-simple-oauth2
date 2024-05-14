import sys

paths = (__file__).split("/")
paths.pop() # __init__.py
paths.pop() # depends

ROOT_PATH = "/".join(paths)
sys.path.append(ROOT_PATH)
