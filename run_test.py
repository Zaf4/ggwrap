import numpy as np
from ggwrap import heatmap
import lets_plot
from lets_plot import *
LetsPlot.setup_html()

from tests import test_heatmap

if __name__ == "__main__":
    ax = test_heatmap()
    ax.to_html("./images/test_heatmap.html")