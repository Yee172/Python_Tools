#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yee_172'
__data__ = '2017/9/12'

import sys
import numpy as np

EPS = 0.000000001

def load_data(filename, data, dim):
    """
    Load data from the file
    Data in file: label\tindex1:value1\tindex2:value2\tindex3:value3...
    Date in date: [[label, sample],[label, sample], ...], where sample: [v_0, v_1, v_2, v_3, ..., v_dim]
    """
    for line in open(filename, 'rt'):
        sample = [0.0 for v in range(0, dim + 1)]
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

