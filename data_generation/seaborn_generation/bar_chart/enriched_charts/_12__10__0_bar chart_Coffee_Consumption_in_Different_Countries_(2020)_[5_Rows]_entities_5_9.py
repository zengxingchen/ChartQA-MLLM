
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average Temperature (°C)': [2, 3, 7, 12, 17, 21, 24, 23, 19, 14, 8, 3]
}

# Create DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 6))

# Plot the temperature
sns.barplot(x="Average Temperature (°C)", y="Month", data=df,
            palette=['#FF6347', '#FFA07A', '#FFD700', '#ADFF2F', '#32CD32', 
                     '#3CB371', '#20B2AA', '#4682B4', '#1E90FF', '#4169E1', 
                     '#8A2BE2', '#DA70D6'], edgecolor=".6", linewidth=1.5)

# Customize the axes and title
ax.set_xlabel('Average Temperature (°C)')
ax.set_ylabel('Month')
ax.set_title('Monthly Average Temperatures', pad=20)

# Adjust bar width
for container in ax.containers:
    plt.setp(container, height=0.6)

# Show the plot
plt.show()