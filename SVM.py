#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yee_172'
__date__ = '2017/9/12'

import random
import numpy as np

EPS = 0.000000001


def load_data(filename, data, dimension):
    """
    Load data from the file
    Data in file: label\tindex1:value1\tindex2:value2\tindex3:value3...
    Date in date: [[label, sample],[label, sample], ...], where sample: [v_0, v_1, v_2, v_3, ..., v_dim]
    """
    for line in open(filename, 'rt'):
        sample = np.zeros(dimension + 1)
        line = line.rstrip('\r\n\r')
        # Delete the tail if it exists
        fields = line.split('\t')
        label = int(fields[0])
        # label would be 1 or -1
        sample[0] = 1.0
        # set x_0 1.0
        for field in fields[1:]:
            kv = field.split(':')
            sample[int(kv[0])] = float(kv[1])
        data.append((label, sample))


def svm_train(data4train, W, iterations, lm, lr):
    """
    Training function
    Object function: obj(<X,y>, W) = (for all<X,y>SUM{max{0, 1 - W*X*y}}) + lm / 2 * ||W||^2, i.e. hinge+L2
    """
    # <sample, label> => <X, y>
    num_train = len(data4train)
    for i in range(iterations):
        index = random.randint(0, num_train - 1)
        X = data4train[index][1]
        y = data4train[index][0]
        WX = (W * X).sum()
        if 1 - WX * y > 0:
            grad = lm * W - X * y
        else:
            grad = lm * W - 0
        W = W - lr * grad
    return W


def svm_predict(data4test, W):
    """
    Prediction function
    """
    num_test = len(data4test)
    num_correct = 0
    for i in range(num_test):
        target = data4test[i][0]
        X = data4test[i][1]
        total = (X * W).sum()
        predict = 1 if total > 0 else -1
        if predict * target > 0:
            num_correct += 1
    return round(num_correct / num_test, 10)


# ---[test zone]---
# epochs = 100
# iterations = 10
# data4train = []
# data4test = []
# lm = 0.0001
# lr = 0.01
# dim = 1000
# W = np.zeros(dim + 1)
