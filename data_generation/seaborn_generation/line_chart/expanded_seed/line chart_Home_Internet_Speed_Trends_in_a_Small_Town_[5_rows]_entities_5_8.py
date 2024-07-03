
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# First, we convert the dictionary to a pandas DataFrame
data = [
    {'Year': 2017, 'Average Download Speed (Mbps)': 20, 'Average Upload Speed (Mbps)': 5},
    {'Year': 2018, 'Average Download Speed (Mbps)': 25, 'Average Upload Speed (Mbps)': 10},
    {'Year': 2019, 'Average Download Speed (Mbps)': 30, 'Average Upload Speed (Mbps)': 15},
    {'Year': 2020, 'Average Download Speed (Mbps)': 50, 'Average Upload Speed (Mbps)': 20},
    {'Year': 2021, 'Average Download Speed (Mbps)': 70, 'Average Upload Speed (Mbps)': 25}
]
df = pd.DataFrame(data)

# Then, we set the aesthetic style of the plots
sns.set_style('whitegrid')

# We'll plot the lines for download and upload speeds separately for more customizations
plt.figure(figsize=(10, 6))

# Plotting the Average Download Speed
sns.lineplot(data=df, x='Year', y='Average Download Speed (Mbps)', 
             label='Download Speed', color='blue', marker='o', linestyle='-', linewidth=2.5)

# Plotting the Average Upload Speed
sns.lineplot(data=df, x='Year', y='Average Upload Speed (Mbps)', 
             label='Upload Speed', color='red', marker='s', linestyle='--', linewidth=2.5)

# Adding a title and labels
plt.title('Average Download and Upload Speeds Over Years', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Speed (Mbps)', fontsize=14)

# Display legend
plt.legend()

# Optional: Customize the ticks and their labels if needed
plt.xticks(df['Year'], labels=[str(year) for year in df['Year']])
plt.yticks(range(0, 81, 10))

# Show the plot
plt.show()