import pickle

import numpy as np
import plotly
import time
import random
import plotly.graph_objects as go

fig = go.Figure()

counting_file = open("results/counting.pkl", "rb")
avl_file = open("results/avl.pkl", "rb")

counting = np.array(pickle.load(counting_file), dtype=int)
avl = np.array(pickle.load(avl_file), dtype=int)

avl_file.close()
counting_file.close()

fig.add_trace(go.Scatter( x=avl[:, 0], y=avl[:, 1],  mode='lines', name='AVL Tree Sort'))
fig.add_trace(go.Scatter( x=counting[:, 0], y=counting[:, 1],  mode='lines',  name='Couting Sort'))

fig.update_layout(
    title='Sorting Algorithm Comparison: AVL Tree Sort vs Counting sort',
    xaxis_title='Array Size',
    yaxis_title='Time (seconds)',
)

fig.show()