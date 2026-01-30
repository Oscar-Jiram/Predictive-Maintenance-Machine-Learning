import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------
# 1. Load dataset (local CSV)
# --------------------------------------------

DATA_PATH = "ai4i2020.csv"

# --------------------------------------------
# 2. discover the dataset 
# --------------------------------------------

df = pd.read_csv(DATA_PATH)
# --------------------------------------------
# 3. Don't hide the columns
# --------------------------------------------

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# --------------------------------------------
# 4. Discover data frame column types and it's measurements
# --------------------------------------------

print(df.info())
print(df.describe())

# --------------------------------------------
# 5. Target Distribution
# --------------------------------------------

df["Machine failure"].value_counts(normalize=True) * 100
