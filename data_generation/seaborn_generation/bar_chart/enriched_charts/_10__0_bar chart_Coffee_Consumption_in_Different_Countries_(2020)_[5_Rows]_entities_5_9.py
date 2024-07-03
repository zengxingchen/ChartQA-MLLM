
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Total Precipitation (mm)': [78, 64, 89, 92, 105, 134, 158, 142, 120, 95, 83, 70]
}

# Create DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(12, 8))

# Plot the precipitation
sns.barplot(y="Total Precipitation (mm)", x="Month", data=df,
            palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
                     '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
                     '#1f77b4', '#ff7f0e'], edgecolor=".6", linewidth=2)

# Customize the axes and title
ax.set_ylabel('Total Precipitation (mm)')
ax.set_xlabel('Month')
ax.set_title('Monthly Precipitation Levels')

# Adjust bar width
for container in ax.containers:
    plt.setp(container, width=0.7)

# Show the plot
plt.show()