
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Prepare the data
data = {
    'Year': list(range(1880, 2021)),
    'Temperature': [13.8 + 0.05 * (i // 10) for i in range(141)]  # simplified model
}

# Create DataFrame
df = pd.DataFrame(data)

# Set the style
sns.set_style("whitegrid")

# Create the line chart
plt.figure(figsize=(12, 6))
ax = sns.lineplot(x='Year', y='Temperature', data=df, color='#FF5733', linewidth=2.5)

# Annotating the last data point
plt.text(x=df['Year'].iloc[-1], y=df['Temperature'].iloc[-1], s=f"{df['Temperature'].iloc[-1]}°C", 
         color='#FF5733', va='center', ha='center', fontsize=10)

# Setting the title and labels
plt.title('Global Average Temperatures (1880-2020)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)

# Display the plot
plt.show()