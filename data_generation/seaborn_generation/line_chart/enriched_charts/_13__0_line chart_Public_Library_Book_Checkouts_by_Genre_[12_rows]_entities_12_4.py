
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Prepare the data
data = {
    'Year': list(range(2000, 2021)),
    'Reading': [70, 72, 68, 75, 78, 80, 82, 81, 85, 87, 88, 89, 90, 91, 92, 94, 96, 97, 98, 99, 100]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set the style
sns.set_style("whitegrid")

# Create the line chart
plt.figure(figsize=(10, 5))
ax = sns.lineplot(x='Year', y='Reading', data=df, color='#1f77b4', linewidth=2.5)

# Annotating the last data point
plt.text(x=df['Year'].iloc[-1], y=df['Reading'].iloc[-1], s=f"{df['Reading'].iloc[-1]}%", 
         color='#1f77b4', va='center', ha='center', fontsize=10)

# Setting the title and labels
plt.title('Annual Rainfall Readings (2000-2020)', fontsize=16, loc='left')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Rainfall (mm)', fontsize=12)

# Display the plot
plt.show()