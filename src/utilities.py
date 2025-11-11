#Import
import pandas as pd
import numpy as np


def outlier_check(df, cols, z):
    z_score = np.abs((df[cols] - df[cols].mean()) / df[cols].std())
    outliers_df = df[np.any(z_score > z, axis = 1)]
    return outliers_df.shape[0]