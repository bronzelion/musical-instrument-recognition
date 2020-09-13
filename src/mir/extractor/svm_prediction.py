"""SVM Predictions from pre-computed model."""
#!/usr/bin/python

import os
import operator

from svmutil import svm_load_model, svm_read_problem, svm_predict

from ..settings import BASE_DIR


def predict(input_file):
    count = {}
    inst = {1: "FLUTE", 2: "GUITAR", 3: "VIOLIN", 4: "PIANO"}
    model = svm_load_model(os.getenv("MIR_MODEL_PATH"))
    y, x = svm_read_problem(input_file)

    p_labels, p_acc, p_vals = svm_predict(y, x, model)

    for i in range(1, 5, 1):
        count[i] = p_labels.count(i)
    predicted_inst = sorted(count.iteritems(), key=operator.itemgetter(1))
    predicted_inst.reverse()
    print ("Prediction Results (Class : Count)", predicted_inst)
    return (inst[predicted_inst[0][0]])

