# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
wine_correlation = dataiku.Dataset("wine_correlation")
wine_correlation_df = wine_correlation.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

output_corr_df = wine_correlation_df # For this sample code, simply copy input to output


# Write recipe outputs
output_corr = dataiku.Dataset("output_corr")
output_corr.write_with_schema(output_corr_df)