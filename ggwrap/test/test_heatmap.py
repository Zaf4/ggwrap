import numpy as np
from core import heatmap
import lets_plot
from lets_plot import *
LetsPlot.setup_html()


def test_heatmap(**kwargs)->lets_plot.plot.core.PlotSpec:
    arr1 = np.random.randn(40)
    dist_mtx = np.zeros((40, 40))
    for i,a in enumerate(arr1):
        dist_mtx[i] = np.abs(arr1 - a)
    
    return heatmap(dist_mtx,**kwargs)


if __name__ == "__main__":
    ax = test_heatmap()
    ax.to_html("heatmap.html")