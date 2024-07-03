
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data provided as a list of dictionaries
data = [{'Online Orders Per Month': 10}, {'Online Orders Per Month': 15}, {'Online Orders Per Month': 1}, 
        {'Online Orders Per Month': 7}, {'Online Orders Per Month': 4}, {'Online Orders Per Month': 3}, 
        {'Online Orders Per Month': 12}, {'Online Orders Per Month': 6}, {'Online Orders Per Month': 20}, 
        {'Online Orders Per Month': 9}, {'Online Orders Per Month': 2}, {'Online Orders Per Month': 8}, 
        {'Online Orders Per Month': 5}, {'Online Orders Per Month': 17}, {'Online Orders Per Month': 3}]

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create the histogram using the DataFrame
plt.figure(figsize=(10, 6))  # Set the figure size
ax = sns.histplot(df['Online Orders Per Month'], bins=10, kde=False, color='skyblue')

# Add titles and labels
ax.set_title('Histogram of Online Orders Per Month', fontsize=16)
ax.set_xlabel('Online Orders Per Month', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)

# Customize the appearance of the plot
sns.despine(trim=True)  # Remove the top and right spines
plt.xticks(range(0, 21, 2))  # Set the x-axis ticks
plt.yticks(range(0, 5))  # Set the y-axis ticks

# Show the plot
plt.show()