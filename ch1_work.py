import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\Lawre\Documents\MSc Applied AI\Data Vis and Analytics\Datasets for Week 5 Activities-20210610\ch1_discoveries.csv')

pd.to_datetime(['2009/07/31', 'test'], errors='coerce')
plt.style.use('fivethirtyeight')
df_subset = df ['01-01-1870':'01-01-1875']
print(df_subset)
