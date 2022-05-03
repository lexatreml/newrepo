# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
wine_correlation = dataiku.Dataset("wine_correlation")
wine_correlation_df = wine_correlation.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df = wine_correlation_df[wine_correlation_df['corr'] < 0.75]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
#assign new dataframe to output
output_corr_df = df.copy()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
output_corr = dataiku.Dataset("output_corr")
output_corr.write_with_schema(output_corr_df)