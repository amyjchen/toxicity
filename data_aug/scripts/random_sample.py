import csv
import sys
import random
import pandas as pd 

filename = sys.argv[1]

num = int(sys.argv[2])

df = pd.read_csv(filename + '.csv')

df = df.sample(num)

df.to_csv(filename + '_sampled.csv', encoding='utf-8', index=False)

