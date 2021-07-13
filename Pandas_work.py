import pandas as pd
import seaborn as sn
import  matplotlib.pyplot as plt
#created data set and put into a dataframe
data = {'A': [45,37,42,35,39],'B': [38,31,26,28,33],'C': [10,15,17,21,12]}

df = pd.DataFrame(data, columns=['A', 'B', 'C'])

#create correlation matrix

corrMatrix = df.corr()

#create a heatmap using seaborn

sn.heatmap(corrMatrix, annot=True)

plt.show()

