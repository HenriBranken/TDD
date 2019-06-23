import os


def read_from_file(filename):
    if not os.path.exists(filename):
        raise Exception("Bad Path!")
    infile = open(filename, "r")  # open the passed in file
    line = infile.readline()  # read the first line
    return line  # return the first line
