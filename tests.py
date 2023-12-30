import numpy as np
from ggwrap import heatmap
import lets_plot
from lets_plot import *
LetsPlot.setup_html()

def make_matrix_NN(N:int)->np.ndarray:
    arr1 = np.random.randn(N)
    dist_mtx = np.zeros((N, N))
    for i,a in enumerate(arr1):
        dist_mtx[i] = np.abs(arr1 - a)

    return dist_mtx

def test_heatmap(**kwargs)->lets_plot.plot.core.PlotSpec:
    # Test for ggwrap.heatmap
    mtx = make_matrix_NN(40)
    return heatmap(mtx,**kwargs)

# listing functions 
__all__ = ["test_heatmap"]

if __name__ == "__main__":
    print("avaliable tests:\n",__all__)