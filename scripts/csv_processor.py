#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:18:10 2019

@author: kristen.anderson101gmail.com
"""
import pandas as pd
import numpy as np

input_file_name = 'test_toxicity.csv'
output_file_name = 'int_test.csv'

df=pd.read_csv(input_file_name, sep=',',header=None)
data = df.values
label = data[0]
label[0] = 'id'
data = data[1:]

for i in [0, 1, 3, 4, 5, 6, 7, 8]:
    data[:, i] = np.round(data[:, i].astype('float')).astype('int')

with open(output_file_name, 'w') as file:
    file.write(','.join(label.tolist()) + '\n')
    for line in data:
        line = [str(ele) for ele in line.tolist()]
        line[2] = '"' + line[2].replace('"', '""') + '"'
        line_joined = ','.join(line)
        file.write(line_joined + '\n')
        
