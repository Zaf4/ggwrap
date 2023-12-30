import numpy as np
import polars as pl
import lets_plot
from lets_plot import *
from ..ops import arr2df_melted
LetsPlot.setup_html()


def heatmap(arr:np.ndarray,value_name:str="value")->lets_plot.plot.core.PlotSpec:
    """Heatmap of the given 2D array.

    Parameters
    ----------
    arr : np.ndarray
        2D array of values with shape.
    value_name : str, optional
        Column name to appoint for values (e.g., distance) of each point to another,
        by default "value"

    Returns
    -------
    lets_plot.plot.core.PlotSpec
        Heatmap plot. 
        
        It is a lets-plot object that can be further customized.
        As lets_plot follows the grammar of graphics, you can add layers to the plot
        and further customize and modify each layer.
    """

    df = arr2df_melted(arr,value_name=value_name)
    ax = (ggplot(df, aes('col', 'row', fill=value_name)) + 
          geom_tile() + 
          scale_y_reverse()+
          scale_fill_viridis()
    )
    return ax

def test_heatmap(**kwargs)->lets_plot.plot.core.PlotSpec:
    arr1 = np.random.randn(40)
    dist_mtx = np.zeros((40, 40))
    for i,a in enumerate(arr1):
        dist_mtx[i] = np.abs(arr1 - a)
    
    return heatmap(dist_mtx,**kwargs)


if __name__ == "__main__":
    ax = test_heatmap()
    ax.to_html("heatmap.html")