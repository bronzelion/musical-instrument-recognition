#!/usr/bin/python
# SVM Predictions from pre-computed model
from svmutil import *
import operator
from ..settings import BASE_DIR


def predict():
    count = {}
    inst = {1: "FLUTE", 2: "GUITAR", 3: "VIOLIN", 4: "PIANO"}
    model = svm_load_model(os.path.join(BASE_DIR, "model/four_instruments.model"))
    y, x = svm_read_problem(os.path.join(BASE_DIR, "testinput.libsvm"))

    p_labels, p_acc, p_vals = svm_predict(y, x, model)

    for i in range(1, 5, 1):
        count[i] = p_labels.count(i)
    predicted_inst = sorted(count.iteritems(), key=operator.itemgetter(1))
    predicted_inst.reverse()
    print ("PRED", predicted_inst)
    confidence = predicted_inst[0][1] / len(p_labels)
    return (
        inst[predicted_inst[0][0]]
        + " with a confidence of "
        + str(confidence * 100)
        + "%"
    )
    # print 'Max occ' +str(max(count))
    # print p_acc
    # print p_vals


if __name__ == "__main__":
    predict()
