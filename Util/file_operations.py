import os


def write(fPath, x):
    file = open(fPath, "a")
    file.write(x)
    file.close()

def read(fPath):
    file = open(fPath, "r")
    x = file.readline().strip()

    file.close()

    x = int(x)

    return x

def isEmpty(fPath):
    return os.path.getsize(fPath) == 0