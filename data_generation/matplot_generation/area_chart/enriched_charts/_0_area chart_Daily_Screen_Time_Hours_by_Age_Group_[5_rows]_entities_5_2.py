
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    "Day": list(range(1, 32)),
    "Average_Temperature": [35.0, 35.5, 35.2, 34.9, 35.1, 36.0, 36.5,
                            36.3, 36.7, 37.0, 37.5, 37.8, 38.0, 38.1,
                            38.5, 38.3, 38.7, 38.9, 39.1, 39.3, 39.2,
                            39.0, 38.8, 38.6, 38.4, 38.3, 38.2, 38.0,
                            37.9, 37.7, 37.6]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create the area plot
plt.figure(figsize=(12, 6))
area_chart = sns.lineplot(data=df, x='Day', y='Average_Temperature', color="#1f77b4")
area_chart.fill_between(df['Day'], df['Average_Temperature'], color="#1f77b4", alpha=0.3)

# Annotate a specific day
plt.annotate('Highest Avg Temp',
             xy=(14, 38.1),
             xytext=(20, 38.5),
             arrowprops=dict(facecolor='#333333', shrink=0.05),
             )

# Add chart title and labels
plt.title('Average Daily Temperature in January')
plt.xlabel('Day of the Month')
plt.ylabel('Temperature (°C)')

# Show the plot
plt.show()