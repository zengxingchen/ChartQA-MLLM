
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Prepare the data
data = {
    'Year': list(range(2000, 2021)),
    'Global_Temperature_Anomaly': [0.42, 0.55, 0.63, 0.61, 0.53, 0.67, 0.63, 0.65, 0.54, 0.64, 0.72, 0.59, 0.62, 0.65, 0.74, 0.87, 0.99, 0.91, 0.85, 0.95, 1.02]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set the style
sns.set_style("whitegrid")

# Create the line chart
plt.figure(figsize=(14, 7))
ax = sns.lineplot(x='Year', y='Global_Temperature_Anomaly', data=df, color='#2E86C1', linewidth=2.5)

# Annotating the last data point
plt.text(x=df['Year'].iloc[-1], y=df['Global_Temperature_Anomaly'].iloc[-1], s=f"{df['Global_Temperature_Anomaly'].iloc[-1]}°C", 
         color='#2E86C1', va='center', ha='center', fontsize=10)

# Setting the title and labels
plt.title('Global Temperature Anomalies (2000-2020)', fontsize=16, loc='center')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperature Anomaly (°C)', fontsize=12)

# Display the plot
plt.show()