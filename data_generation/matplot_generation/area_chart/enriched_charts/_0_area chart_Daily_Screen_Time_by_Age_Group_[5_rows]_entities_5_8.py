
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assume that 'data.csv' is the CSV file containing the above data.
# Please create such a file or substitute with pandas DataFrame directly.
data = pd.read_csv('data.csv')

plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

# Creating an area chart
ax = sns.lineplot(data=data, x='Day', y='AverageTemperature')
ax.fill_between(data.Day, data.AverageTemperature, color="#3399FF", alpha=0.5)

# Annotating the highest temperature
highest_temp = data.AverageTemperature.max()
highest_day = data.Day[data.AverageTemperature.idxmax()]
plt.annotate(f'Highest\n{highest_temp} °C', xy=(highest_day, highest_temp), xytext=(highest_day+2, highest_temp),
             arrowprops=dict(facecolor='#FF5733', shrink=0.05))

# Adding chart title and labels
plt.title('Average Daily Temperature in January')
plt.xlabel('Day')
plt.ylabel('Average Temperature (°C)')

# Display the chart
plt.show()