
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Prepare the data
data = {
    'Year': list(range(2000, 2021)),
    'GDP_Growth_Rate': [4.1, 3.2, 2.5, 3.0, 4.2, 3.8, 4.5, 5.1, 1.9, -2.5, 2.9, 3.5, 2.8, 3.0, 3.1, 2.9, 1.6, 2.2, 2.9, 2.3, -3.4]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set the style
sns.set_style("whitegrid")

# Create the line chart
plt.figure(figsize=(12, 6))
ax = sns.lineplot(x='Year', y='GDP_Growth_Rate', data=df, color='#FF5733', linewidth=2.5)

# Annotating the last data point
plt.text(x=df['Year'].iloc[-1], y=df['GDP_Growth_Rate'].iloc[-1], s=f"{df['GDP_Growth_Rate'].iloc[-1]}%", 
         color='#FF5733', va='center', ha='center', fontsize=10)

# Setting the title and labels
plt.title('Annual GDP Growth Rate (2000-2020)', fontsize=16, loc='right')
plt.xlabel('Year', fontsize=12)
plt.ylabel('GDP Growth Rate (%)', fontsize=12)

# Display the plot
plt.show()