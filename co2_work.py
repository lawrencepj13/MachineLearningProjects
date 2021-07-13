import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\Lawre\Documents\MSc Applied AI\Data Vis and Analytics\Datasets for Week 5 Activities-20210610\ch2_co2_levels.csv')

df = df.set_index('datestamp')
plt.style.use('classic')
ax = df.plot(color='blue')
ax.set_xlabel('Date')
ax.set_ylabel('CO2 Levels')
ax.set_title('CO2 Level change over time')
plt.show()

