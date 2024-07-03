
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generate data for each day of the year
data = {
    "Day": np.arange(1, 366),
    "Average_Temperature": np.random.normal(loc=30, scale=5, size=365)
}

# Adding some specific data points to enrich the data
random_days = np.random.randint(1, 366, size=10)
for day in random_days:
    data["Average_Temperature"][day-1] = np.random.normal(loc=40, scale=2)

data_df = pd.DataFrame(data)

# Plotting using Seaborn
plt.figure(figsize=(12, 6))
sns_line = sns.lineplot(data=data_df, x="Day", y="Average_Temperature", color="#1f77b4")
sns_line.fill_between(data_df.Day, data_df.Average_Temperature, color="#1f77b4", alpha=0.3)

# Annotating the chart
plt.annotate('Summer Peak', xy=(172, data_df.loc[171, 'Average_Temperature']),
             xytext=(190, data_df.Average_Temperature.max() + 2),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Customize the appearance
sns_line.set_title('Yearly Average Temperature Trend in Metropolis City')
sns_line.set_xlabel('Day of the Year')
sns_line.set_ylabel('Average Temperature (°C)')
plt.show()