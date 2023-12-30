import numpy as np
import polars as pl

def arr2df_melted(arr:np.ndarray,value_name:str="value")->pl.DataFrame:
    """Converts 2D array into structured dataframe (melted into longer format) with columns: "row", "col", "value".

    Parameters
    ----------
    arr : np.ndarray
        2D array with shape (M,N).
    
    value_name : str, optional
        Name of the column with values. The default is "value".

    Returns
    -------
    pl.DataFrame
        Structured dataframe (melted into longer format) with columns: "row", "col", "value".
    """

    M,N = len(arr),len(arr[0])

    # create dataframe from array and structure it with column names and row names
    df_mtx = pl.from_numpy(arr, # from 2D array 
                           schema=np.arange(1,N+1).astype(str).tolist(),orient="col" # set column names 1,2,3.. 
                           ).with_columns(row=pl.int_range(1,M+1) # add "row" column to keep track of row names upon melting
                                          ).select('row',pl.all().exclude('row')) # move "row" column to the first position
    
    # melt dataframe to long format to comply with "tidy data" principles
    df_melt = df_mtx.melt(id_vars='row', # repeat row values
                        variable_name="col", # bring column names to a new column
                        value_name=value_name  , # rename values column to "distance")
                        ).with_columns(pl.col('col').cast(pl.Int32)) #change "col" column to Int32 type
    
    return df_melt