import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

df=pd.read_csv("motor_data 14-2018.csv")
df.head()
#info on columns and rows
df.info()
#info on the summary statistics
df.describe
#checking for missing values
df.isna().sum()
