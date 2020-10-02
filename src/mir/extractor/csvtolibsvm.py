import sys
import os
import tempfile

from ..settings import BASE_DIR


def csvtolibsvm(instrument_label, ifile):
    fout = tempfile.NamedTemporaryFile("w+", suffix="testinput.libsvm", delete=False)
    fin = open(ifile, "r")

    line = fin.readline()
    while line != "":
        vals = line.strip().split(",")
        fout.write(str(vals[-1]) + " ")

        for i in range(len(vals) - 1):
            fout.write(str(i + 1) + ":" + str(vals[i]) + " ")
        fout.write("\n")
        line = fin.readline()

    return fout.name