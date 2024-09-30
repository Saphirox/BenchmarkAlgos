import glob
import os
import pickle
import random

num_datasets = 100
datasets = []


files = glob.glob('datasets/*')
for f in files:
    os.remove(f)

for idx in range(1, num_datasets+1):
    value = int(100 + idx**4)
    min_value = -value
    max_value = value
    dataset = [random.randint(min_value, max_value) for _ in range(value)]
    datasets.append(dataset)
    file = open("datasets/ds_" + str(value) + ".pkl", 'wb')
    pickle.dump(dataset, file)
    file.close()
