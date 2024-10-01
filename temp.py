import os
import pickle
from os.path import isfile, join
import re

arr = [0.0,
0.0,
0.0,
0.0,
0.0,
0.0,
0.01,
0.01,
0.02,
0.04,
0.06,
0.09,
0.12,
0.17,
0.23,
0.32,
0.4,
0.52,
0.69,
0.86,
1.05,
1.35,
1.71,
2.04,
2.57,
3.15,
3.63,
4.43,
5.07,
6.28,
7.3,
8.13,
9.89,
10.94,
13.0,
14.45,
16.49,
18.33,
21.62,
24.79,
27.23,
29.19,
34.8,
36.88,
39.33,
43.79,
48.68,
52.08,
57.19,
65.2,
71.88,
76.22,
89.52,
96.3,
95.77,
101.44,
106.94,
120.9,
129.51,
138.91,
149.34]

mypath = "datasets"
onlyfiles = sorted([int(re.findall(r'\d+', f)[0]) for f in os.listdir(mypath) if isfile(join(mypath, f))])

results = list(zip(onlyfiles, arr))
file = open("results/avl.pkl", 'wb')
pickle.dump(results, file)
file.close()