import numpy as np
import lets_plot
from lets_plot import *
LetsPlot.setup_html()

#relative imports
from ..ops import arr2df_melted

# function : heatmap
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

if __name__ == "__main__":
    pass
